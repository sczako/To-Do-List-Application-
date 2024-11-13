import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("to-do list")
root.geometry("400x400") 

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []  
        self.widgets()

    def widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.pack()

        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(pady=10)

        mark_completed_button = tk.Button(self.root, text="Completed", command=self.mark_completed)
        mark_completed_button.pack()

        remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_task_button.pack()

    def add_task(self):
        tasks = self.task_entry.get()
        if tasks:
            self.tasks.append(tasks)
            self.task_list.insert(tk.END, tasks)
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        try:
            selected_index = self.task_list.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{task} - Completed"
            self.task_list.delete(selected_index)
            self.task_list.insert(selected_index, self.tasks[selected_index])
        except IndexError:
            messagebox.showwarning("Select a task to mark as complete.")

    def remove_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.tasks.pop(selected_index)
            self.task_list.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Select a task to delete.") 

if __name__ == "__main__":
    app = ToDoApp (root)
    root.mainloop()
    
