#Variables in Python
edad = 25
precio = 19.99
nombre = "Juan"
confirmacion = True
respuesta = None

#print(type(edad))
#print(type(precio))
#print(type(nombre))
#print(type(confirmacion))
#print(type(respuesta))
#Con el None no se reserva memoria

lista = [1, "2", 4, 5]
print(lista)
print(type(lista[2]))
lista[2] = 3
lista.append(6)
lista.insert(3, 7)
lista.remove(7)
lista.pop(0)  # Elimina el primer elemento
print(lista)

tupla = (1, 2, 3, 4, 5)
print(type(tupla))
#tupla [0] = 6

persona = {
    "nombre": "Juan",
    "edad": 25,
    "altura": 1.75,
    "casado": False,
    "hijos": None
}

print(persona["edad"])

matrices = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrices[1][2])  # Accede al elemento en la segunda fila,
print(type(matrices))