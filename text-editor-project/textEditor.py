import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def changeColor():
    color = colorchooser.askcolor()
    textArea.configure(fg=color[1])

def changeFont(*args):
    textArea.config(font=(fontName.get(), fontSize.get()))

def newFile():
    window.title("Untitled")
    textArea.delete(1.0,END)

def openFile():
    file = askopenfilename(defaultextension=".txt",
                           file=[('All Files', '*.*'),
                                 ("Text Documents", '*.txt')])
    try:
        window.title(os.path.basename(file))
        textArea.delete(1.0, END)
        file = open(file, 'r')
        textArea.insert(1.0, file.read())

    except Exception:
        print("Couldn't Read File!")

    finally:
        file.close()

def saveFile():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                      defaultextension=".txt",
                                      filetypes=[('All Files', '*.*'),
                                                 ('Text Documents', '*.txt')])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')
            file.write(textArea.get(1.0, END))

        except Exception:
            print("Couldn't save the file")

        finally:
            file.close()


def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    aboutText = (
        "About\n\n"
        "A basic text editor built with Python's Tkinter library. "
        "It offers essential features for creating, editing, and saving text documents.\n\n"
        "Features:\n"
        "- Create New Files\n"
        "- Open Existing Files\n"
        "- Save Files\n\n"
        "Developer:\n"
        "Created by Jidhun Puthuppattu, your fellow coder.\n\n"
    )
    showinfo("About This Program", aboutText)

def quit():
    window.destroy()


window = Tk()
window.title("Text Editor")
file = None

windowWidth = 500
windowHeight = 500
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

fontName = StringVar(window)
fontName.set("Arial")
fontSize = StringVar(window)
fontSize.set("12")

textArea = Text(window, font=(fontName.get(), fontSize.get()))

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
textArea.grid(sticky=N + E + S + W)
scrollBar = Scrollbar(textArea)
scrollBar.pack(side=RIGHT, fill=Y)
textArea.configure(yscrollcommand=scrollBar.set)

frame = Frame(window)
frame.grid()

colorButton = Button(frame, text="color", command=changeColor)
colorButton.grid(row=0, column=0)

fontBox = OptionMenu(frame, fontName, *font.families(), command=changeFont)
fontBox.grid(row=0, column=1)

sizeBox = Spinbox(frame, from_=1, to=100, textvariable=fontSize, command=changeFont)
sizeBox.grid(row=0, column=2)

menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New File', command=newFile)
fileMenu.add_command(label='Open File', command=openFile)
fileMenu.add_command(label='Save File', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='About', command=about)


window.mainloop()

