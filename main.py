#Author: captainmyth
#Date: 06/28/2024
#Description: A simple calculator using Python and tkinter
import tkinter as tk


#Creating and naming the main application
root = tk.Tk()
root.title("Calculator")

#Setting the size and limitations
root.geometry("400x500")
root.resizable(0, 0)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#Variables
equation = ""
calculation = tk.StringVar()
last_button_press = ""

#Button clicks and logic
def clearAll():
    global equation
    equation = ""
    calculation.set("")

def equals():
    global equation
    result = str(eval(equation))
    calculation.set(result)
    equation = ""
    
def buttonPress(button):
    global equation
    global last_button_press
    if str(button).isdigit():
        equation += str(button)
        last_button_press = "number"
    elif button in "+-*/" or button == ".":
        if last_button_press != "operand":
            equation += str(button)
            last_button_press = "operand"
    calculation.set(equation)

#Creating the Frames and packing them
results = tk.Frame(root)
results.pack(expand=True, fill="both")
keyboard_row_zero = tk.Frame(root)
keyboard_row_zero.pack(expand=True,fill="both")
keyboard_row_one = tk.Frame(root)
keyboard_row_one.pack(expand=True,fill="both")
keyboard_row_two = tk.Frame(root)
keyboard_row_two.pack(expand=True,fill="both")
keyboard_row_three = tk.Frame(root)
keyboard_row_three.pack(expand=True,fill="both")

#Creating the label/buttons
calculator =   tk.Entry(results, textvariable=calculation, borderwidth=2, relief='sunken')
all_clear   =   tk.Button(keyboard_row_three, text="AC", command=lambda: clearAll())
zero        =   tk.Button(keyboard_row_three, text="0", command=lambda: buttonPress(0))
one         =   tk.Button(keyboard_row_two, text="1", command=lambda: buttonPress(1))
two         =   tk.Button(keyboard_row_two, text="2", command=lambda: buttonPress(2))
three       =   tk.Button(keyboard_row_two, text="3", command=lambda: buttonPress(3))
four        =   tk.Button(keyboard_row_one, text="4", command=lambda: buttonPress(4))
five        =   tk.Button(keyboard_row_one, text="5", command=lambda: buttonPress(5))
six         =   tk.Button(keyboard_row_one, text="6", command=lambda: buttonPress(6))
seven       =   tk.Button(keyboard_row_zero, text="7", command=lambda: buttonPress(7))
eight       =   tk.Button(keyboard_row_zero, text="8", command=lambda: buttonPress(8))
nine        =   tk.Button(keyboard_row_zero, text="9", command=lambda: buttonPress(9))
equal       =   tk.Button(keyboard_row_three, text="=", command=lambda: equals())
plus        =   tk.Button(keyboard_row_three, text="+", command=lambda: buttonPress("+"))
minus       =   tk.Button(keyboard_row_two, text="-", command=lambda: buttonPress("-"))
divide      =   tk.Button(keyboard_row_zero, text="/", command=lambda: buttonPress("/"))
multiply    =   tk.Button(keyboard_row_one, text="*", command=lambda: buttonPress("*"))
decimal     =   tk.Button(keyboard_row_three, text=".", command=lambda: buttonPress("."))

#Setting up the buttons
calculator.pack(side=tk.TOP, expand=True, fill="both", padx=10, pady=10)
seven.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
eight.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
nine.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
four.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
five.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
six.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
multiply.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
one.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
two.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
three.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
minus.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
zero.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
decimal.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
plus.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
equal.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
all_clear.pack(side=tk.LEFT, expand=True, fill="both", padx=5)
divide.pack(side=tk.LEFT, expand=True, fill="both", padx=5)   

#Starting the program
root.mainloop()
