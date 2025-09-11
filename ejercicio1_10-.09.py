def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3
cuad, cubo = cuadrado_y_cubo(4)
print(cuad)
print(cubo)

print()
def exponentes(numero):
    return numero ** 3, numero ** 5, numero ** 9
x=int(input("Indique el numero a conciderar: "))
cubo,quinta,novena = exponentes(x)
print("Al cubo:", cubo)
print("A la quinta:", quinta)
print("A la novena:", novena)

print()
def exponentes(numero,a,b,c):
    return numero ** a, numero ** b, numero ** c
x=int(input("Indique el numero a conciderar: "))
a=int(input("primer exponente: "))
b=int(input("segundo exponente: "))
c=int(input("tercer exponente: "))
prim,seg,ter = exponentes(x,a,b,c)
print("elevado a:", a, "sale:", prim)
print("elevado a:", b, "sale:", seg)
print("elevado a:", c, "sale:", ter)
