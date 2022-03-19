#importing the needed module and file
from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import *
from reminder_subroutines import read_file

def go_home():
    #positioning the items on the 'home page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    create_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    reminders_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    about_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    #creating the button cover and positioning it
    #the button cover covers the 'back' button when the user is on the home screen
    button_cover = Canvas(main, bg ="#EFF1F0", height = 50, width = 50, highlightthickness = 0)
    button_cover.place(relx = 0.15, rely = 0.85, anchor = CENTER)

def leave_page(page_and_home):
    #the elements of the page that is being left have been passed in along with the boolean value that expresses whether we are returning to the home page
    page = page_and_home[0]
    #runs a loop to remove the position of each page element
    for i in range(0, len(page)):
        page[i].place_forget()

    #checks whether page_and_home includes elements that have been positioned with the 'pack' method
    if len(page_and_home) == 2:
        #sets the index containing the name of the page we are returning to to 1
        j = 1
    else:
        #removes the position of the page elements that have been positioned with the 'pack' method
        for i in range(0, len(page_and_home[1])):
            page_and_home[1][i].pack_forget()
        #sets the index containing the name of the page we are returning to to 2
        j = 2

    #checks whether we are returning to the home page or the reminders page. Then runs the code for positioning the items on the page we are returning to
    if page_and_home[j] == "home":
        go_home()
    elif page_and_home[j] == "reminders":
        reminders_page()
      
def back_button(page_and_home):
    #creates the 'back' button
    back = Button(main, text = "<---", command = lambda: leave_page(page_and_home))
    back.place(relx = 0.15, rely = 0.85, anchor = CENTER)

def create_page():
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the string determines whether we are returning to a page and if so, which page
    page_and_home = [home_page, "not returning"]
    leave_page(page_and_home)
    title = Label(main, text = "Create a Reminder", font = (40))
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)

    #creating the items on the 'Create a Reminder' page
    date = Label(main, text = "Date: ")
    title_message = Label(main, text = "Title: ")
    message = Label(main, text = "Message: ")
    date_box = Entry(main)
    title_message_box = Entry(main, width = 40)
    message_box = Text(main, width = 30, height = 5)

    #positioning the items on the 'Create a Reminder' page
    date.place(relx = 0.3, rely = 0.38, anchor = CENTER)
    title_message.place(relx = 0.3, rely = 0.48, anchor = CENTER)
    message.place(relx = 0.3, rely = 0.575, anchor = CENTER)   
    date_box.place(relx = 0.6, rely = 0.38, anchor = E)
    title_message_box.place(relx = 0.6, rely = 0.48, anchor = CENTER)
    message_box.place(relx = 0.6, rely = 0.555, anchor = N)

    #storing the entry and text boxes in the list 'reminder' and creating and positioning the 'save' button
    reminder = [date_box, title_message_box, message_box]
    save = Button(main, text = "Save", command = lambda: save_reminder(reminder))
    save.place(relx = 0.6, rely = 0.85, anchor = CENTER)

    #list containing all of the items on the about page
    page = [title, date_box, title_message_box, message_box, date, title_message, message, save]

    #setting 'page_and_home' to the list of items and setting the string to "home" (as we want the button that will be created to leave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, "home"]
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
    #the string determines whether we are returning to a page and if so, which page
    page_and_home = [home_page, "not returning"]
    leave_page(page_and_home)

    #creating the items on the 'Reminders' page
    title = Label(main, text = "Reminders", font = (40))
    today_reminders = Button(main, text = "Today's Reminders", command = lambda: today_reminders_page(page))
    all_reminders = Button(main, text = "All Reminders", command = lambda: all_reminders_page(page))

    #positioning the items on the 'Reminders' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    today_reminders.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    all_reminders.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    #list containing all of the items on the about page
    page = [title, today_reminders, all_reminders]

    #setting 'page_and_home' to the list of items and setting the string to "home" (as we want the button that will be created to leave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, "home"]
    back_button(page_and_home)

def onselect(event, other_lists):
    # Note here that Tkinter passes an event object to onselect()
    for j in range (0, len(other_lists)):
        other_lists[j].selection_clear(0, END)
    widget = event.widget
    selected = widget.curselection()
    for i in range (0, len(selected)):
        for j in range (0, len(other_lists)):
            other_lists[j].select_set(selected[i])

def today_reminders_page(page):
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the string determines whether we are returning to a page and if so, which page
    page_and_home = [page, "not returning"]
    leave_page(page_and_home)

    #creating the items on the 'Today's Reminders' page
    title = Label(main, text = "Today's Reminders", font = (40))
    #scroll_bar = Scrollbar(main, orient = VERTICAL, height = 200)

    #positioning the items on the 'Today's Reminders' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)


    def scroll(x,y):
        list_title.yview(x,y)
        list_message.yview(x,y)



    frame = Frame(main, bg = "grey", bd = 10)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    scroll_bar = Scrollbar(frame)


    lines = read_file("Today_Reminders.txt")
    list_title = Listbox(frame, height = 5, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_message = Listbox(frame, height = 5, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False) 
    for line in range(0, len(lines)):
        list_title.insert(END, lines[line][1])
        list_message.insert(END, lines[line][2])
    

    top = "Title                                 Message                            "
    label = Label(frame, text = top, bg = "#EFF1F0")
    label.pack(side = TOP, anchor = NW, fill = BOTH)



    list_title.pack(side = LEFT)
    list_message.pack(side = LEFT)
    scroll_bar.config(command = scroll)
    scroll_bar.pack(side = RIGHT, fill = BOTH)

    list_title.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_message]))
    list_message.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_title]))


    #two lists containing all of the items on the about page
    #the first list contains the items that have been positioned using the 'place' method
    #the second list contains the items that have been positioned using the 'pack' method
    page = [title, frame]
    page_pack = [list_title, list_message, scroll_bar]

    #setting 'page_and_home' to the list of items and setting the string to "reminders" (as we want the button that will be created to leave this page and bring us back to the 'Reminders' page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, page_pack, "reminders"]
    back_button(page_and_home)

def all_reminders_page(page):
   #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the boolean determines whether the page we are moving to is a home page
    page_and_home = [page, False]
    leave_page(page_and_home)

    #creating the items on the 'All Reminders' page
    title = Label(main, text = "All Reminders", font = (40))

    #positioning the items on the 'Today's Reminders' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)

   

    frame = Frame(main, bg = "grey", bd = 10)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    scroll_bar = Scrollbar(frame)

    lines = read_file("Reminders.txt")
    list_date = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_title = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_message = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    for line in range(0, len(lines)):
        list_date.insert(END, lines[line][0])
        list_title.insert(END, lines[line][1])
        list_message.insert(END, lines[line][2])
    

    def scroll(x,y):
        list_date.yview(x,y)
        list_title.yview(x,y)
        list_message.yview(x,y)


    top = "Date                               Title                                 Message                             "
    label = Label(frame, text = top, bg = "#EFF1F0")
    label.pack(side = TOP, anchor = NW, fill = BOTH)


    list_date.pack(side = LEFT)
    list_title.pack(side = LEFT)
    list_message.pack(side = LEFT)
    scroll_bar.config(command = scroll)
    scroll_bar.pack(side = RIGHT, fill = BOTH)

    list_date.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_title, list_message]))
    list_title.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_date, list_message]))
    list_message.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_date, list_title]))

    #two lists containing all of the items on the about page
    #the first list contains the items that have been positioned using the 'place' method
    #the second list contains the items that have been positioned using the 'pack' method
    page = [title, frame]
    page_pack = [list_date, list_title, list_message, scroll_bar]

    #setting 'page_and_home' to the list of items and setting the string to "reminders" (as we want the button that will be created to leave this page and bring us back to the 'Reminders' page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, page_pack, "reminders"]
    back_button(page_and_home)

def about_page():
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the string determines whether we are returning to a page and if so, which page
    page_and_home = [home_page, "not returning"]
    leave_page(page_and_home)

    #creating the items on the 'About' page
    title = Label(main, text = "About", font = (40))

    #positioning the items on the 'About' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)

    #list containing all of the items on the about page
    page = [title]

    #setting 'page_and_home' to the list of items and setting the string to "home" (as we want the button that will be created to leave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, "home"]
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
button_cover = Canvas(main, bg = "#EFF1F0", highlightthickness = 0, height = 50, width = 50)

#list containing all the items on the home page
home_page = [title, create_button, reminders_button, about_button]

#calling go_home() to set up and position the items
go_home()

#show window
main.mainloop()