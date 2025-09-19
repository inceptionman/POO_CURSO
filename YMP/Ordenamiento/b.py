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
    return lista_izquierda + [pivote] + lista_derecha
print(quicksort(lista2))