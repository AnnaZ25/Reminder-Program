#importing needed modules
import time

#function that finds the current date and time
def find_date():
    #list of months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #finding the current time and splitting it into sections
    raw_time = time.asctime(time.localtime()).split()

    #finding the month number by searching the array and finding the index + 1 
    found_month = False
    month = 0
    while not found_month:
        if raw_time[1] == months[month]:
            found_month = True
        month += 1

    #adding a 0 to the front of month numbers that are not two digits long
    if len(str(month)) == 1:
        month = "0" + str(month)

    #adding a 0 to the front of day numbers that are not two digits long
    if len(raw_time[2]) == 1:
        day = "0" + raw_time[2]
    else:
        day = raw_time   

    # joining the date together
    date = day + "/" + month + "/" + raw_time[4]

    return date

#main program
date = find_date()


#notify(title, message)