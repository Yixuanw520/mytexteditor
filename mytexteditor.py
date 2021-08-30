"""
[Final Quiz]
Date: 2021-08-23
Design at least 3 major features for a text editor
Do a quick research on the Internet if you need some ideas or references
Save your project as 'mytexteditor'
Share your project to github
Post your URL of your remote git repository to SLACK
Due date: 2021-08-31
Hints:
Self-study on font family, size, weight of text widget in Tkinter
"""

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from tkinter import font

def newfile():
    messagebox.showinfo("File", "New File")

def font():
    messagebox.showinfo("Font", "")

def countlines(event):
    (line, c) = map(int, event.widget.index("end-1c").split("."))
    # print(line, c)
    status_text1 = f"Status: INSERT MODE  ROW:{line},COL:{c}"
    var.set(status_text1)


def cut():
    str_status = var.get()
    status_text2 = ' '*5+"cut."
    var.set(status_text1+status_text2)
    status_text2 = ''

def copy():
    str_status = var.get()
    status_text2 = ' '*5+"copy."
    var.set(status_text1 + status_text2)
    status_text2 = ''


def paste():
    str_status = var.get()
    status_text2 = ' '*5+"paste."
    var.set(status_text1 + status_text2)
    status_text2 = ''

def font_type():
    str_status = var.get()
    status_text2 = ' '*5+"Arial."
    var.set(status_text1 + status_text2)
    status_text2 = ''

def plus():
    str_status = var.get()
    status_text2 = ' '*5+"+ 1."
    var.set(status_text1 + status_text2)
    status_text2 = ''

def moin():
    str_status = var.get()
    status_text2 = ' '*5+"- 1."
    var.set(status_text1 + status_text2)
    status_text2 = ''

root = Tk()
root.title("Athensoft Python Course | Menu")
root.geometry("640x480+300+300")

# main bar
menubar = Menu(root)

# main bar item
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)

# Level 2 menu option
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
filemenu.add_command(label="Exit", command=root.destroy)

# second bar item
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=filemenu)

# Level 2 menu option
filemenu.add_command(label="cut")
filemenu.add_command(label="copy")
filemenu.add_command(label="paste")

# third bar item
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=filemenu)

# Level 2 menu option
filemenu.add_command(label="web")
filemenu.add_command(label="search")

# toolbar frame
frame_toolbar = Frame(root, height=30)
frame_toolbar.pack(anchor=W)

btn1 = Button(frame_toolbar, text="cut", command=cut)
btn1.pack(side=LEFT)

btn2 = Button(frame_toolbar, text="copy", command=copy)
btn2.pack(side=LEFT)

btn3 = Button(frame_toolbar, text="paste", command=paste)
btn3.pack(side=LEFT)

size = 12  # default size
size_var = IntVar()
size_var.set(size)
size_label = Label(frame_toolbar, textvariable=size_var)  # font size label
add_size = Button(frame_toolbar, text="+", width=7, font=(None, 8), command=plus)  # add size button
sub_size = Button(frame_toolbar, text="-", width=7, font=(None, 8), command=moin)  # sub size button
add_size.pack(side=LEFT, padx=5)  # first pack + button
size_label.pack(side=LEFT, padx=5)  # second pack label showing current size
sub_size.pack(side=LEFT, padx=5)  # finally pack - button

btn3 = Button(frame_toolbar, text="Arial", command=font_type)
btn3.pack(side=LEFT, padx=5)

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

text.bind("<KeyRelease>", countlines)

# separator
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# status bar
var = StringVar()

# for mode and position
status_text1= "Status: INSERT MODE"

statusbar = Label(root, textvariable=var)
statusbar.pack(anchor=S + W)
var.set(status_text1)

# # for function button clicked
# status_text2 = ""

root.config(menu=menubar)

root.mainloop()

