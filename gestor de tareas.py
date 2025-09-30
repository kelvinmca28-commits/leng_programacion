import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0, tk.END)
    else:
        
        messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

root = tk.Tk()
root.title("Gestor de Tareas")
task_entry = tk.Entry(root,width=50)
task_entry.pack(pady=10)
add_button = tk.Button(root,text="Añadir Tarea",
command=add_task)
add_button.pack()
task_listbox = tk.Listbox(root,width=50, height=10)
task_listbox.pack(pady=10)
delete_button = tk.Button(root,text="Eliminar Tarea",command=delete_task)
delete_button.pack()
root.mainloop()
