import tkinter as tk

# Function to update the expression
def press(num):
    entry_field.insert(tk.END, num)  # Insert the number into the entry field

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_field.get())  # Evaluate the expression
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(tk.END, result)  # Show result
    except:
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(tk.END, "Error")  # Show error

# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  # Set window size

# Entry field for displaying input and results
entry_field = tk.Entry(root, font=("Arial", 18), bd=8, relief=tk.SUNKEN, justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "C":
        action = clear  # Assign clear function to C button
    elif text == "=":
        action = calculate  # Assign calculate function to = button
    else:
        action = lambda t=text: press(t)  # Insert button text when clicked

    tk.Button(root, text=text, font=("Arial", 16), command=action, width=5, height=2).grid(row=row, column=col, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
