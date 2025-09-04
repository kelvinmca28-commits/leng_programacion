print()
tareas = ["estudiar", "limpiar", "comprar"]
tarea = tareas.pop()
print(tarea) # comprar
print(tareas) # ['estudiar', 'limpiar']

print()
notas=[15,18,12,20,10]
notanegativa = notas.pop()
print(notanegativa)
print(notas)

print()
usuarios_A = ["Ana", "Luis"]
usuarios_B = ["María", "Pedro"]
# Combinar con extend
usuarios_A.extend(usuarios_B)
print(usuarios_A) # ['Ana', 'Luis', 'María', 'Pedro']

print()
cetpro_puno=["lenguaje de programacion","redes","ofimatica"]
cetpro_juliaca=["mecanica de produccion","pasteleria","corte y confeccion"]
cetpro_puno.extend(cetpro_juliaca)
print(cetpro_puno)

print()
# Puntuaciones de jugadores
puntuaciones = [450, 1200, 750, 300]
# Ordenar la lista
puntuaciones.sort()
print(puntuaciones) # [300, 450, 750, 1200]

print()
numeracion=[11,13,16,17,20,12,15,17,19]
numeracion.sort()
print(numeracion)

