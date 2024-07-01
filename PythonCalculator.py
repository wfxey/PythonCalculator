# Author: captainmyth - wfxey
# Date: 07/01/2024
# Description: A simple calculator using Python and customtkinter
import customtkinter as ctk
from CTkMenuBar import CTkTitleMenu, CustomDropdownMenu
from tkinter import filedialog

#Main Application
root = ctk.CTk()
root.title("Calculator")
root.iconbitmap("icon.ico")
root.geometry("800x600")
root.resizable(0, 0)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

menu = CTkTitleMenu(root)

#Variables
equation = ""
calculation = ctk.StringVar()
last_button_press = ""

#Logic
def save_file():
    code = history.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(code)
            
def clearAll():
    global equation
    equation = ""
    calculation.set("")

def clear_text():
    history.delete(1.0, ctk.END)

def equals():
    global equation
    result = str(eval(equation))
    calculation.set(result)
    history.insert(ctk.END, f"{equation} = {result}\n")
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

#File menu
file_menu_btn = menu.add_cascade("File")
file_menu = CustomDropdownMenu(widget=file_menu_btn)
file_menu.add_option(option="Save", command=save_file)
file_menu.add_separator()
file_menu.add_option(option="Exit", command=root.quit)

#Design menu
design_menu_btn = menu.add_cascade("Design")
design_menu = CustomDropdownMenu(widget=design_menu_btn)
design_menu.add_option(option="Dark", command=lambda: ctk.set_appearance_mode("Dark"))
design_menu.add_option(option="Light", command=lambda: ctk.set_appearance_mode("Light"))

#Frames
bar_fm = ctk.CTkFrame(root)
bar_fm.pack(side=ctk.BOTTOM, pady=10, padx=10)
results = ctk.CTkFrame(root)
results.pack(expand=True, fill="both")
keyboard_row_zero = ctk.CTkFrame(root)
keyboard_row_zero.pack(expand=True, fill="both")
keyboard_row_one = ctk.CTkFrame(root)
keyboard_row_one.pack(expand=True, fill="both")
keyboard_row_two = ctk.CTkFrame(root)
keyboard_row_two.pack(expand=True, fill="both")
keyboard_row_three = ctk.CTkFrame(root)
keyboard_row_three.pack(expand=True, fill="both")
history_frame = ctk.CTkFrame(root)
history_frame.pack(side=ctk.TOP, expand=True, fill="both")

#Labels, Buttons and stuff
calculator = ctk.CTkEntry(results, textvariable=calculation)
all_clear = ctk.CTkButton(keyboard_row_three, text="AC", command=clearAll)
zero = ctk.CTkButton(keyboard_row_three, text="0", command=lambda: buttonPress(0))
one = ctk.CTkButton(keyboard_row_two, text="1", command=lambda: buttonPress(1))
two = ctk.CTkButton(keyboard_row_two, text="2", command=lambda: buttonPress(2))
three = ctk.CTkButton(keyboard_row_two, text="3", command=lambda: buttonPress(3))
four = ctk.CTkButton(keyboard_row_one, text="4", command=lambda: buttonPress(4))
five = ctk.CTkButton(keyboard_row_one, text="5", command=lambda: buttonPress(5))
six = ctk.CTkButton(keyboard_row_one, text="6", command=lambda: buttonPress(6))
seven = ctk.CTkButton(keyboard_row_zero, text="7", command=lambda: buttonPress(7))
eight = ctk.CTkButton(keyboard_row_zero, text="8", command=lambda: buttonPress(8))
nine = ctk.CTkButton(keyboard_row_zero, text="9", command=lambda: buttonPress(9))
equal = ctk.CTkButton(keyboard_row_three, text="=", command=equals)
plus = ctk.CTkButton(keyboard_row_three, text="+", command=lambda: buttonPress("+"))
minus = ctk.CTkButton(keyboard_row_two, text="-", command=lambda: buttonPress("-"))
divide = ctk.CTkButton(keyboard_row_zero, text="/", command=lambda: buttonPress("/"))
multiply = ctk.CTkButton(keyboard_row_one, text="*", command=lambda: buttonPress("*"))
decimal = ctk.CTkButton(keyboard_row_three, text=".", command=lambda: buttonPress("."))
history_label = ctk.CTkLabel(history_frame, text="History")
history_label.pack(side=ctk.TOP)
history = ctk.CTkTextbox(history_frame)
history.pack(expand=True, fill="both")
clear_history_btn = ctk.CTkButton(bar_fm, text="Clear history", command=clear_text, fg_color="red3", hover_color="red4")
clear_history_btn.pack(pady=10, padx=10)

#Positioning and configuration
calculator.pack(side=ctk.TOP, expand=True, fill="both", padx=10, pady=10)
seven.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
eight.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
nine.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
four.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
five.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
six.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
multiply.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
one.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
two.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
three.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
minus.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
zero.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
decimal.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
plus.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
equal.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
all_clear.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)
divide.pack(side=ctk.LEFT, expand=True, fill="both", padx=5, pady=5)

#Start
root.mainloop()