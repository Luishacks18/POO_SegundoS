import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MiApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("#UEAESEXCELCIA")
        self.ventana.geometry("400x300")

        # Etiqueta
        self.etiqueta = tk.Label(self.ventana, text="Escribe algo para agregar:")
        self.etiqueta.pack(pady=10)

        # Entrada de texto
        self.entrada = tk.Entry(self.ventana, width=30)
        self.entrada.pack()

        # Botón para agregar
        self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar)
        self.boton_agregar.pack(pady=5)

        # Lista para mostrar datos
        self.lista = tk.Listbox(self.ventana, width=40, height=10)
        self.lista.pack(pady=10)

        # Botón para limpiar
        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar Lista", command=self.limpiar_lista)
        self.boton_limpiar.pack()

    def agregar(self):
        texto = self.entrada.get().strip()
        if texto == "":
            messagebox.showwarning("Advertencia", "No puedes agregar texto vacío.")
        else:
            self.lista.insert(tk.END, texto)
            self.entrada.delete(0, tk.END)

    def limpiar_lista(self):
        if self.lista.size() == 0:
            messagebox.showinfo("Información", "La lista ya está vacía.")
        else:
            self.lista.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
