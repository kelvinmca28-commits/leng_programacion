import tkinter as tk
from tkinter import messagebox
def saludar():
  nombre = entrada.get()
  if nombre:
    messagebox.showinfo("BIENVENIDO", f"¡Hola, {nombre}! bienvenido al LABORATORIO DEL FUTURO")
  else:
    messagebox.showwarning("Advertencia", "Por favor, introduce tu nombre.")

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Introduccion en TKINTER")
ventana.geometry("400x200") # Establece el tamaño inicial de la ventana

# Crear y configurar widgets (elementos de la interfaz)
etiqueta = tk.Label(ventana, text="Introduce tu nombre y apellido:")
entrada = tk.Entry(ventana, width=45) # Se aumenta el ancho para mejor visualización
boton = tk.Button(ventana, text="Iniciar", command=saludar)

# Organizar los widgets en la ventana (gestión de layout)
etiqueta.pack(pady=10) # Añade un espacio vertical de 10 píxeles
entrada.pack(pady=5)
boton.pack(pady=10)

# Iniciar el bucle principal de eventos de la GUI
ventana.mainloop()
