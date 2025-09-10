def sumar(numero1, numero2=20):
    print(numero1 + numero2)
sumar(10,15)
sumar(10)

print()
def sumar(numero1,numero2=20):
    print(numero1)
    print(numero2)
    print(numero1 + numero2)
sumar(numero2=10, numero1=15)#15, 10 25
sumar(10) #10, 20, 30

print()
print("_"*30)
print("EJEMPLO")
print("_"*30)
print()
def multiplicar(x, y=10):
    print(x * y)
multiplicar(5, 9)
multiplicar(5)

print()
x=int(input("idnque primer valor: "))
y=int(input("idnque segundo valor: "))
def multiplicar(x, y=60):
    print(x)
    print(y)
    print(x * y)
multiplicar(y, x)
multiplicar(15)
