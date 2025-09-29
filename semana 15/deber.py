import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Frame para entrada y botones
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.task_entry.bind("<Return>", self.add_task_event)  # Añadir tarea con Enter

        # Botón para añadir tarea
        add_button = tk.Button(input_frame, text="Añadir Tarea", command=self.add_task)
        add_button.pack(side=tk.LEFT)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task_completion)  # Doble clic para marcar completada

        # Frame para botones de acción
        action_frame = tk.Frame(root)
        action_frame.pack(pady=5)

        # Botón para marcar tarea como completada
        complete_button = tk.Button(action_frame, text="Marcar como Completada", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        delete_button = tk.Button(action_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Diccionario para almacenar estado de tareas: key=index, value=bool(completada)
        self.tasks_completed = {}

    def add_task_event(self, event):
        """Manejador para añadir tarea con tecla Enter."""
        self.add_task()

    def add_task(self):
        """Añade una nueva tarea a la lista si el campo no está vacío."""
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea antes de añadir.")
            return
        # Añadir tarea a la lista visual
        self.task_listbox.insert(tk.END, task_text)
        # Inicialmente la tarea no está completada
        self.tasks_completed[self.task_listbox.size() - 1] = False
        self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        """Marca la tarea seleccionada como completada o no completada."""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Selección requerida", "Selecciona una tarea para marcar como completada.")
            return
        index = selected[0]
        self._toggle_completion_state(index)

    def toggle_task_completion(self, event):
        """Alterna el estado de completado al hacer doble clic en una tarea."""
        index = self.task_listbox.nearest(event.y)
        self._toggle_completion_state(index)

    def _toggle_completion_state(self, index):
        """Cambia el estado visual y lógico de una tarea dada su posición."""
        completed = self.tasks_completed.get(index, False)
        task_text = self.task_listbox.get(index)

        if not completed:
            # Marcar como completada: cambiar color y añadir prefijo
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, f"✔ {task_text}")
            self.task_listbox.itemconfig(index, fg="gray")
            self.tasks_completed[index] = True
        else:
            # Desmarcar completada: quitar prefijo y color
            if task_text.startswith("✔ "):
                task_text = task_text[2:]
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, task_text)
            self.task_listbox.itemconfig(index, fg="black")
            self.tasks_completed[index] = False

        # Mantener la selección en la tarea modificada
        self.task_listbox.selection_clear(0, tk.END)
        self.task_listbox.selection_set(index)

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista y del estado."""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Selección requerida", "Selecciona una tarea para eliminar.")
            return
        index = selected[0]
        self.task_listbox.delete(index)
        # Eliminar estado de la tarea
        self.tasks_completed.pop(index, None)
        # Ajustar índices en el diccionario de estados
        self._reindex_tasks_after_deletion(index)

    def _reindex_tasks_after_deletion(self, deleted_index):
        """Actualiza los índices en el diccionario de estados tras eliminar una tarea."""
        new_tasks_completed = {}
        for idx, completed in self.tasks_completed.items():
            if idx < deleted_index:
                new_tasks_completed[idx] = completed
            elif idx > deleted_index:
                new_tasks_completed[idx - 1] = completed
        self.tasks_completed = new_tasks_completed

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
