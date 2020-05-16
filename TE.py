from  tkinter import *
from  tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from  tkinter.filedialog import askopenfilename
import os

from tkinter.filedialog import askdirectory
import tkinter as GUI
import codecs



#Window's Creation
first = Tk()

#Variables
filename = ''

#Window's title
first.title(filename)




#Functions

#Function for 'event 1'

def pop_up(event):
    Editmenu.tk_popup(event.x_root, event.y_root)


#New file function
def newf():
    filename = "Not Set"
    first.title(filename+" -Text Editor")
    T.delete('0.0', END)



#Open function
def open():
    global filename
    filename = askopenfilename(title = "Select file")
    test, test2 = os.path.splitext(os.path.basename(filename))
    print(test)
    print(test2)
    first.title(test+" -Text Editor")
    with codecs.open(filename, 'r') as f:
        t= f.read()
    T.delete('0.0', END)
    T.insert('0.0',t)

#Save as Function
def saveas():
   f = asksaveasfile(mode = 'w', defaultextension = ".txt")
   t = T.get('0.0', END)
   f.write(t)

#Save function
def save():
    t = T.get('0.0', END)

    if filename == '':
        saveas()
    else:
        with codecs.open(filename, 'w') as f:
            f.write(t)








def cleartext():
    T.delete('1.0', END)



#Widgets

T = Text(first)


#Menubar

#Creating the main menu bar
Menubar = Menu(first)

#Ading members tothe 'Filemenu'
Filemenu = Menu(Menubar, tearoff = 0)
Filemenu.add_command(label = "New", command = newf)
Filemenu.add_command(label = "Open", command = open)
Filemenu.add_command(label = "Save", command = save)
Filemenu.add_command(label = "Save as...", command = saveas)
Filemenu.add_command(label = "Exit", command = first.quit)

#Creating a Submenu 'File' to the main menu 'Menu bar' and assigning the 'Filemenu' to it
Menubar.add_cascade(label = "File", menu = Filemenu)

Editmenu = Menu(Menubar, tearoff = 0)

#Ading members tothe 'Editmenu'
Editmenu.add_command(label = "Copy",  command =  lambda:  T.event_generate("<<Copy>>"))
Editmenu.add_command(label = "Cut",   command =  lambda:   T.event_generate("<<Cut>>"))
Editmenu.add_command(label = "Paste", command =  lambda: T.event_generate("<<Paste>>"))
Editmenu.add_command(label = "Undo",  command =  lambda: T.event_generate("<<Undo>>"))
Editmenu.add_command(label = "Redo",  command =  lambda: T.event_generate("<<Redo>>"))

#Creating a Submenu 'Edit' to the main menu 'Menu bar' and assigning the 'Editmenu' to it
Menubar.add_cascade(label = "Edit", menu = Editmenu)

Helpmenu = Menu(Menubar, tearoff = 0)

#Ading members tothe 'Helpmenu'

Menubar.add_cascade(label = "Help", menu = Helpmenu)





#Events

#Event 1
T.bind("<Button-3>", pop_up)

#Positioning

T.place(x = 0, y = 0, height = 500, width = 500)



#Configurations
first.config(bg = "#e2e2e2", height = 500, width = 500, menu = Menubar)




first.mainloop()
