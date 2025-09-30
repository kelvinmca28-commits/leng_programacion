import tkinter as tk

def convert_units():
    try:
        value = float(input_value.get())
        unit_from = unit_from_var.get()
        unit_to = unit_to_var.get()
        result = "N/A" # Lógica de conversión(simplificada)
        if unit_from == "Metros" and unit_to == "Pies":
            result = f"{value * 3.28084:.2f} pies"
        elif unit_from == "Pies" and unit_to == "Metros":
            result = f"{value / 3.28084:.2f} metros"
        elif unit_from == "Metros" and unit_to == "Kilometros":
            result = f"{value * 1000:.2f} metros"
        output_result.set(result)
    except ValueError:
        output_result.set("Inválido")
        
root = tk.Tk()
root.title("Conversor de Unidades")
units = ["Metros", "Pies", "Kilometros", "Libras"]
unit_from_var = tk.StringVar(root)
unit_from_var.set(units[0])
unit_to_var = tk.StringVar(root)
unit_to_var.set(units[1])

input_value = tk.Entry(root)
input_value.pack(pady=5)
tk.OptionMenu(root, unit_from_var, *units).pack()
tk.OptionMenu(root, unit_to_var, *units).pack()
tk.Button(root, text="Convertir", command=convert_units).pack(pady=5)
output_result = tk.StringVar()
tk.Label(root, textvariable=output_result).pack(pady=5)
root.mainloop()
