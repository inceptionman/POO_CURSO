import random

tablero = [["-" for cuadro in range(5)] for cuadro in range(5)]

# Ubicar el tesoro
fila_aleatoria= random.randint(0, 4)
columna_aleatoria = random.randint(0, 4)
tablero[fila_aleatoria][columna_aleatoria] = "T"

# Colocar trampas
trampas_colocadas = 0
while trampas_colocadas < 3:
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = "X"
        trampas_colocadas += 1

# Juego de adivinanza de tesoro
MINIMO = 0
MAXIMO = 5
print("Bienvenido al juego del tesoro\nEl tesoro está escondido en un tablero de 5x5\nTienes que adivinar la ubicación del tesoro en un maximo de 5 intentos\nSi caes en una trampa, perderás el juego")
buscar_tesoro = True
intentos = int(input("¿Cuantos intentos quieres? (máximo 10): "))
contador = 1
while buscar_tesoro and contador < intentos:
    fila = int(input(f"Ingrese la fila (1-{MAXIMO}): ")) - 1
    columna = int(input(f"Ingrese la columna (1-{MAXIMO}): ")) - 1
    if fila < MINIMO or fila >= MAXIMO or columna < MINIMO or columna >= MAXIMO:
        print("Coordenadas inválidas. Intente de nuevo.")
        continue
    
    print(f"tus coordenadas son: "f"({fila + 1}, {columna + 1})")
    if tablero[fila][columna] == "T":
        print("Felicidades, Has encontrado el tesoro.")
        buscar_tesoro = False
    elif tablero[fila][columna] == "X":
        print("Has caído en una trampa. Juego terminado.")
        buscar_tesoro = False
    else:
        print(f"No hay tesoro ni trampa en esa ubicación. Tienes {intentos - contador} intentos restantes.")
    contador+= 1

for fila in tablero:
 print(" ".join(fila))
if buscar_tesoro:
    print("Juego terminado. No encontraste el tesoro.")





