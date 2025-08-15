import random

def crear_tablero():
    """Crea un tablero de 5x5 lleno de guiones (-)."""
    return [['-' for _ in range(5)] for _ in range(5)]

def posicionar_elementos(tablero):
    """Coloca un tesoro (T) y tres trampas (X) en posiciones aleatorias del tablero."""
    # Colocar el tesoro
    fila_tesoro = random.randint(0, 4)
    col_tesoro = random.randint(0, 4)
    tablero[fila_tesoro][col_tesoro] = 'T'

    # Colocar trampas
    trampas_colocadas = 0
    while trampas_colocadas < 3:
        fila_trampa = random.randint(0, 4)
        col_trampa = random.randint(0, 4)
        # Asegurarse de que no se superponga con el tesoro o con otra trampa
        if tablero[fila_trampa][col_trampa] == '-':
            tablero[fila_trampa][col_trampa] = 'X'
            trampas_colocadas += 1

def mostrar_tablero_juego(tablero, revelar_todo=False):
    """Muestra el tablero en la consola, ocultando T y X si no es el final."""
    for fila in tablero:
        fila_mostrada = []
        for celda in fila:
            if revelar_todo:
                fila_mostrada.append(celda)
            else:
                fila_mostrada.append(celda if celda in ['O', 'X', 'T'] else '-')
        print(' '.join(fila_mostrada))

def ingresar_numero(mensaje, minimo=1):
    """Función para ingresar números con validación."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= minimo:
                return numero
            print(f"El número debe ser mayor o igual a {minimo}. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def jugar():
    """Función principal del juego."""
    # Creamos dos tableros: uno real y otro que ve el jugador
    tablero_real = crear_tablero()
    tablero_visible = crear_tablero()
    posicionar_elementos(tablero_real)

    print("\n" + "="*50)
    print(" BUSQUEDA DEL TESORO ".center(50))
    print("="*50)
    
    # Configuración inicial
    max_intentos = ingresar_numero("\n¿Cuántos intentos deseas tener? (mínimo 1): ")
    intentos = max_intentos
    encontrado = False

    print(f"\nTienes {max_intentos} intentos para encontrar el tesoro.")
    print("Cuidado con las trampas!")
    
    while intentos > 0 and not encontrado:
        print(f"\nIntentos restantes: {intentos}")
        print("Tablero actual (O = casillas ya exploradas):")
        mostrar_tablero_juego(tablero_visible)

        # Solicitar coordenadas al usuario
        try:
            print("\nIngresa coordenadas entre 0 y 4")
            fila = int(input("Fila (0-4): "))
            col = int(input("Columna (0-4): "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        # Verificar coordenadas
        if fila < 0 or fila > 4 or col < 0 or col > 4:
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue

        # Verificar contenido en el tablero REAL
        if tablero_real[fila][col] == 'T':
            tablero_visible[fila][col] = 'T'
            print("\n¡Felicidades! ¡Has encontrado el tesoro!")
            encontrado = True
        elif tablero_real[fila][col] == 'X':
            tablero_visible[fila][col] = 'X'
            print("\n¡Oh no! Has pisado una trampa. ¡Juego terminado!")
            encontrado = True
        elif tablero_visible[fila][col] == 'O':
            print("\nYa exploraste esta casilla antes. Pierdes un intento.")
            intentos -= 1
        else:
            print("\nNo encontraste nada en esta casilla.")
            tablero_visible[fila][col] = 'O'
            intentos -= 1

    # Fin del juego
    if not encontrado:
        print("\nSe te han acabado los intentos. ¡Juego terminado!")
    
    print("\nTablero final revelado:")
    mostrar_tablero_juego(tablero_real, revelar_todo=True)

# Iniciar el juego
if __name__ == "__main__":
    jugar()

