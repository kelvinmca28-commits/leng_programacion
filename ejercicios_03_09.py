curso = {'Matemáticas': 5, 'Física': 3, 'Química': 4}
t_valor = 0
for clave, valor in curso.items():
  print(clave, 'tiene', valor, 'créditos')
#t_valor += valor
  t_valor = t_valor + valor
print('Número total de créditos del curso: ', t_valor)

print()
p = int(input('¿Cual es tu peso? '))
a = float(input('¿Cual es tu altura? '))
IMC = {'peso': p, 'altura': a}
resultado = 0
for clave, valor in IMC.items():
  if clave == 'peso':
    print(clave, 'tiene', valor, 'kg')
  elif clave == 'altura':
    print(clave, 'tiene', valor, 'metros')
#t_valor += valor
  resultado = p / (a ** 2)
print('Tu IMC es: ', resultado)

n = input('¿Cómo te llamas? ')
e = input('¿Cuántos años tienes? ')
d = input('¿Cuál es tu dirección? ')
persona = {'n': n, 'e': e, 'd': d}
print(persona["n"], 'tiene', persona['e'], 'años y vive en', persona['d'])

print()
n = input('¿Cómo te llamas? ')
e = input('¿Cuántos años tienes? ')
d = input('¿Cuál es tu dirección? ')
persona = {'Nombre': n, 'Edad': e, 'Direccion': d}
for key in persona:
  print(key,":", persona[key])


print()
print("-"*20)
print("EJEMPLO")
print("-"*20)
pc = input('¿Que marca es tu PC? ')
proc = input('¿Que procesador tiene? ')
ram = input('¿Que memoria RAM tiene? ')
alm = input('¿Que almacenamiento tiene? ')
tarj = input('¿Que tarjeta grafica tiene? ')
comp = {'Marca': pc, 'Procesador': proc, 'RAM': ram, 'Almacenamiento': alm, 'Tarjeta Grafica': tarj}
print("Tu computadora es una", comp["Marca"],comp["Procesador"], "con una memoria RAM de ", comp["RAM"], ", un almacenamiento de", comp["Almacenamiento"], "y una tarjeta grafica", comp["Tarjeta Grafica"])

print()
pc_marca = input('¿Que marca es tu PC? ')
proc = input('¿Que procesador tiene? ')
ram = input('¿Que memoria RAM tiene? ')
alm = input('¿Que almacenamiento tiene? ')
tarj = input('¿Que tarjeta grafica tiene? ')
comp1 = {'Marca': pc_marca, 'Procesador': proc, 'RAM': ram, 'Almacenamiento': alm, 'Tarjeta Grafica': tarj}
for key in comp1:
  print(key,":", comp1[key])

diccionario={'nombre':'Carlos','edad':22,'cursos':['Matemática','Fisica','Computo']}
print(diccionario)
print(diccionario['nombre']) #Carlos
print(diccionario['edad'])#22
print(diccionario['cursos']) #['Matemática','Fisica','Computo']

print()
diccionario={'nombre':'Carlos','edad':22,'cursos':['Matemática','Fisica','Computo']}
print(diccionario)
print(diccionario['cursos'][0])#Matematica
print(diccionario['cursos'][1])#Fisica
print(diccionario['cursos'][2])#Computo

print()
diccionario={'nombre':'Carlos','edad':22,'cursos':['Matemática','Fisica','Computo']}
print(diccionario)
for key in diccionario:
  print(key,":", diccionario[key])

print()
diccionario = {
"clave1":234,
"clave2":True,
"clave3":"Valor 1",
"clave4":[1,2,3,4]
}
print(diccionario, type(diccionario))
print(diccionario)
print(type(diccionario))

print()
usuarios = {
"cliente1":"percy",
"cliente2":"Gustavo",
"cliente3":"Andre",
"cliente4":"Carlos",
"cliente5":"Esteban",
"cliente6":"Ruth"
}
for key in usuarios:
  print(key,":", usuarios[key])
print(type(usuarios))

print()
datos_basicos = {
"apellidos":"Caballero Garcia",
"DNI":"26938401",
"fecha_nacimiento":"03/12/1980",
"lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
"nacionalidad":"Peruana",
"estado_civil":"Soltera"
}
print (datos_basicos, type(datos_basicos))
print (datos_basicos)
print (type(datos_basicos))
