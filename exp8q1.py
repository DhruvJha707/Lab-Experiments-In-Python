'''Create a simple Tkinter window with a title and fixed size. '''

import tkinter as tk

# Create main window
root = tk.Tk()

# Set window title
root.title("My Tkinter Window")

# Set fixed window size (width x height)
root.geometry("400x300")

# Disable resizing (fixed size)
root.resizable(False, False)

# Run the application
root.mainloop()