#importing needed modules
import time
from plyer import notification as n

#procedure that sends a desktop notification
def notify(ptitle, pmessage):
    n.notify(
        title = ptitle,
        message = pmessage,
        app_icon = None,
        timeout = 15,
        )

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
        day = raw_time[2]   

    # joining the date together
    date = day + "/" + str(month) + "/" + raw_time[4]

    return date

#function that reads the file that is passed in and stores each line in a two-dimensional list 
def read_file(file):
    #opening the file in read mode
    file = open(file, "r")

    #adding all the lines in the file to a list
    lines = []
    for line in file:
        sections = line.split(", ")
        lines.append(sections)
    file.close()

    return lines
