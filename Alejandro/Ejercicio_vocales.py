def contar_vocales(cadena):
    # Definimos las vocales
    vocales = 'aeiouAEIOU'
    # Creamos un diccionario para contar las vocales
    contador = {vocal: 0 for vocal in vocales}
    
    # Contamos las vocales en la cadena
    for letra in cadena:
        if letra in contador:
            contador[letra] += 1
            
    return contador
# Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Ingresa una cadena: ")
resultado = contar_vocales(cadena_usuario)

# Mostrar el conteo de vocales
print("Conteo de vocales:", resultado)

# Preguntar al usuario por una vocal específica
vocal_a_preguntar = input("¿Qué vocal deseas consultar? (a, e, i, o, u): ")

# Mostrar cuántas veces se repitió la vocal
if vocal_a_preguntar in resultado:
    print(f"La vocal '{vocal_a_preguntar}' se repitió {resultado[vocal_a_preguntar]} veces.")
else:
    print("La vocal ingresada no es válida.")