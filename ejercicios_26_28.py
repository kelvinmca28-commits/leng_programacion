meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
print(meses[1:4]) # Se extrae una lista con los valores 1, 2 y 3
print(meses[4:5]) # Se extrae una lista con el valor 4
print(meses[4:4]) # Se extrae una lista vacía
print(meses[:4]) # Se extrae una lista hasta el valor 4 (no incluido)
print(meses[4:]) # Se extrae una lista desde el valor 4 (incluido)
print(meses[:]) # Se extrae una lista con todos los valores

print()
peru=["Lima","Piura","Loreto","Cajamarca","Junin","Cusco","Arequipa","Puno","Tacna","Ayacucho","Ancash","Ica","Madre de Dios"]
print(peru[0:5])
print(peru[5:12])
print(peru[:5])
print(peru[5:5])
print(peru[6:])
print(peru[:])
print(peru[8:9])
print(peru[0:12])

print()
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[1:4] = ["X"] #Se sustituye la sublista ['B','C','D'] por ['X']
print(letras)
letras[1:4]=["Y","Z"]#sustituye ['X','E','F'] por ['Y','Z']
print(letras)
letras[0:1] = ["Q"] # Se sustituye la sublista ['A'] por ['Q']
print(letras)
letras[3:3]=["U","V"]# Inserta la lista ['U','V'] en la posición 3
print(letras)
letras[0:3] = [] # Elimina la sublista ['Q','Y', 'Z']
print(letras)

print()
print("EJEMPLO")
print()
notas=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(notas)
notas[0:3]=["AD"]
notas[1:4]=["A"]
notas[2:6]=["B"]
notas[3:]=["C"]
print(notas)
print("Donde:")
print(f"""AD = 20 - 18
A = 17 - 15
B = 14 - 11
C = 10 - 1""")

letras = ["D", "E", "F"]
letras[3:3] = ["G", "H"] # Añade ["G", "H"] al final de la lista
print(letras)
letras[50:50] = ["I", "J"] # Añade ["I", "J"] al final de la lista
print(letras)
letras[-50:-50]=["A", "B", "C"] #Añade ["A", "B", "C"] al principio de la lista
print(letras)

print()
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
del letras[4] # Elimina la sublista ['E']
print(letras)
del letras[1:4] # Elimina la sublista ['B', 'C', 'D']
print(letras)
del (letras[0:10]) # Elimina completamente la lista
print(letras)

print()
print("EJEMPLO")
print()
orden=["primero","segundo","tercero","cuarto","quinto","sexto","septimo","octavo","noveno"]
orden[50:50]=["decimo"]
del orden[0]
orden[:0]=["ONE"]
print(orden)

print()
a = (10,11,12,10,15,10,11)
print(a)
print(15 in a)
print(a.count(10))
print()
print("----"*10)
print("EJEMPLO")
print("----"*10)
notas=(11,13,13,15,11,17,18,15,15,16,14,20,13,19,17,11,13,13,15,11,17,18,15,15,16,14,15,13,19,17,14,14,16,19,18,10,11,9,18,18,17)
print("Existen las siguientes notas: ",notas)
print("Son un total de ",len(notas), "notas")
print("De las cuales se tiene:")
print("Nota 20:",notas.count(20))
print("Nota 19:",notas.count(19))
print("Nota 18:",notas.count(18))
print("Nota 17:",notas.count(17))
print("Nota 16:",notas.count(16))
print("Nota 15:",notas.count(15))
print("Nota 14:",notas.count(14))
print("Nota 13:",notas.count(13))
print("Nota 12:",notas.count(12))
print("Nota 11:",notas.count(11))
print("La peor nota es", min(notas),", y esta en la posicion: ", notas.index(min(notas)))
print("La mejor nota es", max(notas),", y esta en la posicion: ", notas.index(max(notas)))
notas1=(14,9,10,6,15,13,12,17,18,15)
print("Se agregaron las siguientes notas: ",notas1)
total=notas+notas1
print("Ahora existen un total de ",len(total), "notas,",total)
print("De las cuales ahora se tiene:")
print("Nota 20:",total.count(20))
print("Nota 19:",total.count(19))
print("Nota 18:",total.count(18))
print("Nota 17:",total.count(17))
print("Nota 16:",total.count(16))
print("Nota 15:",total.count(15))
print("Nota 14:",total.count(14))
print("Nota 13:",total.count(13))
print("Nota 12:",total.count(12))
print("Nota 11:",total.count(11))
print("La peor nota ahora es", min(total),", y esta en la posicion: ", total.index(min(total)))
print("La mejor nota ahora es", max(total),", y esta en la posicion: ", total.index(max(total)))
print("Luego de la peor nota, esta las siguientes notas:",total[45:])
print("Y de la mejor nota, esta las siguientes notas:",total[:11])
print("Existen algun 9 en las notas:",9 in total)
try:
  print("La nota 9 esta en la ubicacion:",total.index(9))
except ValueError:
  print("La nota 9 no se encuentra en la lista.")

print("Existen algun 8 en las notas:",8 in total)
try:
  print("La nota 8 esta en la ubicacion:",total.index(8))
except ValueError:
  print("La nota 8 no se encuentra en la lista.")
