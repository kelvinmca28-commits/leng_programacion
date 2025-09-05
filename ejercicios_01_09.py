#for i in [0, 1, 2]:
# for j in [5, 6]:
# print(f"i vale {i} y j vale {j}")
for i in [0, 1, 2]:
  for j in [5, 6]:
#print(f"i vale {i} y j vale {j}")
    print(i,j)

print()
for i in range(3):
  for j in range(2):
#print(f"i vale {i} y j vale {j}")
    print(i,j)

print()

print()
for i in [0, 1, 2, 3, 4, 5, 6]:
  print(f"{i} * {i} = {i ** 2}")
print()
for i in [0, 1, 2, 3]:
  print(f"{i} * {i} * {i} = {i ** 3}")

i = 0
print(f"El bucle no ha comenzado. Ahora i vale {i}")
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
  print(f"{i} * {i} * {i} = {i ** 3}")
print(f"El bucle ha terminado. Ahora i vale {i}")

print()
for i in [0, 1, 2]:
  print(f"{i} * {i} = {i ** 2}")
print()
for i in [0, 1, 2, 3]:
  print(f"{i} * {i} * {i} = {i ** 3}")

print()
print("-" * 20)
print("Ejemplo 01")
print("-" * 20)
for i in range(10):
  print(f"2 + ({i} * {i}) = {2 + (i ** 2)}")


print()
for i in "CETPRO":
  print(f"Dame una {i}")
print("¡CETPRO PUNO!")

print()
print("-" * 20)
print("Ejemplo 02")
print("-" * 20)
print()
multi = int(input("¿Cuántas veces quiere aparesca? "))
for i in range(multi):
  print(f"{i} * {i} * {i} = {i ** 3}")
print()
print("Adiós")

print("-" * 20)
print("Ejemplo 03")
print("-" * 20)
print()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  print(f"{i} * 7 = {i * 7}")
print()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  print(f"{i} * 9 = {i * 9}")

print()
print("-" * 20)
print("Ejemplo 04")
print("-" * 20)
numero = int(input("La tabla del "))
tabla = int(input("Hasta el numero "))
print()
for i in range(tabla):
  print(f"{i} * {numero} = {i * numero}")
print()

print()
print("-" * 20)
print("Ejemplo 04")
print("-" * 20)
print()
multi = int(input("¿Cuántas veces quiere aparesca? "))
for i in range(multi):
  print(f"Vamos Perú!!! ", end="")
print()
print("Felicidades")
