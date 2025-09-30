import tkinter as tk
import matplotlib.pyplot as plt
# Importar matplotlib.pyplot as plt y FiguraCanvasTkAgg
# para una implementación real. Aquí solo es conceptual.

def plot_data():
# En una aplicación real, aquí se usaría Matplotlib
# para generar un gráfico y Canvas para incrustarlo
# en la ventana de Tkinter.
    messagebox.showinfo("Visualizador", "Mostrando gráfico de datos (conceptual)")

root = tk.Tk()
root.title("Visualizador de Datos")
data_label = tk.Label(root, text="Datos a visualizar (simulados): [1, 2, 5, 3, 7]")
data_label.pack(pady=10)
plot_button = tk.Button(root, text="Generar Gráfico", command=plot_data)
plot_button.pack()

# Aquí iría el Frame para incrustar el gráfico de
Matplotlib
# plot_frame = tk.Frame(root)
# plot_frame.pack(expand=True, fill="both")

root.mainloop()
