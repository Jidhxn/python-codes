### The Calculator Code - Code Explanation

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
