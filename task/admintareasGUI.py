import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title} - {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        if title:
            task = Task(title, description)
            self.tasks.append(task)
            return True
        return False

    def get_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()


class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("📝 Gestor de Tareas")

        self.create_widgets()

    def create_widgets(self):
        # Entradas
        tk.Label(self.root, text="Título:").grid(row=0, column=0, sticky="e")
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Descripción:").grid(row=1, column=0, sticky="e")
        self.desc_entry = tk.Entry(self.root, width=40)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón agregar
        self.add_button = tk.Button(self.root, text="Agregar Tarea", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de tareas
        self.task_frame = tk.Frame(self.root)
        self.task_frame.grid(row=3, column=0, columnspan=2)

        self.update_task_list()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if self.manager.add_task(title, description):
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "El título es obligatorio.")

    def update_task_list(self):
        # Limpiar tareas anteriores
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        tasks = self.manager.get_tasks()
        if not tasks:
            tk.Label(self.task_frame, text="No hay tareas.").pack()
            return

        for index, task in enumerate(tasks):
            task_str = str(task)
            task_label = tk.Label(self.task_frame, text=task_str, anchor="w", width=60)
            task_label.grid(row=index, column=0, sticky="w")

            if not task.completed:
                done_btn = tk.Button(self.task_frame, text="Completar", command=lambda i=index: self.complete_task(i))
                done_btn.grid(row=index, column=1)

    def complete_task(self, index):
        self.manager.complete_task(index)
        self.update_task_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
