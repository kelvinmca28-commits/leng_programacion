print(f"Ejercicio01: COUNT E INDEX")
# Datos de ejemplo: categorías observadas
categorias = ('A', 'B', 'A', 'C', 'A', 'B','A', 'B', 'A', 'C', 'A', 'B')
# ¿Cuántas veces aparece 'A'?
total_A = categorias.count('A') # 3
# ¿En qué posición aparece por primera vez 'C'?
pos_C = categorias.index('C') # 3
print(      total_A, pos_C)
print(f"  EJEMPLO")
notas=(11,13,13,15,11,17,18,15,15,16,14,20,13,19,17,11,13,13,15,11,17,18,15,15,16,14,20,13,19,17,11,13,13,15,11,17,18,15,15,16,14,20,13,19,17)
print(f"De la lista: 11,13,13,15,11,17,18,15,15,16,14,20,13,19,17,11,13,13,15,11,17,18,15,15,16,14,20,13,19,17,11,13,13,15,11,17,18,15,15,16,14,20,13,19,17")
nota_18=notas.count(18)
nota_19=notas.count(19)
nota_20=notas.count(20)
mejor_nota=notas.index(20)
print("Nota 18:",nota_18  ,"Nota 19:",nota_19  ,"Nota 20:",nota_20)
print("La mejor nota esta en la posicion: ", mejor_nota)

print()
print(f"Ejercicio02: Desempaquetado básico de registros")
# Un registro de producto (id, nombre, precio, categoría)
registro = (1001, 'Laptop', 1299.0, 'Electrónica')
id_prod, nombre, precio, categoria = registro
# Podemos ignorar campos con el guión bajo
id2, _, precio2, _ = registro
print(id_prod, nombre, precio, categoria)
print(f"  EJEMPLO")
registro=(6644, "PC", "Teros CORE i7", 1850.00, 5)
codigo, equipo, marca, precios, unidades=registro
print("Codigo de la unidad:",codigo, "Equipo:",equipo, "marca:",marca, "precio:",precios, "Unidades:",unidades)

print()
print(f"Ejercicio03: Desempaquetado en bucles para agregaciones")
# Lista de tuplas: (venta_id, categoría, unidades)
ventas = [
 (1, 'A', 10),
 (2, 'B', 7),
 (3, 'A', 5),
 (4, 'B', 14),
 (5, 'B', 11),
 (6, 'A', 9),
 (7, 'A', 8),
 (8, 'B', 4),
 (9, 'A', 5),
]
totales = {}
for _, cat, unidades in ventas:
 totales[cat] = totales.get(cat, 0) + unidades
print(totales) # {'A': 15, 'B': 7}

print(f"Ejercicio04:  Desempaquetado con * para tamaños variables")
registro = ('U123', 'Perú', 'premium', 'activa', '2025-08-01')
user_id, pais, *atributos, fecha = registro
print(user_id) # 'U123'
print(pais) # 'Perú'
print(atributos) # ['premium', 'activa']
print(fecha) # '2025-08-01'

print()
print(f"  EJEMPLO")

print()
print(f"Ejercicio05:  Pares clave-valor con tuplas → dict")
precios = [('A', 10.0), ('B', 5.5), ('C', 8.0)]
precio_por_cat = dict(precios)
print(precio_por_cat['B']) # 5.5

print()
print(f"  EJEMPLO")

print()
print(f"Ejercicio06:  Ordenar listas de tuplas por una columna")
productos = [('Laptop', 1299), ('Mouse', 20), ('Monitor', 250)]
ordenados = sorted(productos, key=lambda x: x[1], reverse=True)
print(ordenados) # [('Laptop', 1299), ('Monitor', 250), ('Mouse', 20)]

print(f"Ejercicio07:  Conteo de categorías con Counter")
from collections import Counter
ventas = [
 (1, 'A', 10),
 (2, 'B', 7),
 (3, 'A', 5),
]
categorias = [cat for _, cat, _ in ventas]
conteo = Counter(categorias)
print(conteo) # Counter({'A': 2, 'B': 1})
print()
print(f"  EJEMPLO")

print()
print(f"Ejercicio08:  De lista de tuplas a pandas DataFrame")
import pandas as pd
ventas = [
 (1, 'A', 10),
 (2, 'B', 7),
 (3, 'A', 5),
]
df = pd.DataFrame(ventas, columns=['id', 'cat', 'unidades'])
res = df.groupby('cat')['unidades'].sum().reset_index()
print(res)
print()
print(f"  EJEMPLO")

print()
print(f"Ejercicio09:   Desempaquetar tuplas dentro de una columna de DataFrame")
import pandas as pd
df_coords = pd.DataFrame({
 'id': [1, 2, 3],
 'coord': [(-12.05, -77.05), (-16.40, -71.50), (-13.50, -76.10)]
})
# Expandir la tupla (lat, lon) en dos columnas
df_coords[['lat', 'lon']] = pd.DataFrame(df_coords['coord'].tolist(), index=df_coords.index)
print(df_coords)
print()
print(f"  EJEMPLO")
