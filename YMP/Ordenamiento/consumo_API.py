import requests
import pandas as pd
import json
from pandas import json_normalize

link = "https://www.datos.gov.co/api/v3/views/rgxm-mmea/query.json"
peticion = requests.get(link)
print(peticion)
pokemones = json.loads(peticion.text)
print(pokemones)
# Peticiones http(s) tienen estados:
# 1xx: Información
# 2xx: Éxito
# 3xx: Redirección
# 4xx: Error del cliente
# 5xx: Error del servidor

def burbuja(lista):
    tamano = len(lista)
    for i in range(tamano):
        for j in range(0, tamano-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

