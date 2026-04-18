'''Design a GUI based basic calculator for performing basic arithmetic operations.'''

import tkinter as tk

# Function to handle button click
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")

    elif text == "C":
        screen.set("")

    else:
        screen.set(screen.get() + text)

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 16")
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

# Run app
root.mainloop()