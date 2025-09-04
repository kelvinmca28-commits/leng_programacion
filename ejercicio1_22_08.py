# Ejemplos de operaciones
tupla = (1, 2, 3, 2, 4)
print(tupla.count(2)) # Output: 2
print(tupla.index(3)) # Output: 2
print((1, 2) + (3, 4)) # Output: (1, 2, 3, 4)
print(('a',) * 3) # Output: ('a', 'a', 'a')

print()
# Representación de coordenadas geográficas
punto = (40.7128, -74.0060) # Nueva York
def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    # Cálculo de distancia (implementación simplificada)
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
ny = (40.7128, -74.0060)
la = (34.0522, -118.2437)
distancia = calcular_distancia(ny, la)
