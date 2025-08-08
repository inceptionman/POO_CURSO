Vocales = ["a","e","i","o","u",]
contador_vocales = {}
Texto = input("Ingrese una cadena de texto: ").lower()
Elegir = input("Por cual vocal deseas preguntar: ")
for letra in Texto:
    if letra in Vocales:
        if letra in contador_vocales:
            contador_vocales[letra] += 1
        else:
            contador_vocales[letra] = 1

if Elegir in contador_vocales:
    print(f"La vocal {Elegir} se repitio {contador_vocales[Elegir]}")
else:
    print(f"La vocal '{Elegir}' no se encuentra en el texto.")