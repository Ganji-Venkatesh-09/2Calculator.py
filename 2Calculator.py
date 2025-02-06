import tkinter as tk

# Function to handle button click events
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=6, height=2, font=('Arial', 20), command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, width=6, height=2, font=('Arial', 20), command=calculate)
    else:
        button = tk.Button(root, text=text, width=6, height=2, font=('Arial', 20), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Run the application
root.mainloop()
