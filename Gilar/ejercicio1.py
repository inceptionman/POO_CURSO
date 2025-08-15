# Definir las dimensiones de la matriz
# Pedir al usuario las dimensiones de la matriz
filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

# Paso 2: Crear la matriz con los índices
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append((i, j))  # cada celda contiene (fila, columna)
    matriz.append(fila)

# Paso 3: Mostrar la matriz antes de dar el orden 
print("\nMatriz original con índices:")
for fila in matriz:
    for celda in fila:
        print(celda, end=" ")
    print()  # salto de línea por cada fila

# Paso 4: Mostrar los índices en forma horizontal alternando dirección de izq a der y de der a izq
print("\nÍndices en forma horizontal:")
for i in range(filas):
    if i % 2 == 0:
        # Fila par: izquierda a derecha para seguir el orden 
        for j in range(columnas):
            print(matriz[i][j], end=" ")
    else:
        # Fila impar: derecha a izquierda para organizar mejor
        for j in range(columnas - 1, -1, -1):
            print(matriz[i][j], end=" ")
print()  # salto de línea final
