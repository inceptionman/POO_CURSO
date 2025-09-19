# Aplicar los coknceptos de POO (Abstraccion, encapsulamiento, herencia y polimorfismo)

# Metodo de ordenamiento burbuja

lista = [5, 2, 9, 1, 5, 6]

def burbuja(lista):
    tamano = len(lista)
    for i in range(tamano):
        for j in range(0, tamano-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# Metodo de ordenamiento por seleccion

def seleccion(lista):
    tamano = len(lista)
    for i in range(tamano):
        min_idx = i
        for j in range(i+1, tamano):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Metodo de ordenamiento por insercion

def insercion(lista):
    tamano = len(lista)
    for i in range(1, tamano):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista
    
# Metodo de ordenamiento por mezcla (Merge Sort)

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

# Metodo de ordenamiento rapido (Quick Sort)

lista2 = [10,4, 23, 2, 45, 1, 67, 34]

def quicksort(lista2):
    base = len(lista2)
    if base <= 1:
        return lista2
    pivote = lista2.pop()
    lista_izquierda = []
    lista_derecha = []
    
    for i in lista2:
        if i <= pivote:
            lista_izquierda.append(i)
        else:
            lista_derecha.append(i)
    
    print(f"Lista original: {lista2}, Pivote: {pivote}, Izquierda: {lista_izquierda}, Derecha: {lista_derecha}")

    lista_izquierda = quicksort(lista_izquierda)
    lista_derecha = quicksort(lista_derecha)
    print(quicksort(lista2))

    # Metodo de ordenamiento por conteo (Counting Sort)
lista = [2, 7, 4, 1, 3, 6]
def counting_sort(lista):
    auxiliar = [0 for i in range(10)]
    resultado = [0 for i in range(len(lista))]

    for i in lista:
        auxiliar[i] += 1
    print(auxiliar)

    for i in range (1, 8):
        auxiliar[i] += auxiliar[i-1]
    print(auxiliar)

    for i in range(len(lista)):
        resultado[auxiliar[lista[i]] - 1] = lista[i]
        auxiliar[lista[i]] -= 1
    return resultado

print(counting_sort(lista))

# Tarea: CONSUMIR UNA API Y ORDENAR SEGUN LOS CRITERIOS YA VISTOS EN CLASE