from tkinter import *

root = Tk()
root.title("Simple Calc")
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):

    current = entry.get()
    entry.delete(0, END)

    if current is str:
        current = current.strip()
    if current == "":
        current = 0

    entry.insert(0, int(current)*10 + int(num))


global sign


def button_cleared():
    entry.delete(0, END)


def button_add():
    global sign
    number = entry.get()
    global first_num
    first_num = number
    sign = "+"
    entry.delete(0, END)


def button_min():
    global sign
    number = entry.get()
    global first_num
    first_num = number
    sign = "-"
    entry.delete(0, END)


def button_css():
    global sign
    number = entry.get()
    global first_num
    first_num = number
    sign = "x"
    entry.delete(0, END)


def button_div():
    global sign
    number = entry.get()
    global first_num
    first_num = number
    sign = "/"
    entry.delete(0, END)


def equal_():
    global sign
    number = entry.get()
    entry.delete(0, END)
    if sign == "+":
        entry.insert(0, int(first_num) + int(number))
    elif sign == "-":
        entry.insert(0, int(first_num) - int(number))
    elif sign == "/":
        entry.insert(0, int(first_num) / int(number))
    elif sign == "x":
        entry.insert(0, int(first_num) * int(number))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=38, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=38, pady=20, command=button_add)
button_minus = Button(root, text="-", padx=38, pady=20, command=button_min)
button_cross = Button(root, text="x", padx=38, pady=20, command=button_css)
button_divi = Button(root, text="/", padx=38, pady=20, command=button_div)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal_)
button_clear = Button(root, text="clear", padx=75, pady=20, command=button_cleared)

button_1.grid(row=1, column=0, padx=3, pady=3)
button_2.grid(row=1, column=1, padx=3, pady=3)
button_3.grid(row=1, column=2, padx=3, pady=3)
button_4.grid(row=2, column=0, padx=3, pady=3)
button_5.grid(row=2, column=1, padx=3, pady=3)
button_6.grid(row=2, column=2, padx=3, pady=3)
button_7.grid(row=3, column=0, padx=3, pady=3)
button_8.grid(row=3, column=1, padx=3, pady=3)
button_9.grid(row=3, column=2, padx=3, pady=3)
button_0.grid(row=4, column=0, padx=3, pady=3)
button_plus.grid(row=5, column=0, padx=3, pady=3)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_minus.grid(row=6, column=0, padx=3, pady=3)
button_cross.grid(row=6, column=1, padx=3, pady=3)
button_divi.grid(row=6, column=2, padx=3, pady=3)

root.mainloop()