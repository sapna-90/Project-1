# Import Tkinter module
import tkinter as tk

#  Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create the input display field
display = tk.Entry(root, width=20, font=('Callibri', 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click functions
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

# Create number and operator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, font=('Callibri', 14),
              command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Define clear and equal functions
def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create clear and equal buttons
tk.Button(root, text="C", width=5, font=('Callibri', 14), command=button_clear).grid(row=row, column=0, padx=5, pady=5)
tk.Button(root, text="=", width=5, font=('Callibri', 14), command=button_equal).grid(row=row, column=1, columnspan=3, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()