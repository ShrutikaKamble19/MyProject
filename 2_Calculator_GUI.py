import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the input field
def click_button(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear the input field
def clear_input():
    input_text.set("")

# Function to evaluate the final expression
def calculate():
    try:
        result = str(eval(input_text.get()))  # `eval` evaluates the expression
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        input_text.set("")

# Setting up the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.resizable(False, False)

# StringVar to store the expression
input_text = tk.StringVar()

# Input field for the calculator
input_frame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side="top")

# Input entry box
input_field = tk.Entry(input_frame, font=("Arial", 18, "bold"), textvariable=input_text, width=50, bg="#eee", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for buttons
buttons_frame = tk.Frame(root, width=400, height=350, bg="grey")
buttons_frame.pack()

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
    # ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    # ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    # ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    # ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Creating buttons and placing them in the grid
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#f3a683", fg="black", command=clear_input)
    elif text == '=':
        button = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#78e08f", fg="black", command=calculate)
    else:
        button = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#f7f1e3", fg="black", command=lambda t=text: click_button(t))
    button.grid(row=row, column=col, padx=1, pady=1)

# Start the main event loop
root.mainloop()
