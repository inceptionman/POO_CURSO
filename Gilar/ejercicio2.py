import random

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para colocar elementos aleatorios en el tablero
def colocar_elemento(tablero, simbolo):
    while True:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = simbolo
            break

# Función principal del juego
def jugar():
    print("🎮 ¡Bienvenido al juego de la Búsqueda del Tesoro!")
    print("Tu misión es encontrar el tesoro escondido en el tablero.")
    print("Pero cuidado... hay trampas que pueden terminar el juego 💣")

    # Crear tablero vacío
    tablero = [["-" for _ in range(5)] for _ in range(5)]

    # Colocar tesoro y trampas
    colocar_elemento(tablero, "T")
    for _ in range(3):
        colocar_elemento(tablero, "X")

    intentos = 5
    while intentos > 0:
        print(f"\nTe quedan {intentos} intentos.")
        try:
            fila = int(input("Ingresa la fila (0-4): "))
            columna = int(input("Ingresa la columna (0-4): "))
        except ValueError:
            print("❌ Solo puedes ingresar números del 0 al 4.")
            continue

        if fila < 0 or fila > 4 or columna < 0 or columna > 4:
            print("❌ Coordenadas fuera del tablero. Intenta de nuevo.")
            continue

        if tablero[fila][columna] == "T":
            print("🎉 ¡Felicidades! Encontraste el tesoro.")
            break
        elif tablero[fila][columna] == "X":
            print("💥 ¡Oh no! Caíste en una trampa. Fin del juego.")
            break
        else:
            print("😕 No encontraste nada.")
            intentos -= 1

    if intentos == 0:
        print("😢 Se acabaron tus intentos. No encontraste el tesoro.")

    print("\nEste era el tablero:")
    mostrar_tablero(tablero)

# Bucle para repetir el juego
while True:
    jugar()
    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta != "s":
        print("👋 Gracias por jugar. ¡Hasta la próxima!")
        break