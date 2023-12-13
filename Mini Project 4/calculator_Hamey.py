# Ross Hamey
# CSE163 - Mini Project 4
# 12/13/2023
# https://github.com/Endeared

# tkinter import
from tkinter import *

# create a calculator
root = Tk()
root.title("Calculator")
root.resizable(False, False)

# window to display output, tall and wide
display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, ipadx=20, ipady=10)

# function to add pressed button to the display
def button_click(input):
    current = display.get()

    # if display is shwoing an error, clear it then store it to current
    if "current" == "Error":
        display.delete(0, END)
        current = display.get()
    
    # otherwise, only clear display after storing it
    display.delete(0, END)
    if input == "+" or input == "-" or input == "*" or input == "/":
        # check last letter of current, make sure it isnt a symbol
        try:
            # if it is a symbol, don't allow a new symbol to be added
            if current[-1] == "+" or current[-1] == "-" or current[-1] == "*" or current[-1] == "/":
                display.insert(0, str(current)[:-1] + str(input))
            # otherwise, add the symbol to the display
            else:
                display.insert(0, str(current) + str(input))
        except:
            # if we run into an error, it means there is no current, so we can't check the last letter. thus,
            # we check if the input is a symbol, and if it is, we don't add it to the display - if it isn't we
            # add it to the display
            if "-+/*".find(input) == -1:
                display.insert(0, str(current) + str(input))
    else:
        # if the input is a number, add it to the display
        display.insert(0, str(current) + str(input))            

def clear():
    # clear display
    display.delete(0, END)

def equal():
    # try to evaluate equation in display, otherwise show an error
    try:
        equation = display.get()
        result = eval(equation)
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def create_buttons():
    # create calculator buttons
    button_1 = Button(root, text="1", width=11, height=3, command=lambda: button_click(1), bg="white", fg="black", bd=2, relief="solid")
    button_2 = Button(root, text="2", width=11, height=3, command=lambda: button_click(2), bg="white", fg="black", bd=2, relief="solid")
    button_3 = Button(root, text="3", width=11, height=3, command=lambda: button_click(3), bg="white", fg="black", bd=2, relief="solid")
    button_4 = Button(root, text="4", width=11, height=3, command=lambda: button_click(4), bg="white", fg="black", bd=2, relief="solid")
    button_5 = Button(root, text="5", width=11, height=3, command=lambda: button_click(5), bg="white", fg="black", bd=2, relief="solid")
    button_6 = Button(root, text="6", width=11, height=3, command=lambda: button_click(6), bg="white", fg="black", bd=2, relief="solid")
    button_7 = Button(root, text="7", width=11, height=3, command=lambda: button_click(7), bg="white", fg="black", bd=2, relief="solid")
    button_8 = Button(root, text="8", width=11, height=3, command=lambda: button_click(8), bg="white", fg="black", bd=2, relief="solid")
    button_9 = Button(root, text="9", width=11, height=3, command=lambda: button_click(9), bg="white", fg="black", bd=2, relief="solid")
    button_0 = Button(root, text="0", width=11, height=3, command=lambda: button_click(0), bg="white", fg="black", bd=2, relief="solid")

    # add, subtract, equals, clear buttons
    button_add = Button(root, text="+", width=11, height=3, command=lambda: button_click("+"), bg="white", fg="black", bd=2, relief="solid")
    button_subtract = Button(root, text="-", width=11, height=3, command=lambda: button_click("-"), bg="white", fg="black", bd=2, relief="solid")
    button_equals = Button(root, text="=", width=11, height=3, command=lambda: equal(), bg="white", fg="black", bd=2, relief="solid")
    button_clear = Button(root, text="C", width=11, height=3, command=lambda: clear(), bg="white", fg="black", bd=2, relief="solid")

    # multiplication and division buttons
    button_multiply = Button(root, text="*", width=11, height=3, command=lambda: button_click("*"), bg="white", fg="black", bd=2, relief="solid")
    button_divide = Button(root, text="/", width=11, height=3, command=lambda: button_click("/"), bg="white", fg="black", bd=2, relief="solid")

    # put buttons on the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_multiply.grid(row=3, column=3)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_subtract.grid(row=2, column=3)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_add.grid(row=1, column=3)

    button_0.grid(row=4, column=1)
    button_clear.grid(row=4, column=0)
    button_equals.grid(row=4, column=2)
    button_divide.grid(row=4, column=3)

# run the calculator
create_buttons()
root.mainloop()