""" Calculator GUI by Piotr Goldys """

from tkinter import *


root = Tk()
root.title('Dr Pit Calculator')
root.config(bg='gray90')

# Necessary variables
tooltip = ''
equal = StringVar()
equation = ''
answer = ''
equal.set('Enter your equation')


''' Functions '''


# Pressing 'standard' buttons, mostly numeric
def press_button(num):
    global equal, equation
    # Prevents using double-comas
    if num == '.' and '.' in equation:
        equation = equation
    else:
        equation += str(num)
    equal.set(equation)


# DEL/C button right click action
def clear(event):
    global equal, equation
    equation = ''
    equal.set('')


# DEL/C button left click action
def delete(event):
    global equal, equation
    equation = equation[:-1]
    equal.set(equation)


# Equal button action
def equals(event):
    global equal, equation, answer
    equal.set(round(eval(equation), 9))
    answer = str(round(eval(equation), 9))
    equation = ''


# Percent button action
def percent():
    global answer, equal, equation
    press_button(answer + '/100')
    equals('<Button-1>')


# Sqrt button action
def sqrt():
    global answer, equal, equation
    press_button(answer + '**(1/2)')
    equals('<Button-1>')


# Ans button action
def ans():
    global equal, equation, answer
    equation += answer
    equal.set(equation)


# Showing info while hovering on 'help'
def info(event):
    global tooltip
    tooltip = Tk()
    infos = Label(tooltip, text='Left mouse button to delete \nRight mouse button to clear', font=('Arial', 15))
    infos.pack()


# Hiding info when not hovering on 'help' anymore
def exitt(event):
    global tooltip
    tooltip.destroy()


''' GUI Layout '''

# Calculator screen
screen = Label(root, textvariable=equal, font=("Arial", 30), height=2, width=20, bg='white')
screen.grid(column=1, row=0, columnspan=4)

# Numeric buttons
button1 = Button(root, text='1', height=2, width=4, font='arial 30 bold', command=lambda: press_button(1))
button1.grid(column=1, row=3, pady=10, padx=5)

button2 = Button(root, text='2', height=2, width=4, font='arial 30 bold', command=lambda: press_button(2))
button2.grid(column=2, row=3, pady=10, padx=5)

button3 = Button(root, text='3', height=2, width=4, font='arial 30 bold', command=lambda: press_button(3))
button3.grid(column=3, row=3, pady=10, padx=5)

button4 = Button(root, text='4', height=2, width=4, font='arial 30 bold', command=lambda: press_button(4))
button4.grid(column=1, row=4, pady=10, padx=5)

button5 = Button(root, text='5', height=2, width=4, font='arial 30 bold', command=lambda: press_button(5))
button5.grid(column=2, row=4, pady=10, padx=5)

button6 = Button(root, text='6', height=2, width=4, font='arial 30 bold', command=lambda: press_button(6))
button6.grid(column=3, row=4, pady=10, padx=5)

button7 = Button(root, text='7', height=2, width=4, font='arial 30 bold', command=lambda: press_button(7))
button7.grid(column=1, row=5, pady=10, padx=5)

button8 = Button(root, text='8', height=2, width=4, font='arial 30 bold', command=lambda: press_button(8))
button8.grid(column=2, row=5, pady=10, padx=5)

button9 = Button(root, text='9', height=2, width=4, font='arial 30 bold', command=lambda: press_button(9))
button9.grid(column=3, row=5, pady=10, padx=5)

button0 = Button(root, text='0', height=1, width=4, font='arial 30 bold', command=lambda: press_button(0))
button0.grid(column=2, row=6, pady=10, padx=5)

# Help
helpButton = Button(root, text='Help', relief=FLAT)
helpButton.place(x=0, y=0)
helpButton.bind('<Enter>', info)
helpButton.bind('<Leave>', exitt)

# DEL/C
buttonC = Button(root, text='DEL/C', height=3, width=8, font='arial 15 bold', fg='brown')
buttonC.bind('<Button-3>', clear)
buttonC.bind('<Button-1>', delete)
buttonC.grid(column=1, row=1, pady=10, padx=5)

# Ans
buttonAns = Button(root, text='Ans', height=3, width=8, font='arial 15 bold', command=ans)
buttonAns.grid(column=2, row=1, pady=10, padx=5)

# Percent
buttonPercent = Button(root, text='%', height=3, width=8, font='arial 15 bold', command=percent)
buttonPercent.grid(column=3, row=1, pady=10, padx=5)

# Sqrt
buttonSqrt = Button(root, text=u"\u221A", height=3, width=6, font='arial 15 bold', command=sqrt)
buttonSqrt.grid(column=4, row=1, pady=10, padx=5)

# Multiplication
buttonMultiplication = Button(root, text='x', height=2, width=3, font='arial 30 bold',
                              command=lambda: press_button('*'))
buttonMultiplication.grid(column=4, row=3, pady=10, padx=5)

# Division
buttonDivision = Button(root, text=chr(247), height=2, width=3, font='arial 30 bold', command=lambda: press_button('/'))
buttonDivision.grid(column=4, row=4, pady=10, padx=5)

# Minus
buttonMinus = Button(root, text='-', height=2, width=3, font='arial 30 bold', command=lambda: press_button('-'))
buttonMinus.grid(column=4, row=5, pady=10, padx=5)

# Plus
buttonPlus = Button(root, text='+', height=1, width=3, font='arial 30 bold', command=lambda: press_button('+'))
buttonPlus.grid(column=4, row=6, pady=10, padx=5)

# Equal
buttonEqual = Button(root, text='=', height=1, width=4, font='arial 30 bold')
buttonEqual.bind('<Button-1>', equals)
buttonEqual.grid(column=3, row=6, pady=10, padx=5)

# Point
buttonPoint = Button(root, text='.', height=1, width=4, font='arial 30 bold', command=lambda: press_button('.'))
buttonPoint.grid(column=1, row=6, pady=10, padx=5)


root.mainloop()
