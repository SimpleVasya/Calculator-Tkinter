""" Calculator GUI by Piotr Goldys """ 
""" -*- A bit updated by Simple Vasya -*- """

from tkinter import *
import tkinter.ttk as tk


root = Tk()
root.title('Dr Pit Calculator')
root.config(bg='gray90')

root.resizable(width="false",height="false")
root.iconbitmap("C:\Windows\System32\eudcedit.exe")

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
def info():
    global tooltip
    tooltip = Tk()
    tooltip.title("Help")
    tooltip.resizable(width="false",height="false")
    tooltip.iconbitmap("C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_x86_d174002f2f9e1a17\\I386\\UNIDRV.HLP")


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
button1 = tk.Button(root, text='1',command=lambda: press_button(1))
button1.place(x=30,y=130)

button2 = tk.Button(root, text='2',command=lambda: press_button(2))
button2.place(x=110,y=130)

button3 = tk.Button(root, text='3', command=lambda: press_button(3))
button3.place(x=190,y=130)

button4 = tk.Button(root, text='4', command=lambda: press_button(4))
button4.place(x=30,y=160)

button5 = tk.Button(root, text='5', command=lambda: press_button(5))
button5.place(x=110,y=160)

button6 = tk.Button(root, text='6', command=lambda: press_button(6))
button6.place(x=190,y=160)

button7 = tk.Button(root, text='7', command=lambda: press_button(7))
button7.place(x=30,y=190)

button8 = tk.Button(root, text='8', command=lambda: press_button(8))
button8.place(x=110,y=190)

button9 = tk.Button(root, text='9', command=lambda: press_button(9))
button9.place(x=190,y=190)

button0 = tk.Button(root, text='0', command=lambda: press_button(0))
button0.place(x=110,y=220)


def destroyMenu():
    root.destroy()
    sys.exit()



    
m=Menu(root)
root.config(menu=m)

m1=Menu(m,tearoff=0)
m.add_cascade(label='•',menu=m1)

m1.add_command(label="Help",command=info)
m1.add_separator()
m1.add_command(label="Exit                        ",command=destroyMenu)



# DEL/C
buttonC = tk.Button(root, text='DEL/C')
buttonC.bind('<Button-3>', clear)
buttonC.bind('<Button-1>', delete)
buttonC.place(x=30,y=100)

# Ans
buttonAns = tk.Button(root, text='Ans', command=ans)
buttonAns.place(x=110,y=100)

# Percent
buttonPercent = tk.Button(root, text='%', command=percent)
buttonPercent.place(x=190,y=100)

# Sqrt
buttonSqrt = tk.Button(root, text=u"\u221A", command=sqrt)
buttonSqrt.grid(column=4, row=1, pady=3, padx=1)

# Multiplication
buttonMultiplication = tk.Button(root, text='x',command=lambda: press_button('*'))
buttonMultiplication.grid(column=4, row=3, pady=3, padx=1)

# Division
buttonDivision = tk.Button(root,text="/", command=lambda: press_button('/'))
buttonDivision.grid(column=4, row=4, pady=3, padx=1)

# Minus
buttonMinus = tk.Button(root, text='-', command=lambda: press_button('-'))
buttonMinus.grid(column=4, row=5, pady=3, padx=1)

# Plus
buttonPlus = tk.Button(root, text='+', command=lambda: press_button('+'))
buttonPlus.grid(column=4, row=6, pady=3, padx=1)

# Equal
buttonEqual = tk.Button(root, text='=')
buttonEqual.bind('<Button-1>', equals)
buttonEqual.place(x=190,y=220)

# Point
buttonPoint = tk.Button(root, text='.',  command=lambda: press_button('.'))
buttonPoint.place(x=30,y=220)


root.mainloop()

