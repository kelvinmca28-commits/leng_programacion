def sumar(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
#resultado=resultado+numer
    print(resultado)
sumar([4,5]) # 9
sumar([2,3,1])# 6

print()
def sumar(**numeros):
 print(numeros)
 print(numeros['numero1'] + numeros['numero2'])
sumar(numero1=10, numero2=20) # 30
sumar(numero1=4, numero2=11) # 15

print()
print("_"*30)
print("EJEMPLO")
print("_"*30)
print()
print()
def restar(**numeros):
 print(numeros)
 print(numeros['numero1'] - numeros['numero2'] - numeros["numero3"])
restar(numero1=70, numero2=20, numero3=10)
restar(numero1=50, numero2=11, numero3=8)
