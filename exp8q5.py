''' Design a login and signup authentication system.'''

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

# ================= FUNCTIONS =================
def signup():
    username = user_var.get()
    password = pass_var.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Account Created!")
    except:
        messagebox.showerror("Error", "User already exists!")

def login():
    username = user_var.get()
    password = pass_var.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def clear():
    user_var.set("")
    pass_var.set("")

# ================= UI =================
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("350x250")
root.resizable(False, False)

user_var = tk.StringVar()
pass_var = tk.StringVar()

# Labels & Entry
tk.Label(root, text="Username", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=user_var).pack(pady=5)

tk.Label(root, text="Password", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=pass_var, show="*").pack(pady=5)

# Buttons
tk.Button(root, text="Login", width=15, command=login, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Signup", width=15, command=signup, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Clear", width=15, command=clear).pack(pady=5)

# Run app
root.mainloop()

# Close DB
conn.close()