###########################################################################################################
# IS 590 PR ###############################################################################################
# 29/01/19 ################################################################################################
# Spring 2019 ###############################################################################4#############
# HW2 #####################################################################################################
# Worawich Chaiyakunapruk [wchaiy2] #######################################################################
# Yao Xiao [yaoxiao9] #####################################################################################
# We work together and discuss along the way ##############################################################
###################### THIS CODE READ, STORE DATA, AND PROCESS THEM LINE BY LINE ##########################


i = 1  # line counter
j = 1  # temporary line counter >>>> use as Number of best track entries counter to catch up and a flag as we got data written down
# if the line is not header, leave j alone, only increase i. When i = j+ (amount data line of each storm) then it's the last time storm appear
l = 0  # landfall counter
n = 0  # storm counter
h = 0  # hurricane counter

date = list()
date_list = list()  # make the date list counter to list all the date of each storm
wind_speed = list()  # make the wind speed list counter to wind speed and hurricane level

pressure = list()  # make the pressure list counter to calculate pressure change
year_list = list()  # make the year list counter to list all the year of each storm
storm_yearly = list()  # make the storm counter per year
hurricane_yearly = list()  # make the hurricane counter per year

while True:
    select = input('Enter 1 for Atlantic, 2 for Pacific: ')
    if select is '1':
        filename = 'hurdat2-1851-2017-050118.txt'
        break
    if select is '2':
        filename = 'hurdat2-nepac-1949-2017-050418.txt'
        break
    else:
        print("WRONG INPUT, DO IT AGAIN!!!!!")
        continue

path = '/Users/xy/Downloads/' + filename

with open(path, 'r') as f:
    for line in f:  # looping read ONLY ONE line from the file
        line = line.replace(',\n', '')  # replace comma and new line with nothing (end of line)
        line = line.replace(' ', '')
        values_on_line = line.split(",")  # Split string at comma (,) into list of "words" which are number strings.

        if i == 2:  # First data line (first time it contains the year (yyyy))
            year = values_on_line[0][:4]  # Initiate a temporary year value to store the year (yyyy)

        ###################### IF LOOP FOR A HEADER #####################################
        if not (line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))):
            if i == j:  # When i=j it's the first header
                ID, name, nelement = values_on_line  # put value in line into variables
                nelement = int(nelement)  # make Number of best track entries into int
                print("Storm ID:", ID)
                if name != "UNNAMED":
                    print("Strom name:", name)
                else:
                    print("No storm name.")
                #                 print("number of element", nelement)
                j += 1  # Line counter when meet a header
                i += 1  # Line counter for the first line only

            ##################### THIS INDICATE LAST LINE OF EACH STORM ##############################
            if i == j + nelement:  # If i counter equal to j counter plus the element of each storm (which means we already got all data in that storm) then go into this loop
                print("Date range (yyyymmdd):", min(date_list), "-", max(date_list))
                print("Maximum sustained wind (in knots):", max(wind_speed), "occurred on (yyyymmdd):", date_list[
                    wind_speed.index(
                        max(wind_speed))])  # return index of maximum wind speed and use that as an index of the date
                print("Pressure change (millibars):", max(pressure) - min(pressure))
                if l != 0:
                    print("“Landfall” happened:", l, "times.")
                else:
                    print("No landfall happened.")
                l = 0  # reset landfall counter

                if int(max(wind_speed)) >= 64:  # if max wind speed is equal or more than 64 knots, it's a hurricane
                    h += 1  # increase hurricane counter

                ################################ DONE WITH ONE STORM, RESET VARIABLES FOR THE NEXT ONE ########################

                date_list.clear()  # reset the list counter since we are done with this storm
                wind_speed.clear()
                pressure.clear()

                ################################ NEXT STORM #########################################

                ID, name, nelement = values_on_line  # \
                nelement = int(nelement)  # \
                print("\nStorm ID:", ID)  # \
                if name != "UNNAMED":  # \ DO THE SAME WITH PREVIOUS IF LOOP
                    print("Strom name:", name)  # /
                else:  # /
                    print("No storm name.")  # /
                #                 print("number of element", nelement)         #/

                i += 1  # line counter for header
                j = i  # reset the j value to i (difference in i, j are the number of data line)
                n += 1  # counting as 1 storm

        ######################## IF LOOP WHEN IT'S NOT A HEADER (DATA LINE) #################################
        else:
            date_list.append(values_on_line[0])  # put the date into datelist counter  \
            wind_speed.append(
                values_on_line[6])  # add the wind speed into the list     >  These are each day (each line) of the data
            pressure.append(int(values_on_line[7]))  # add the pressure into the list      /

            if str(values_on_line[2]) == "L":  # If there's "L" flag, there's landfall
                l += 1  # Landfall counter +1

            i += 1  # line counter for data

            if year != values_on_line[0][:4]:  # if year counter isn't the same year
                year_list.append(year)  # record the year (yyyy) into the year list
                storm_yearly.append(n)  # record number of storm(s) into the storm list
                n = 0  # reset the number of storm counter
                hurricane_yearly.append(h)  # record number of hurricane(s) into the hurricane list
                h = 0  # reset the number of hurricane counter
                year = values_on_line[0][:4]  # set year counter to new year

######################### FOR THE LAST SET OF DATA, IT DIDN'T COMPLETE THE IF LOOP, SO PUT THEM HERE AGAIN #############################

print("Date range (yyyymmdd):", min(date_list), "-", max(date_list))
print("Maximum sustained wind (in knots):", max(wind_speed), "occurred on (yyyymmdd):", date_list[
    wind_speed.index(max(wind_speed))])  # return index of maximum wind speed and use that as an index of the date
print("Pressure change (millibars):", max(pressure) - min(pressure))
if l != 0:
    print("“Landfall” happened:", l, "times.")
else:
    print("No landfall happened.")
l = 0
year_list.append(year)
storm_yearly.append(n)
hurricane_yearly.append(h)
year = values_on_line[0][:4]

print(
    "\n\n******************************************************\n=======================SUMMARY=======================\n******************************************************\n")

for a in range(len(year_list)):
    print("Year ", year_list[a], " has ", storm_yearly[a], "storm(s) and ", hurricane_yearly[a], " hurricane(s)")
