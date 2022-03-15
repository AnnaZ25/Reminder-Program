#importing needed modules and file
import time
from reminder_subroutines import find_date
from reminder_subroutines import read_file
from reminder_subroutines import notify
from os.path import exists

def write_file():
    counter = 0 
    
    file = open("Today_Reminders.txt", "w")
    for i in range (0, len(remove)):
        file.write(", ".join(lines.pop(remove[i]-counter)))
        counter += 1
    file.close()

#main program

date = find_date()
lines = read_file("Reminders.txt")

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

if exists("C:\\Users\\dorot\\Documents\\GitHub\\Reminder\\Today_Reminders.txt") == True:
    lines_in = read_file("Today_Reminders.txt")
    if lines_in != []:
        if lines_in[0][0] != date:
            write_file()
    else:
        write_file()
else:
    write_file()




#opening the reminders file in write mode and writing the information in the list to the file
file = open("Reminders.txt", "w")
for line in lines:
    file.write(", ".join(line))
file.close()