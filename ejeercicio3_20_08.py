# Historial de navegación
historial = ["google.com", "youtube.com", "openai.com"]
# Invertir orden
historial.reverse()
print(historial) # ['openai.com', 'youtube.com', 'google.com']

print()
numeracion=["cinco","cuatro","tres","dos","uno"]
numeracion.reverse()
print(numeracion)

print()
# Respuestas de encuesta
respuestas = ["sí", "no", "sí", "sí", "no"]
# Contar cuántos respondieron 'sí'
print(respuestas.count("sí")) # 3

print()
notas=[15,12,14,12,15,11,12,13,12,15]
print(notas.count(12))

print()
# Sistema de pedidos
pedidos = []
# Clientes hacen pedidos
pedidos.append("pizza")
pedidos.append("hamburguesa")
pedidos.append("pizza")
pedidos.append("ensalada")
# Revisar cuántas pizzas hay
print("Pizzas pedidas:", pedidos.count("pizza"))
# Eliminar un pedido cancelado
pedidos.remove("ensalada")
# Copiar la lista actual de pedidos
pedidos_backup = pedidos.copy()
# Ordenar los pedidos alfabéticamente
pedidos.sort()
print("Pedidos ordenados:", pedidos)
# Limpiar lista de pedidos al final del día
pedidos.clear()
print("Pedidos del día:", pedidos)
print("Respaldo:", pedidos_backup)
