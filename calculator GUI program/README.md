### The Calculator Code

```python
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
```

### Code Explanation

#### Importing Tkinter

```python
from tkinter import *
```

- **Tkinter Import:** We import all the necessary functions and classes from the Tkinter module to create our GUI.

#### Global Variable for Equation Text

```python
equationText = ""
```

- **Global Variable:** `equationText` is a global variable that stores the current equation displayed on the calculator screen.

#### Button Press Function

```python
def buttonPress(num):
    global equationText
    equationText = equationText + str(num)
    equationLabel.set(equationText)
```

- **Function Definition:** `buttonPress` appends the pressed button's value to `equationText` and updates the display.

#### Equals Function

```python
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
```

- **Function Definition:** `equals` evaluates the current equation using `eval()`. It handles errors such as division by zero and syntax errors.

#### Clear Function

```python
def clear():
    global equationText
    equationText = ""
    equationLabel.set(equationText)
```

- **Function Definition:** `clear` resets `equationText` and updates the display to be empty.

#### Setting Up the Window

```python
window = Tk()
window.title("Calculator")
window.geometry("340x385")
window.resizable(width=FALSE, height=FALSE)
```

- **Window Initialization:** We create the main window, set its title, size, and make it non-resizable.

#### Display Label

```python
equationLabel = StringVar()
label = Label(window, textvariable=equationLabel, font=("Arial Bold", 20), bg='white', relief=GROOVE, width=21, height=2, anchor='e', justify='right', padx=10)
label.pack()
```

- **Label Creation:** We create a label to display the equation and results, setting its text variable, font, background color, and other properties.

#### Button Frame

```python
frames = Frame(window)
frames.pack()
```

- **Frame Creation:** We create a frame to organize the calculator buttons.

#### Calculator Buttons

```python
button1 = Button(frames, text=1, height=2, width=7, font=35, command=lambda: buttonPress(1))
button1.grid(row=1, column=0)
button2 = Button(frames, text=2, height=2, width=7, font=35, command=lambda: buttonPress(2))
button2.grid(row=1, column=1)
...
clear = Button(frames, text='C', height=2, width=7, font=35, bg="#669bbc", command=clear)
clear.grid(row=4, column=0)
```

- **Button Creation:** We create buttons for numbers, operators, and special functions like clear and equals. Each button calls `buttonPress` with the appropriate value or function.

#### Main Loop

```python
window.mainloop()
```

- **Main Loop:** We start the Tkinter event loop to keep the window open and responsive.
