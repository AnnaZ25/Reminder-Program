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

#main program

date = find_date()

#opening the reminders file in read mode
file = open("reminders.txt", "r")

#adding all the lines in the file to a list
lines = []
for line in file:
    sections = line.split(", ")
    lines.append(sections)
file.close()

#finding all the items to be removed in the list by comparing the date for each element with the current date
remove = []
for element in range(0, len(lines)):
    if lines[element][0] == date:
        #sending the desktop notification(s)
        notify(lines[element][1], lines[element][2])
        #appending the index numbers to be removed
        remove.append(element)
        #adding a delay of 10 seconds so that there is a delay between each notification
        time.sleep(10)

#removing the items that needed to be removed from the list
counter = 0
for i in range (0, len(remove)):
    lines.pop(remove[i]-counter)
    counter += 1

#opening the reminders file in write mode and writing the information in the list to the file
file = open("reminders.txt", "w")
for line in lines:
    file.write(", ".join(line))
file.close()