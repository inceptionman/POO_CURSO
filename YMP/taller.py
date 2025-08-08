Vocales = ["a","e","i","o","u"]
contador_vocales = {}
Texto = input('Ingresa una cadena de texto: ').lower()
vocal = input("Cual es la vocal por la que deseas preguntar? ").lower()
for letra in Texto:
    if letra in Vocales:
        if letra in contador_vocales:
            contador_vocales[letra] += 1
        else:
            contador_vocales[letra] = 1

if vocal in contador_vocales:
    print(f"La vocal '{vocal}' se repitió {contador_vocales[vocal]} veces.")
else:
    print(f"La vocal '{vocal}' no aparece en el texto.")

