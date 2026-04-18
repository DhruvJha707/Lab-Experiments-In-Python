'''Design a GUI for student registration for a course and store these details in a database. Use 
Tkinter for UI, SQLite/MySQL for database storage. '''

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT,
    phone TEXT
)
""")
conn.commit()

# ================= FUNCTIONS =================
def add_student():
    name = name_var.get()
    email = email_var.get()
    course = course_var.get()
    phone = phone_var.get()

    if name == "" or email == "" or course == "" or phone == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO students (name, email, course, phone) VALUES (?, ?, ?, ?)",
                   (name, email, course, phone))
    conn.commit()

    messagebox.showinfo("Success", "Student Added Successfully!")
    clear_fields()
    view_students()

def view_students():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

def clear_fields():
    name_var.set("")
    email_var.set("")
    course_var.set("")
    phone_var.set("")

# ================= UI =================
root = tk.Tk()
root.title("Student Registration System")
root.geometry("700x500")
root.resizable(False, False)

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
course_var = tk.StringVar()
phone_var = tk.StringVar()

# Form Frame
form_frame = tk.Frame(root)
form_frame.pack(pady=20)

tk.Label(form_frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, padx=10)

tk.Label(form_frame, text="Email", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=email_var).grid(row=1, column=1, padx=10)

tk.Label(form_frame, text="Course", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=course_var).grid(row=2, column=1, padx=10)

tk.Label(form_frame, text="Phone", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=phone_var).grid(row=3, column=1, padx=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", command=add_student, bg="green", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_fields, bg="red", fg="white").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="View Students", command=view_students).grid(row=0, column=2, padx=10)

# Table
tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Course", "Phone"), show="headings")
tree.pack(fill="both", expand=True, padx=20, pady=20)

for col in ("ID", "Name", "Email", "Course", "Phone"):
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Run app
root.mainloop()

# Close DB when app closes
conn.close()