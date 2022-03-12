#importing the needed module
from tkinter import *

def go_home():
    title.place(relx = 0.5, y = 80, anchor = CENTER)
    create_button.place(relx = 0.5, y = 140, anchor = CENTER)
    reminders_button.place(relx = 0.5, y = 180, anchor = CENTER)
    about_button.place(relx = 0.5, y = 220, anchor = CENTER)
    button_cover = Canvas(main, bg ="#EFF1F0", height = 50, width = 50, highlightthickness = 0)
    button_cover.place(relx = 0.15, y = 350, anchor = CENTER)

def leave_page(page_and_home):
    page = page_and_home[0]
    for i in range(0, len(page)):
        page[i].place_forget()
    if page_and_home[1] == True:
        go_home()
      
def back_button(page_and_home):
    back = Button(main, text = "<---", command = lambda: leave_page(page_and_home))
    back.place(relx = 0.15, y = 350, anchor = CENTER)

def create_page():
    page_and_home = [home_page, False]
    leave_page(page_and_home)
    title = Label(main, text="Create a Reminder", font=(40))
    title.place(relx = 0.5, y = 80, anchor = CENTER)

    date = Label(main, text="Date: ")
    title_message = Label(main, text= "Title: ")
    message = Label(main, text="Message: ")
    date_box = Entry(main)
    title_message_box = Entry(main, width = 40)
    message_box = Text(main, width = 30, height = 5)

    date.place(relx = 0.3, y = 140, anchor = CENTER)
    title_message.place(relx = 0.3, y = 180, anchor = CENTER)
    message.place(relx = 0.3, y = 220, anchor = CENTER)   
    date_box.place(relx = 0.60, y = 140, anchor = E)
    title_message_box.place(relx = 0.6, y = 180, anchor = CENTER)
    message_box.place(relx = 0.6, y = 210, anchor = N)

    reminder = [date_box, title_message_box, message_box]
    save = Button(main, text = "Save", command = lambda: save_reminder(reminder))
    save.place(relx = 0.6, y = 350, anchor = CENTER)

    page = [title, date_box, title_message_box, message_box, date, title_message, message, save]
    page_and_home = [page, True]
    back_button(page_and_home)
    
def save_reminder(reminder):
    for i in range (0, len(reminder)-1):
        print(reminder[i].get())
    print(reminder[2].get(1.0, "end-1c"))

def reminders_page():
    page_and_home = [home_page, False]
    leave_page(page_and_home)
    title = Label(main, text ="Reminders", font = (40))
    title.place(relx = 0.5, y = 80, anchor = CENTER)
    page = [title]
    page_and_home = [page, True]
    back_button(page_and_home)

def about_page():
    page_and_home = [home_page, False]
    leave_page(page_and_home)
    title = Label(main, text ="About", font = (40))
    title.place(relx = 0.5, y = 80, anchor = CENTER)
    page = [title]
    page_and_home = [page, True]
    back_button(page_and_home)

#initialising the window, setting some properties and creating a canvas
main = Tk()
main.configure(bg = "#EFF1F0")
main.geometry("500x400")
main.title("Reminder Program")

#home page
title = Label(main, text = "The Reminders App", font = (40))
create_button = Button(main, text = "Create a Reminder", command = create_page)
reminders_button = Button(main, text = "Reminders", command = reminders_page)
about_button = Button(main, text = "About", command = about_page)
button_cover = Canvas(main, bg ="#EFF1F0", highlightthickness = 0, height = 50, width = 50)


#############################remmeber to this below when adding new things######################################################
home_page = [title, create_button, reminders_button, about_button]

go_home()

#show window

main.mainloop()