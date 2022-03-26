#importing the needed module and file
from tkinter import *
from reminder_subroutines import read_file
from PIL import ImageTk, Image  

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
    #clearing already selected items from the lists stored at each index of the 'other_lists' list
    for j in range (0, len(other_lists)):
        other_lists[j].selection_clear(0, END)
    #finding the items selected in the listbox that the item was selected in
    widget = event.widget
    selected = widget.curselection()
    #selecting all items in all listboxes that are in the same row 
    for i in range (0, len(selected)):
        for j in range (0, len(other_lists)):
            other_lists[j].select_set(selected[i])

def list_boxes_add(list_boxes, file):
    #inserting rows of data to the listboxes created

    #reading the file passed into the subroutine
    lines = read_file(file)

    #inserting the data from the file into the right columns of the listboxes
    for line in range(0, len(lines)):
        #checking whether we are adding to two or three listboxes 
        if len(list_boxes) == 3:
            list_boxes[0].insert(END, lines[line][0])
            list_boxes[1].insert(END, lines[line][1])
            list_boxes[2].insert(END, lines[line][2])
        else:
            list_boxes[0].insert(END, lines[line][1])
            list_boxes[1].insert(END, lines[line][2])
    
    #returning the listboxes
    return list_boxes

def today_reminders_page(page):
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the string determines whether we are returning to a page and if so, which page
    page_and_home = [page, "not returning"]
    leave_page(page_and_home)

    #procedure that scrolls both of the listboxes to be created at the same time
    def scroll(x,y):
        list_title.yview(x,y)
        list_message.yview(x,y)

    #creating the items on the 'Today's Reminders' page
    title = Label(main, text = "Today's Reminders", font = (40))
    frame = Frame(main, bg = "grey", bd = 10)
    scroll_bar = Scrollbar(frame)
    scroll_bar.config(command = scroll)
    top_label = "Title                                 Message                            "
    label = Label(frame, text = top_label, bg = "#EFF1F0")

    #creating the listboxes
    #setting the selection mode to allow multiple selections; configuring other settings of the listboxes.
    list_title = Listbox(frame, height = 5, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_message = Listbox(frame, height = 5, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False) 
    list_boxes = [list_title, list_message]
    list_boxes = list_boxes_add(list_boxes, "Today_Reminders.txt")

    #creating the delete button and linking it to the procedure delete_rows
    delete = Button(main, text = "Delete", command = lambda: delete_rows([list_boxes, "Today_Reminders.txt"]))

    #positioning the items on the 'Today's Reminders' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    label.pack(side = TOP, anchor = NW, fill = BOTH)
    list_boxes_pack(list_boxes)
    scroll_bar.pack(side = RIGHT, fill = BOTH)
    delete.place(relx = 0.5, rely = 0.85, anchor = CENTER)

    #the procedure 'onselect' is run when an item is selected (or deselected) from either list.
    list_title.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_message]))
    list_message.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_title]))

    #two lists containing all of the items on the about page
    #the first list contains the items that have been positioned using the 'place' method
    #the second list contains the items that have been positioned using the 'pack' method
    page = [title, frame, delete]
    page_pack = [list_title, list_message, scroll_bar]

    #setting 'page_and_home' to the list of items and setting the string to "reminders" (as we want the button that will be created to leave this page and bring us back to the 'Reminders' page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, page_pack, "reminders"]
    back_button(page_and_home)

def list_boxes_pack(list_boxes):
    #packing all the listboxes in 'list_boxes'
    for i in range (0, len(list_boxes)):
        list_boxes[i].pack(side = LEFT)

def all_reminders_page(page):
    #calling leave page to leave the home page
    #using the variable 'page_and_home' to pass in the list of home page elements
    #the boolean determines whether the page we are moving to is a home page
    page_and_home = [page, False]
    leave_page(page_and_home)

    #procedure that scrolls both of the listboxes to be created at the same time
    def scroll(x,y):
        list_date.yview(x,y)
        list_title.yview(x,y)
        list_message.yview(x,y)

    #creating the items on the 'All Reminders' page
    title = Label(main, text = "All Reminders", font = (40))
    frame = Frame(main, bg = "grey", bd = 10)
    scroll_bar = Scrollbar(frame)
    scroll_bar.config(command = scroll)
    top_label = "Date                               Title                                 Message                             "
    label = Label(frame, text = top_label, bg = "#EFF1F0")

    #creating the listboxes
    #setting the selection mode to allow multiple selections; configuring other settings of the listboxes.
    list_date = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_title = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_message = Listbox(frame, height = 7, yscrollcommand = scroll_bar.set, bd = 0, highlightthickness = 0, selectmode = "multiple", exportselection = False)
    list_boxes = [list_date, list_title, list_message]
    list_boxes = list_boxes_add(list_boxes, "Reminders.txt")
    
    #creating the delete button and linking it to the procedure delete_rows
    delete = Button(main, text = "Delete", command = lambda: delete_rows([list_boxes, "Reminders.txt"]))

    #positioning the items on the 'All Reminders' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    label.pack(side = TOP, anchor = NW, fill = BOTH)
    list_boxes_pack(list_boxes)
    scroll_bar.pack(side = RIGHT, fill = BOTH)
    delete.place(relx = 0.5, rely = 0.85, anchor = CENTER)

    #the procedure 'onselect' is run when an item is selected (or deselected) from either list.
    list_date.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_title, list_message]))
    list_title.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_date, list_message]))
    list_message.bind("<<ListboxSelect>>", lambda event: onselect(event, [list_date, list_title]))

    #two lists containing all of the items on the about page
    #the first list contains the items that have been positioned using the 'place' method
    #the second list contains the items that have been positioned using the 'pack' method
    page = [title, frame, delete]
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
    frame = Frame(main, bg = "grey", bd = 10)
    frame_paragraphs = Frame(frame)

    #creating the paragraphs to be displayed inside the frame 'frame_paragraphs'
    about_1 = "The Reminder App is a program which allows you to create reminders for specific dates."
    about_2 = "With the Reminder App you can set reminders for specific dates and be reminded on the day as soon as you log in! You can also look at all and delete any reminders you have set for the future that you don't need anymore."
    about_box1 = Message(frame_paragraphs, text = about_1, width = 200)
    about_box2 = Message(frame_paragraphs, text = about_2, width = 200)  

    #positioning the items on the 'About' page
    title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    frame_paragraphs.pack(side = RIGHT)
    about_box1.pack(anchor = W)
    about_box2.pack(anchor = W)
    
    #positioning the 'About' page image
    Label(frame, image = img).pack(side = LEFT)

    #list containing all of the items on the about page
    page = [title, frame]
    page_pack = [frame_paragraphs, about_box1, about_box2] #pass into subroutine #########################################################################################

    #setting 'page_and_home' to the list of items and setting the string to "home" (as we want the button that will be created to leave this page and bring us back to the home page)
    #passing this into 'back_button' which creates and positions the button
    page_and_home = [page, page_pack, "home"]
    back_button(page_and_home)

def delete_rows(list_and_file):
    #deleting the rows from the lists and updating the 'Reminders.txt' or 'Today_Reminders.txt' file

    #finding the selected item indexes
    selected = list_and_file[0][0].curselection()

    #adding the selected items to a list called items
    items = []
    lists = list_and_file[0]
    for i in range (0, len(selected)):
        item_selected = selected[i]
        #checking whether there are two or three listboxes passed into the subroutine to resolve indexing problems
        if len(lists) == 3:
            items.append([lists[0].get(item_selected), lists[1].get(item_selected), lists[2].get(item_selected)])
        else:
            items.append([lists[0].get(item_selected), lists[1].get(item_selected)])

    #reading the file and storing all its lines in the list 'lines'
    lines = read_file(list_and_file[1])

    #deleting the items that should be deleted from the lists.
    for i in range (0, len(items)):
        for j in range (0, len(lines)):
            #checking whether there are two or three listboxes passed into the subroutine to resolve indexing problems
            if len(lists) == 3:
                if (lists[0].get(j) == items[i][0]) and (lists[1].get(j) == items[i][1]) and (lists[2].get(j) == items[i][2]): 
                    lists[0].delete(j)
                    lists[1].delete(j)
                    lists[2].delete(j)
            else:
                if (lists[0].get(j) == items[i][0]) and (lists[1].get(j) == items[i][1]): 
                    lists[0].delete(j)
                    lists[1].delete(j)

    #adding all of the items that need removing from the text file passed into the subroutine
    remove = []
    for i in range (0, len(lines)):
        for j in range (0, len(items)):
            #checking whether there are two or three listboxes passed into the subroutine to resolve indexing problems
            if len(lists) == 3:
                if (lines[i][0] == items[j][0]) and (lines[i][1] == items[j][1]) and (lines[i][2] == items[j][2]):
                    remove.append(i)
            else:
                if (lines[i][1] == items[j][0]) and (lines[i][2] == items[j][1]):
                    remove.append(i)

    #removing the indexes present in the list 'remove'
    counter = 0 
    for i in range (0, len(remove)):
        lines.pop(remove[i]-counter)
        counter += 1

    #writing the data in 'lines' to the text file passed into the procedure
    file = open(list_and_file[1], "w")
    for i in range (0, len(lines)):
        file.write(", ".join(lines[i]))
    file.close()

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

#opening and creating the 'About' page image
img = Image.open("about_page_image.png")
img = img.resize((115, 162))
img = ImageTk.PhotoImage(img)

#show window
main.mainloop()