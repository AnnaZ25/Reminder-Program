from plyer import notification as n

#procedure that sends a desktop notification
def notify(ptitle, pmessage):
    n.notify(
        title = ptitle,
        message = pmessage,
        app_icon = None,
        timeout = 15,
        )

#main program 

#recieving userinput information
print("Hello, welcome to the Reminder program.")
title = input("Please enter the text you would like to display as the title: ")
message = input("Please enter the message you would like to display underneath the title: ")
date = input("Please enter the date you would like to be notified (in the format xx/xx/xxxx): ")

#joining together the information and appending it to the file "reminder.txt" (the file is created if not already existing)
line = date + ", " + title + ", " + message + "\n"
file = open("Reminders.txt", "a+")
file.write(line)
file.close()