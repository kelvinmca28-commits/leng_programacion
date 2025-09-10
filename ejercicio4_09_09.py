def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)
cuadrado_de_par(8)
cuadrado_de_par(3)
print()


def cuadrado_de_inpar(numero):
    if not numero % 2 != 0:
        return
    else:
        print(numero ** 2)
cuadrado_de_inpar(9)
cuadrado_de_inpar(12)


print()
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(2))
print(es_par(5))
