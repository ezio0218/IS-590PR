###########################################################################################################
# IS 590 PR ###############################################################################################
# 02/07/19 ################################################################################################
# Spring 2019 ###############################################################################4#############
# HW3 #####################################################################################################
# We work together and discuss along the way ##############################################################
# Worawich Chaiyakunapruk [wchaiy2] --- mostly table, list ################################################
# Yao Xiao [yaoxiao9] - mostly functions, global list #####################################################

from pygeodesy import ellipsoidalVincenty as ev  # import this to for geo calculation
import math                                      # import this just for pi value

def disCalculate(location1,location2):           # function to calculate storm moving distance
    distance = []                                # prepare all the lists for calculating variables
    Lation = []
    total = 0
    for a in range(len(location1)):              # calculation all the lat long to find the distance then add them together
        Lation.append(ev.LatLon(location1[a], location2[a]))
    for b in range((len(location1)-1)):
        distance.append(Lation[b].distanceTo(Lation[b+1])/1852.0)
    for c in range(len(distance)):
        total = total + distance[c]
    distance.clear()                             # clear variable list for next use
    Lation.clear()
    if total == 0:
        line_list.append("N/A")                  # this append to output table
#         print('The Storm did not move!')
    else:
        total = str(round(total,2))
        line_list.append(str(total))
#         print('The distance it traveled is:', total)
    return total


def getHeader(values_on_line):           # function to get header (name, id)
    ID, name, nelement = values_on_line  # put value in line into variables
    nelement = int(nelement)             # how many lines are there
    #     print("Storm ID:", ID)
    if name != "UNNAMED":                # if not unnamed
        if len(name) >= 8:               # then add data line normal
            name = name
        else:                            # but if unnamed
            name = name
        line_list.append(name)
        line_list.append(str(ID))
    #         print("Strom name:", name)
    else:
        line_list.append("N/A")         # put N/A in place of the name
        line_list.append(str(ID))       # global list for summary and return ID
    #         print("No storm name.")
    #print(ID)
    ID_list.append(ID)
    top10_dict.update({ID: None})
    #print(ID)
    return ID, name, nelement

def SpeedCalculate(location1,location2,date,time):  # function to calculate propagation speed
    epoch = []
    distance = []
    Lation = []
    speed = []
    total = 0
    epc = 0
    for a in range(len(location1)):
        Lation.append(ev.LatLon(location1[a], location2[a]))
    for b in range((len(location1)-1)):
        distance.append(Lation[b].distanceTo(Lation[b+1])/1852.0)
        if (int(date[b+1])-int(date[b])) > 0:
            ep = int(time[b+1])-int(time[b])+2400
        else:
            ep = int(time[b+1])-int(time[b])
        if ep % 100 == 0:
            epo = float(ep/100)
        else:
            epo = ep//100 + float((ep % 100)/60)
        epoch.append(epo)
    for c in range(len(distance)):
        speed.append(distance[c]/epoch[c])
        total = total + distance[c]
        epc = epc + epoch[c]
    if speed == []:
        mean_list.append(0)
        line_list.append('N/A')               # append to table
        line_list.append('N/A')
#         print('The Storm did not have speed!')
    else:
        mean_speed = total/epc
        max_speed = max(speed)
        mean_list.append(mean_speed)
        epoch.clear()
        distance.clear()
        Lation.clear()
        speed.clear()
#         if max_speed == 0.0:
#             max_speed = str(max_speed)+"\t\t"
#         if mean_speed == 0.0:
#             mean_speed = str(mean_speed)+"\t\t"
        if mean_speed == 0.0:
            line_list.append(str(mean_speed))
        if max_speed == 0.0:
            line_list.append(str(max_speed))
        line_list.append(str(round(mean_speed,2)))   # append to table, rounded to 2 significant digit
        line_list.append(str(round(max_speed,2)))
#         print('The mean propagation speed is: (Knots)', mean_speed, 'The maximum propagation speed is: (Knots)', max_speed)
        return mean_speed, max_speed

def StormEnergy(max_wind,date,time):                 # function to calculate storm energy
    Power = []
    epoch = []
    Energy = []
    total = 0
    for a in range(len(max_wind)):
        Power.append(float(max_wind[a])**3)
    for b in range((len(date)-1)):
        if (int(date[b+1])-int(date[b])) > 0:
            ep = int(time[b+1])-int(time[b])+2400
        else:
            ep = int(time[b+1])-int(time[b])
        if ep % 100 == 0:
            epo = float(ep/100)
        else:
            epo = float(ep//100) + float((ep % 100)/60)
        epoch.append(epo)
    for c in range(len(epoch)):
        energy = epoch[c]*Power[c+1]
        Energy.append(energy)                        # global list for summary energy
    for d in range(len(Energy)):                     # append to table
        total = total + Energy[d]
    if Energy == []:
        Energy_list.append(-99999)                   # global list for summary energy
        line_list.append("N/A")                      # append to table
#         print('The Storm did not have energy!')
    else:
        Energy_list.append(total)
        line_list.append(str(total))
#         print("The Storm's TRSE is", total)
    #print('Power',Power)
    #print('Energy',total)
    epoch.clear()
    Power.clear()
    Energy.clear()

def HUArea(extent1,extent2,extent3,extent4):          # function to calculate area
    area_list = []
    for i in range(len(extent1)):
        if int(extent1[i]) == -999 or int(extent2[i]) == -999 or int(extent3[i]) == -999 or int(extent4[i]) == -999:
            area = 'N/A'
        else:
            area = (1/4)*math.pi*(float(extent1[i])**2)+(1/4)*math.pi*(float(extent2[i])**2+(1/4)*math.pi*(float(extent3[i])**2+(1/4)*math.pi*(float(extent4[i])**2)))
            area_list.append(area)
    if area_list == []:
        Area_list.append(-99999)
        line_list.append("N/A")
#         print('The storm did not have largest area')
    else:
        Area_list.append(max(area_list))                       # global list for summary
        line_list.append(str(round(max(area_list),2)))         # append to table
#         print("The storm's largest area is", max(area_list))

def top10_prop():                                              # function to sort top 10 propagation speed
    top10 = sorted(mean_list, reverse=True)[:10]               # sort mean_list into descending order, pick first 10
    print("The 10 fastest-propagating storms (from mean propagation) are")
    print("Storm ID\t","Mean propagation")
    for i in range(10):                                        # iterate by size of 10 for top 10
        max_val = top10[i]
        print(ID_list[mean_list.index(max_val)], "\t", mean_list[mean_list.index(max_val)] )


def top10_TRSE():                                              # function to sort top 10 TRSE
    top10 = sorted(Energy_list, reverse=True)[:10]
    print("\n\nThe 10 most-energetic storms (from TRSE) are")
    print("Storm ID\t","TRSE")
    for i in range(10):
        max_val = top10[i]
        print(ID_list[Energy_list.index(max_val)], "\t", Energy_list[Energy_list.index(max_val)] )


def top10_area():                                              # function to sort top 10 areas
    top10 = sorted(Area_list, reverse=True)[:10]
    print("\n\nThe 10 biggest hurricanes (from maximum hurricane-level surface area) are")
    print("Storm ID\t","Max hurricane surface area")
    for i in range(10):                                        # iterate by size of 10 for top 10
        max_val = top10[i]
        print(ID_list[Area_list.index(max_val)], "\t", Area_list[Area_list.index(max_val)] )

def putTable():                                                # function to put everything into nice table
    for i in range(len(data_list)):
        print('\n', end="", flush=True)
        for j in range(len(data_list[0][:])):
            print('|'+data_list[i][j].center(20)+'|', end="", flush=True)


def main():                                                   # main function to define all the veriable and call the functions in order
    i = 1                                                     # line counter
    j = 1                                                     # temporary line counter >>>> use as Number of best track entries counter to catch up and a flag as we got data written down
    global mean_list                                          # we need some global lists for the summary
    mean_list = []
    global ID_list
    ID_list = []
    global data_list
    data_list = [
        ["Strom name", "Storm ID", "Distance travel ", "Mean propagation", "Max propagation", "TRSE","Max hurricane surface area"]]
    global line_list                                          # global list to add data to make the table
    line_list = list()
    #print(data_list)
    temp_data = list()
    global Energy_list
    Energy_list = []
    global Area_list
    Area_list = []
    global top10_dict
    top10_dict = {}
    for filename in ['hurdat2-1851-2017-050118.txt', 'hurdat2-nepac-1949-2017-050418.txt']:
        path = '/Users/xy/Downloads/' + filename
        if filename == 'hurdat2-1851-2017-050118.txt':
            print('The result for hurdat2-1851-2017-050118.txt is:')
        else:
            print('\nThe result for hurdat2-nepac-1949-2017-050418.txt is:')
        location1 = list()  # make corresponding lists to list all the date of each storm
        location2 = list()
        time = list()
        date = list()
        max_wind = list()
        extent1 = list()
        extent2 = list()
        extent3 = list()
        extent4 = list()
        with open(path, 'r') as f:
            for line in f:  # looping read ONLY ONE line from the file
                line = line.replace(',\n', '')  # replace comma and new line with nothing (end of line)
                line = line.replace(' ', '')
                values_on_line = line.split(
                    ",")  # Split string at comma (,) into list of "words" which are number strings.

                if not (line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))):

                    if i == j:  # When i=j it's the first header
                        ID, name, nelement = getHeader(values_on_line)

                        j += 1  # Line counter when meet a header
                        i += 1  # Line counter for the first line only
                    if i == j + nelement:  # If i counter equal to j counter plus the element of each storm (which means we already got all data in that storm) then go into this loop
                        disCalculate(location1, location2)
                        SpeedCalculate(location1, location2, date, time)
                        StormEnergy(max_wind, date, time)
                        HUArea(extent1, extent2, extent3, extent4)

                        location1.clear()  # reset the list counter since we are done with this storm
                        location2.clear()
                        time.clear()
                        date.clear()
                        max_wind.clear()
                        extent1.clear()
                        extent2.clear()
                        extent3.clear()
                        extent4.clear()
                        #print(line_list)
                        data_list.append(list(line_list))
                        line_list.clear()
                        ID, name, nelement = getHeader(values_on_line)
                        i += 1  # line counter for header
                        j = i  # reset the j value to i (difference in i, j are the number of data line)
                else:

                    time.append(values_on_line[1])
                    date.append(values_on_line[0])
                    location1.append(values_on_line[4])  # put the date into datelist counter  \
                    location2.append(values_on_line[5])
                    max_wind.append(values_on_line[6])
                    extent1.append(values_on_line[-4])
                    extent2.append(values_on_line[-3])
                    extent3.append(values_on_line[-2])
                    extent4.append(values_on_line[-1])
                    i += 1
        ID_list.append(values_on_line[0])
        disCalculate(location1, location2)
        SpeedCalculate(location1, location2, date, time)
        StormEnergy(max_wind, date, time)
        HUArea(extent1, extent2, extent3, extent4)
        data_list.append(list(line_list))
        putTable()
    print(
            "\n\n******************************************************\n=======================SUMMARY=======================\n******************************************************\n")

########## RUN FUNCTIONS ############
main()
top10_prop()
top10_TRSE()
top10_area()