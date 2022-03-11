#importing the needed module
from tkinter import *

def go_home():
    title.place(relx = 0.5, y = 80, anchor = CENTER)
    create_button.place(relx = 0.5, y = 140, anchor = CENTER)
    reminders_button.place(relx = 0.5, y = 180, anchor = CENTER)
    about_button.place(relx = 0.5, y = 220, anchor = CENTER)

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
    page = [title]
    page_and_home = [page, True]
    back_button(page_and_home)

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
main.geometry("500x400")
main.title("Reminder Program")

#home page
title = Label(main, text = "The Reminders App", font = (40))
create_button = Button(main, text = "Create a Reminder", command = create_page)
reminders_button = Button(main, text = "Reminders", command = reminders_page)
about_button = Button(main, text = "About", command = about_page)
C = Canvas(main, bg ="blue", height = 50, width = 50)
C.place(relx = 0.15, y = 350, anchor = CENTER)

#############################remmeber to this below when adding new things######################################################
home_page = [title, create_button, reminders_button, about_button]

go_home()

#show window

main.mainloop()

'''
#creating an entry box
entry_box = Entry(main)
canvas.create_window(200, 50, window=entry_box)

'''
