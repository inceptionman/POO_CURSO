#Contador de vocales: Contar cuantas vocales tiene una cadena ingresada por el usuario, almacenando en un diccionario y pudiendo 
# escoger después que tanto se repitió alguna vocal. El usuario ingresa la información y pregunta el número de veces que se repitió.

# Función para contar vocales en una cadena
def contar_vocales(texto):
    texto = texto.lower()
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto:
        if letra in vocales:
            vocales[letra] += 1
    return vocales

# Bucle principal para que puedas ingresar varias frases
while True:
    #Pedir una frase o palabra al usuario
    texto = input("\nIngresa una frase o palabra: ")

    # Contar las vocales
    resultado = contar_vocales(texto)

    # Mostrar el conteo de vocales
    print("\nConteo de vocales:")
    for vocal, cantidad in resultado.items():
        print(f"{vocal}: {cantidad}")

    # Para consultar una vocal específica
    consulta = input("\n¿Quieres saber cuántas veces se repitió una vocal? Ingresa la vocal: ").lower() #para evitar errores de mayúsculas y tildes
    if consulta in resultado:
        print(f"La vocal '{consulta}' se repitió {resultado[consulta]} veces.")
    else:
        print("Eso no es una vocal válida.")

    # Preguntar si quiere ingresar otra frase o terminar
    continuar = input("\n¿Quieres ingresar otra frase o palabra? (sí/no): ").lower() #para evitar errores de mayúsculas y tildes
    if continuar != "sí":
        print("Gracias por usar el programa. ATT: Gilar")
        break
