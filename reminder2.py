import os
from plyer import notification as n

folder = "Reminder"
#creating folder "Reminder" if not found
if not os.path.exists(folder):
    os.makedirs(folder)

#procedure that sends a desktop notification
def notify(ptitle, pmessage):
    n.notify(
        title = ptitle,
        message = pmessage,
        app_icon = None,
        timeout = 15,
        )
'''
print("Hello, welcome to the reminder program.")
title = input("Please enter the text you would like to display as the title; ")
message = input("Please enter the message you would like to display underneath the title: ")
'''
#notify(title, message)


date = 'fdfks'
title = "dskfgjsd"
message = "fhjkghd"

#joining together the information and appending it to the file "reminder.txt" (the file is created if not already existing)
line = date + ", " + title + ", " + message + "\n"
file = open(folder + "\\" + "reminder.txt", "a+")
file.write(line)
file.close()

