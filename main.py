#importing the needed module
from tkinter import *

def go_home():
    #positioning the items on the 'home page
    title.place(relx = 0.5, y = 80, anchor = CENTER)
    create_button.place(relx = 0.5, y = 140, anchor = CENTER)
    reminders_button.place(relx = 0.5, y = 180, anchor = CENTER)
    about_button.place(relx = 0.5, y = 220, anchor = CENTER)

    #creating the button cover and positioning it
    #the button cover covers the 'back' button when the user is on the home screen
    button_cover = Canvas(main, bg ="#EFF1F0", height = 50, width = 50, highlightthickness = 0)
    button_cover.place(relx = 0.15, y = 350, anchor = CENTER)

def leave_page(page_and_home):
    #the elements of the page that is being left have been passed in along with the boolean value that expresses whether we are returning to the home page
    page = page_and_home[0]
    #runs a loop to remove the position of each page element
    for i in range(0, len(page)):
        page[i].place_forget()
    #checks whether we are returning to the home page. If yes, then runs the code for positioning the home page elements
    if page_and_home[1] == True:
        go_home()
      
def back_button(page_and_home):
    #creates the 'back' button
    back = Button(main, text = "<---", command = lambda: leave_page(page_and_home))
    back.place(relx = 0.15, y = 350, anchor = CENTER)

def create_page():
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the boolean determines whether the page we are moving to is a home page
    page_and_home = [home_page, False]
    leave_page(page_and_home)
    title = Label(main, text="Create a Reminder", font=(40))
    title.place(relx = 0.5, y = 80, anchor = CENTER)

    #creating the items on the 'Create a Reminder' page
    date = Label(main, text="Date: ")
    title_message = Label(main, text= "Title: ")
    message = Label(main, text="Message: ")
    date_box = Entry(main)
    title_message_box = Entry(main, width = 40)
    message_box = Text(main, width = 30, height = 5)

    #positioning the items on the 'Create a Reminder' page
    date.place(relx = 0.3, y = 140, anchor = CENTER)
    title_message.place(relx = 0.3, y = 180, anchor = CENTER)
    message.place(relx = 0.3, y = 220, anchor = CENTER)   
    date_box.place(relx = 0.60, y = 140, anchor = E)
    title_message_box.place(relx = 0.6, y = 180, anchor = CENTER)
    message_box.place(relx = 0.6, y = 210, anchor = N)

    #storing the entry and text boxes in the list 'reminder' and creating and positioning the 'save' button
    reminder = [date_box, title_message_box, message_box]
    save = Button(main, text = "Save", command = lambda: save_reminder(reminder))
    save.place(relx = 0.6, y = 350, anchor = CENTER)

    #list containing all of the items on the about page
    page = [title, date_box, title_message_box, message_box, date, title_message, message, save]

    #setting 'page_and_home' to the list of items and setting the boolean value to True (as we want the button that will be created toleave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, True]
    back_button(page_and_home)
    
def save_reminder(reminder):
    #checking whether the date and title have been entered, if yes, the data can be saved
    if reminder[0].get() != '' and reminder[1].get() != '':
        #getting the information entered into the fields and storing it in variables
        date = reminder[0].get()
        title = reminder[1].get()
        message = reminder[2].get(1.0, "end-1c")

        #deleting the data from the fields
        reminder[0].delete(0, END)
        reminder[1].delete(0, END)
        reminder[2].delete(1.0, END)

        #joining together the information and appending it to the file "reminder.txt" (the file is created if not already existing)
        line = date + ", " + title + ", " + message + "\n"
        file = open("reminders.txt", "a+")
        file.write(line)
        file.close()

def reminders_page():
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the boolean determines whether the page we are moving to is a home page
    page_and_home = [home_page, False]
    leave_page(page_and_home)

    #creating the items on the 'Reminders' page
    title = Label(main, text ="Reminders", font = (40))

    #positioning the items on the 'Reminders' page
    title.place(relx = 0.5, y = 80, anchor = CENTER)

    #list containing all of the items on the about page
    page = [title]

    #setting 'page_and_home' to the list of items and setting the boolean value to True (as we want the button that will be created toleave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, True]
    back_button(page_and_home)

def about_page():
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the boolean determines whether the page we are moving to is a home page
    page_and_home = [home_page, False]
    leave_page(page_and_home)

    #creating the items on the 'About' page
    title = Label(main, text ="About", font = (40))

    #positioning the items on the 'About' page
    title.place(relx = 0.5, y = 80, anchor = CENTER)

    #list containing all of the items on the about page
    page = [title]

    #setting 'page_and_home' to the list of items and setting the boolean value to True (as we want the button that will be created toleave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, True]
    back_button(page_and_home)

#initialising the window, setting some properties and creating a canvas
main = Tk()
main.configure(bg = "#EFF1F0")
main.geometry("500x400")
main.title("Reminder Program")

#setting up the home page - creating the buttons and title
title = Label(main, text = "The Reminders App", font = (40))
create_button = Button(main, text = "Create a Reminder", command = create_page)
reminders_button = Button(main, text = "Reminders", command = reminders_page)
about_button = Button(main, text = "About", command = about_page)
button_cover = Canvas(main, bg ="#EFF1F0", highlightthickness = 0, height = 50, width = 50)

#list containing all the items on the home page
home_page = [title, create_button, reminders_button, about_button]

#calling go_home() to set up and position the items
go_home()

#show window
main.mainloop()