n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

# Construir una matriz de n filas y m columnas
construir_matriz = [[(i * m) + j + 1 for j in range(m)] for i in range(n)]

# Mostrar los índices de la matriz
print("Los índices de la matriz son: ")
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(f"({i},{j})", end=' ')
    else:
        for j in reversed(range(m)):
            print(f"({i},{j})", end=' ')

        