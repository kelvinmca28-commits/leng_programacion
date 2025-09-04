cont = 1
while cont <= 5:
    print(cont)
    cont += 1

print()
while True:
    valor = int(input("ingrese un numero (0 para salir): "))
    if valor == 0:
        break
    print("ingresaste:", valor)

print()
cont = 5
while cont <= 10:
    print(cont)
    cont += 1

print()
counter = 100
while counter < 150:
    print(counter)
    counter += 10
else:
    print("terminado sin break")
