from tkinter import *


equationText = ""

def buttonPress(num):
    global equationText
    equationText = equationText + str(num)
    equationLabel.set(equationText)

def equals():
    global equationText
    try:
        total = str(eval(equationText))
        equationLabel.set(total)
        equationText = total
    except ZeroDivisionError:
        equationLabel.set("Arithmetic Error")
        equationText = ""
    except SyntaxError:
        equationLabel.set("Syntax Error")
        equationText = ""

def clear():
    global equationText
    equationText = ""
    equationLabel.set(equationText)

window = Tk()
window.title("Calculator")
window.geometry("340x385")
window.resizable(width=FALSE, height=FALSE)

equationLabel = StringVar()


label = Label(window, textvariable=equationLabel, font=("Arial Bold", 20), bg='white', relief=GROOVE, width=21, height=2, anchor='e', justify='right', padx=10)
label.pack()

frames = Frame(window)
frames.pack()


button1 = Button(frames, text=1, height=2, width=7, font=35, command=lambda: buttonPress(1))
button1.grid(row=1, column=0)
button2 = Button(frames, text=2, height=2, width=7, font=35, command=lambda: buttonPress(2))
button2.grid(row=1, column=1)
button3 = Button(frames, text=3, height=2, width=7, font=35, command=lambda: buttonPress(3))
button3.grid(row=1, column=2)
button4 = Button(frames, text=4, height=2, width=7, font=35, command=lambda: buttonPress(4))
button4.grid(row=2, column=0)
button5 = Button(frames, text=5, height=2, width=7, font=35, command=lambda: buttonPress(5))
button5.grid(row=2, column=1)
button6 = Button(frames, text=6, height=2, width=7, font=35, command=lambda: buttonPress(6))
button6.grid(row=2, column=2)
button7 = Button(frames, text=7, height=2, width=7, font=35, command=lambda: buttonPress(7))
button7.grid(row=3, column=0)
button8 = Button(frames, text=8, height=2, width=7, font=35, command=lambda: buttonPress(8))
button8.grid(row=3, column=1)
button9 = Button(frames, text=9, height=2, width=7, font=35, command=lambda: buttonPress(9))
button9.grid(row=3, column=2)
button0 = Button(frames, text=0, height=2, width=7, font=35, command=lambda: buttonPress(0))
button0.grid(row=4, column=1)
plus = Button(frames, text='+', height=2, width=7, font=35, command=lambda: buttonPress('+'))
plus.grid(row=3, column=3)
minus = Button(frames, text='-', height=2, width=7, font=35, command=lambda: buttonPress('-'))
minus.grid(row=2, column=3)
multiply = Button(frames, text='x', height=2, width=7, font=35, command=lambda: buttonPress('*'))
multiply.grid(row=1, column=3)
divide = Button(frames, text='/', height=2, width=7, font=35, command=lambda: buttonPress('/'))
divide.grid(row=0, column=3)
decimal = Button(frames, text='.', height=2, width=7, font=35, command=lambda: buttonPress('.'))
decimal.grid(row=4, column=2)
equals = Button(frames, text='=', height=2, width=7, font=35, bg="#669bbc", command=equals)
equals.grid(row=4, column=3)
bracesL = Button(frames, text='(', height=2, width=7, font=30, command=lambda: buttonPress('('))
bracesL.grid(row=0, column=0)
bracesR = Button(frames, text=')', height=2, width=7, font=35, command=lambda: buttonPress(')'))
bracesR.grid(row=0, column=1)
percentage = Button(frames, text='%', height=2, width=7, font=35, command=lambda: buttonPress('%'))
percentage.grid(row=0, column=2)
clear = Button(frames, text='C', height=2, width=7, font=35, bg="#669bbc", command=clear)
clear.grid(row=4, column=0)

window.mainloop()