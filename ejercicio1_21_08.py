# Extraemos los nombres de productos a una lista
lista_productos = df_inventario['nombre'].tolist()
print(f"\nLista de productos original: {lista_productos}")
# Añadimos un nuevo producto
nuevo_producto = "Auriculares Inalámbricos"
lista_productos.append(nuevo_producto)
print(f"Lista actualizada con append(): {lista_productos}")
