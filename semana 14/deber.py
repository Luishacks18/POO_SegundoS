import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Lista para guardar los eventos
eventos = []

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    desc = entry_desc.get()

    if fecha == "" or hora == "" or desc == "":
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except:
        messagebox.showwarning("Error", "La fecha debe ser YYYY-MM-DD")
        return

    try:
        datetime.strptime(hora, "%H:%M")
    except:
        messagebox.showwarning("Error", "La hora debe ser HH:MM (24h)")
        return

    eventos.append((fecha, hora, desc))
    actualizar_lista()

    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

# Función para borrar evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showinfo("Aviso", "Selecciona un evento para eliminar")
        return
    confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
    if confirmar:
        item = seleccionado[0]
        tree.delete(item)

# Función para refrescar el TreeView
def actualizar_lista():
    for i in tree.get_children():
        tree.delete(i)
    for ev in eventos:
        tree.insert("", tk.END, values=ev)

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# Frame de lista
frame_lista = ttk.Frame(root)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(frame_lista, columns=("fecha", "hora", "desc"), show="headings")
tree.heading("fecha", text="Fecha")
tree.heading("hora", text="Hora")
tree.heading("desc", text="Descripción")

tree.column("fecha", width=100)
tree.column("hora", width=70)
tree.column("desc", width=350)

tree.pack(fill="both", expand=True)

#entrada
frame_entrada = ttk.LabelFrame(root, text="Nuevo Evento")
frame_entrada.pack(fill="x", padx=10, pady=10)

ttk.Label(frame_entrada, text="Fecha :").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = ttk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Hora :").grid(row=1, column=0, padx=5, pady=5)
entry_hora = ttk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_desc = ttk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

#botones
frame_botones = ttk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = ttk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5)

root.mainloop()
