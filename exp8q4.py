'''Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter 
(buttons, listbox), SQLite/MySQL (task storage). '''

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

# ================= FUNCTIONS =================
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]}. {row[1]}")

def add_task():
    task = task_var.get()
    if task == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    task_var.set("")
    load_tasks()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete!")
        return

    task_text = listbox.get(selected[0])
    task_id = int(task_text.split(".")[0])

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    load_tasks()

def edit_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to edit!")
        return

    task_text = listbox.get(selected[0])
    task_id = int(task_text.split(".")[0])
    new_task = task_var.get()

    if new_task == "":
        messagebox.showerror("Error", "Enter new task!")
        return

    cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
    conn.commit()
    task_var.set("")
    load_tasks()

# ================= UI =================
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x450")
root.resizable(False, False)

task_var = tk.StringVar()

# Entry
tk.Entry(root, textvariable=task_var, font=("Arial", 14)).pack(pady=10, padx=10, fill="x")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", width=12, command=add_task, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit Task", width=12, command=edit_task, bg="blue", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task, bg="red", fg="white").grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(padx=10, pady=10, fill="both", expand=True)

# Load existing tasks
load_tasks()

# Run app
root.mainloop()

# Close DB
conn.close()