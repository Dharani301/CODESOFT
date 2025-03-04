import tkinter as tk
from tkinter import messagebox
import json

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Update task list display with checkboxes
def update_task_list(filtered_tasks=None):
    # Remove old widgets from the frame
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    task_list = filtered_tasks if filtered_tasks else tasks
    for i, task in enumerate(task_list):
        task_frame = tk.Frame(task_list_frame, bg="#f4f4f4")
        task_frame.pack(fill=tk.X, pady=2)

        # Create a BooleanVar for each task checkbox
        status = tk.BooleanVar(value=task["completed"])

        # Create a checkbox for each task
        checkbox = tk.Checkbutton(task_frame, variable=status, command=lambda i=i, status=status: toggle_task_status(i, status), bg="#f4f4f4")
        checkbox.pack(side=tk.LEFT, padx=10)

        # Display task number and text
        task_label = tk.Label(task_frame, text=f"{i + 1}. {task['task']}", font=("Arial", 12), bg="#f4f4f4", anchor="w")
        task_label.pack(side=tk.LEFT, padx=10, fill=tk.X)

        # Set checkbox state based on task completion status
        if task["completed"]:
            checkbox.select()
        else:
            checkbox.deselect()

# Toggle task completion status when checkbox is clicked
def toggle_task_status(index, status):
    tasks[index]["completed"] = status.get()
    save_tasks()

# Delete checked tasks
def delete_task():
    global tasks
    checked_tasks = [task for task in tasks if task["completed"]]
    if checked_tasks:
        tasks = [task for task in tasks if not task["completed"]]  # Keep only unchecked tasks
        save_tasks()
        update_task_list()
    else:
        messagebox.showwarning("Warning", "No completed tasks to delete!")

# Show all tasks
def show_all_tasks():
    update_task_list()

# Show completed tasks
def show_completed_tasks():
    completed_tasks = [task for task in tasks if task["completed"]]
    update_task_list(completed_tasks)

# Show pending tasks
def show_pending_tasks():
    pending_tasks = [task for task in tasks if not task["completed"]]
    update_task_list(pending_tasks)

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.configure(bg="#add8e6")  # Set background color for the window

tasks = load_tasks()

# Task Entry Field
task_entry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, relief="solid")
task_entry.pack(pady=20)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=10)

# Add Buttons with styling
add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, relief="flat", padx=10, pady=5)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task, font=("Arial", 12), bg="#F44336", fg="white", bd=0, relief="flat", padx=10, pady=5)
delete_btn.grid(row=0, column=1, padx=10)

# Filter Tasks Frame
filter_frame = tk.Frame(root, bg="#f4f4f4")
filter_frame.pack(pady=10)

all_btn = tk.Button(filter_frame, text="All Tasks", command=show_all_tasks, font=("Arial", 12), bg="#FF9800", fg="white", bd=0, relief="flat", padx=10, pady=5)
all_btn.grid(row=0, column=0, padx=10)

completed_btn = tk.Button(filter_frame, text="Completed Tasks", command=show_completed_tasks, font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, relief="flat", padx=10, pady=5)
completed_btn.grid(row=0, column=1, padx=10)

pending_btn = tk.Button(filter_frame, text="Pending Tasks", command=show_pending_tasks, font=("Arial", 12), bg="#2196F3", fg="white", bd=0, relief="flat", padx=10, pady=5)
pending_btn.grid(row=0, column=2, padx=10)

# Task List Frame for dynamically adding checkboxes and labels
task_list_frame = tk.Frame(root, bg="#f4f4f4")
task_list_frame.pack(pady=20, fill=tk.BOTH, expand=True)  

# Initial update of the task list
update_task_list()

# Run the application
root.mainloop()
