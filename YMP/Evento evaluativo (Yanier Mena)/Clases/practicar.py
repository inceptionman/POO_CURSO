construir_matriz = ["Hola", "Mundo"]

# Mostrar la matriz
for fila in construir_matriz:
    print(" ".join(map(str, fila)))

for fila in construir_matriz:
    print("-".join(str(elemento) for elemento in fila))

for fila in construir_matriz:
    print(str(fila))
    
"""

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

# Construir una matriz de n filas y m columnas
construir_matriz = [[(i * m) + j + 1  for j in range(m)] for i in range(n)]

for fila in construir_matriz:
    print(" ".join(map(str, fila)))

print("Los índices de la matriz son: ")
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(f"({i},{j})", end=' ')
    else:
        for j in reversed(range(m)):
            print(f"({i},{j})", end=' ')
"""