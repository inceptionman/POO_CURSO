def recorrido_zigzag_matriz(n, m):
    """
    Genera los índices de una matriz n×m con recorrido zigzag:
    - Filas pares (0, 2, 4...): izquierda → derecha
    - Filas impares (1, 3, 5...): derecha → izquierda
    """
    indices = []
    
    for i in range(n):
        if i % 2 == 0:
            # Fila par: izquierda a derecha
            for j in range(m):
                indices.append((i, j))
        else:
            # Fila impar: derecha a izquierda
            for j in range(m-1, -1, -1):
                indices.append((i, j))
    
    return indices

# Función para validar entrada numérica
def ingresar_dimension(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("¡Error! Debe ser un número mayor que 0.")
            else:
                return valor
        except ValueError:
            print("¡Error! Ingresa un número entero válido.")

# Interfaz de usuario
print("\n" + "="*50)
print(" GENERADOR DE RECORRIDO ZIGZAG EN MATRIZ".center(50))
print("="*50)

# Ingreso de dimensiones
print("\nIngresa las dimensiones de la matriz:")
n = ingresar_dimension("  - Número de filas (n): ")
m = ingresar_dimension("  - Número de columnas (m): ")

# Generar y mostrar resultado
indices = recorrido_zigzag_matriz(n, m)
print("\n" + " RESULTADO ".center(50, "="))
print(f"\nMatriz {n}x{m} - Recorrido Zigzag ({n*m} elementos):\n")

# Mostrar indices con formato
for i, (fila, col) in enumerate(indices, 1):
    # Resaltar dirección
    if fila % 2 == 0:
        direccion = "→"
    else:
        direccion = "←"
    
    print(f" {i:2d}. ({fila},{col}) {direccion}")
    
# Representación visual simple
print("\nRepresentación visual:")
for i in range(n):
    row = []
    for j in range(m):
        pos = indices.index((i, j)) + 1
        row.append(f"({i},{j}):{pos}")
    
    # Alinear según dirección
    if i % 2 != 0:
        row.reverse()
    
    print(" " + " ".join(row))