def tabla_del(numero):
    resultados = []
    for i in range(11):
        resultados.append(numero * i)
    return resultados
res = tabla_del(3)
print(res)

print()
def jose():
    num=int(input("que producto compraste 1)leche 2)pan 3)alcohol 4)otros; "))
    total=int(input("cuanto costo S/.? : "))
    if num==1:
        im=10
    elif num==2:
        im=20
    elif num==3:
        im=30
    else:
        im=50
    impu=(total*im/100)
    print('impuesto de ese producto es S/.: ',impu)
# print(impu)
    return impu
jose()
print("Programa terminado")

print()
def pago_mensual():
    grado=int(input("En que grado esta el niño: 1)primero 2)segundo 3)tercero 4)cuarto 5)quinto 6)sexto; "))
    if grado==1:
        pago=400
    elif grado==2:
        pago=450
    elif grado==3:
        pago=500
    elif grado==4:
        pago=450
    elif grado==5:
        pago=500
    else:
        pago=550
    impu=(pago*5/100)
    mensualidad=(pago+impu)
    print("el impuesto seria:", impu)
    print('la mensulidad es de: S/.',mensualidad)
    return mensualidad
pago_mensual()
print("Programa terminado")
