import requests
import time
from typing import List, Dict, Any, Callable, Type, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Base Sorter Class
class BaseSorter(ABC):
    """Método abstracto que deben implementar las subclases.
        Ordena los datos según la clave especificada."""
    
    @abstractmethod
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        """Ordena los datos según la clave especificada."""
        pass
    
    def _compare(self, a: Any, b: Any, reverse: bool) -> bool:
        """Método auxiliar para comparar dos valores según el orden de clasificación."""
        if isinstance(a, str) and isinstance(b, str):
            return a.lower() > b.lower() if not reverse else a.lower() < b.lower()
        return a > b if not reverse else a < b

# IMPLEMENTACIONES DE ALGORITMOS DE ORDENAMIENTO

# Bubble Sort
class BubbleSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        data = data.copy()
        n = len(data)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self._compare(data[j][key], data[j + 1][key], reverse):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped: 
                break
        return data
# Selection Sort
class SelectionSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        data = data.copy()
        n = len(data)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self._compare(data[min_idx][key], data[j][key], not reverse):
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

# Insertion Sort
class InsertionSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        data = data.copy()
        
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and self._compare(data[j][key], key_item[key], reverse):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item
        return data

# Merge Sort
class MergeSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if len(data) <= 1:
            return data.copy()
            
        mid = len(data) // 2
        left = self.sort(data[:mid], key, reverse)
        right = self.sort(data[mid:], key, reverse)
        
        return self._merge(left, right, key, reverse)

    def _merge(self, left: List[Dict], right: List[Dict], key: str, reverse: bool) -> List[Dict]:
        """Función auxiliar que combina dos listas ordenadas."""   
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if not self._compare(left[i][key], right[j][key], reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# Quick Sort
class QuickSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if len(data) <= 1:
            return data.copy()
            
        pivot = data[len(data) // 2][key]
        left = [x for x in data if self._compare(pivot, x[key], not reverse)]
        middle = [x for x in data if x[key] == pivot]
        right = [x for x in data if self._compare(x[key], pivot, not reverse)]
        
        return self.sort(left, key, reverse) + middle + self.sort(right, key, reverse)

# Counting Sort
class CountingSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        # Validar que los valores sean numéricos
        if not all(isinstance(d[key], int) for d in data):
            raise ValueError("Counting sort can only be used with integer values")

        # Determinar el valor máximo y mínimo de la clave 
        max_val = max(d[key] for d in data)
        min_val = min(d[key] for d in data)

        # Crea un arreglo de conteo (frecuencia) y un arreglo de salida (resiltado)
        count = [0] * (max_val - min_val + 1)
        output = [None] * len(data)
        
        # Contar la frecuencia de cada valor
        for item in data:
            count[item[key] - min_val] += 1
            
        # Modificar el arreglo de conteo para que contenga las posiciones finales
        total = 0
        for i in range(len(count)):
            count[i], total = total, count[i] + total

        # Construir el arreglo de salida con los elementos ordenados    
        for item in data:
            output[count[item[key] - min_val]] = item
            count[item[key] - min_val] += 1
            
        return output if not reverse else output[::-1]

# Radix Sort (usando Counting Sort)
class RadixSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        if not all(isinstance(d[key], int) for d in data):
            raise ValueError("Radix sort can only be used with integer values")
        
        # Encontrar el número máximo para saber cuantos digitos tiene
        max_num = max(d[key] for d in data)
        exp = 1 # Exponente para el dígito actual
        
        while max_num // exp > 0:
            data = self._counting_sort(data, key, exp, reverse)
            exp *= 10 # Incrementar al siguiente dígito
            
        return data
    # Método auxiliar: Counting Sort a un digito especifico 
    def _counting_sort(self, data: List[Dict], key: str, exp: int, reverse: bool) -> List[Dict]:
        n = len(data)
        output = [None] * n
        count = [0] * 10
        
        # Contar la frecuencia de cada dígito 
        for item in data:
            index = (item[key] // exp) % 10
            count[index] += 1
        
        # Modificar el arreglo de conteo para que contenga las posiciones finales
        for i in range(1, 10):
            count[i] += count[i - 1]
            
        # Construir el arreglo de salida
        i = n - 1
        while i >= 0:
            index = (data[i][key] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1
            i -= 1
            
        return output if not reverse else output[::-1]

# Heap Sort
class HeapSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
            
        data = data.copy()
        n = len(data)
        
        # Contuir el monticulo (heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(data, n, i, key, reverse)
            
        # Extraer elementos del monticulo uno por uno
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i] # Mover la raiz al final
            self._heapify(data, i, 0, key, reverse)
            
        return data if not reverse else data[::-1]
    
    # Método auxiliar para mantener la propiedad del monticulo
    def _heapify(self, data: List[Dict], n: int, i: int, key: str, reverse: bool) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Verificar si el hijo izquierdo es mayor que la raiz
        if left < n and self._compare(data[largest][key], data[left][key], reverse):
            largest = left
        
        # Verificar si el hijo derecho es mayor que la raiz
        if right < n and self._compare(data[largest][key], data[right][key], reverse):
            largest = right
        
        # Cambiar la raiz si es necesario
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self._heapify(data, n, largest, key, reverse)

# Bucket Sort
class BucketSort(BaseSorter):
    def sort(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        if not data:
            return []
        
        # Validar que los valores sean numéricos
        if not all(isinstance(d[key], (int, float)) for d in data):
            raise ValueError("Bucket sort can only be used with numeric values")
           
        min_val = min(d[key] for d in data)
        max_val = max(d[key] for d in data)
        
        # Manejar el caso donde todos los valores son iguales
        if min_val == max_val:
            return data.copy()
        
        # Crear buckets tantas como elementos haya en la lista
        bucket_count = len(data)
        buckets = [[] for _ in range(bucket_count)]
        
        # Distribuir los elementos en los buckets
        for item in data:
            index = int(((item[key] - min_val) / (max_val - min_val)) * (bucket_count - 1))
            buckets[index].append(item)
            
        # Ordenar cada bucket y concatenar los resultados mediante el Insertion Sort
        sorted_buckets = []
        for bucket in buckets:
            if bucket:
                insertion_sorter = InsertionSort()
                sorted_bucket = insertion_sorter.sort(bucket, key, reverse)
                sorted_buckets.append(sorted_bucket)
        result = []
        for bucket in (sorted_buckets if not reverse else reversed(sorted_buckets)):
            result.extend(bucket if not reverse else reversed(bucket))
            
        return result if not reverse else result

# API CLIENT
class PokeAPIClient:
    """Cliente para obtener datos de Pokemon de la PokeAPI."""
    
    BASE_URL = "https://pokeapi.co/api/v2"
    
    def __init__(self):
        self.session = requests.Session()
    
    def get_pokemon_list(self, limit: int = 20) -> List[Dict]:
        """
        Obtiene una lista de pokemon con detalles basicos hasta el limite especificado
        Hace varias llamadas a la API para obtener detalles de cada pokemon 
        y devuelve una lista de diccionarios con los datos relevantes
        """
        try:
            url = f"{self.BASE_URL}/pokemon?limit={limit}"
            response = self.session.get(url)
            response.raise_for_status()
            
            results = response.json().get('results', [])
            pokemon_list = []
            
            # Obtener detalles de cada pokemon
            for item in results:
                pokemon_data = self.session.get(item['url']).json()
                pokemon = {
                    'id': pokemon_data['id'],
                    'name': pokemon_data['name'],
                    'height': pokemon_data['height'],
                    'weight': pokemon_data['weight'],
                    'base_experience': pokemon_data.get('base_experience', 0)
                }
                pokemon_list.append(pokemon)
                
            return pokemon_list
            
        except requests.RequestException as e:
            print(f"Error al obtener datos de Pokemon: {e}")
            return []

# APLICACION PRINCIPAL
class PokemonSorterApp:
    """Clase principal de la aplicación de ordenamiento de pokemon."""
    
    def __init__(self):
        self.api_client = PokeAPIClient()
        self.sorters = {
            '1': ('Ordenamiento de Burbuja', BubbleSort()),
            '2': ('Ordenamiento por Selección', SelectionSort()),
            '3': ('Ordenamiento por Inserción', InsertionSort()),
            '4': ('Ordenamiento por Mezcla', MergeSort()),
            '5': ('Ordenamiento Rápido', QuickSort()),
            '6': ('Ordenamiento por Conteo', CountingSort()),
            '7': ('Ordenamiento Radix', RadixSort()),
            '8': ('Ordenamiento por Montículo', HeapSort()),
            '9': ('Ordenamiento por Cubetas', BucketSort())
        }
        self.data = [] # Datos de pokemon obtenidos de la API
    
    def run(self):
        """Ejecuta el bucle principal de la aplicación."""
        print("=== Ordenador de Pokémon ===\n")
        self._fetch_data()
        
        while True:
            if not self.data:
                break
                
            print("\n=== Menú Principal ===")
            print("1. Cambiar cantidad de Pokémon (actual: {})".format(len(self.data)))
            print("2. Ordenar Pokémon")
            print("3. Mostrar datos actuales")
            print("4. Salir")
            
            choice = input("\nIngrese su opción (1-4): ").strip()
            
            if choice == '1':
                self._change_limit()
            elif choice == '2':
                self._sort_menu()
            elif choice == '3':
                self._display_data()
            elif choice == '4':
                print("\n¡Gracias por usar el Ordenador de Pokémon!")
                break
            else:
                print("\nOpción inválida. Por favor, intente nuevamente.")
    
    def _fetch_data(self, limit: int = 10):
        """Obtiene datos de Pokémon de la API."""
        print("\nObteniendo datos de Pokémon...")
        self.data = self.api_client.get_pokemon_list(limit=limit)
        if not self.data:
            print("Error al obtener los datos. Por favor, verifique su conexión a internet e intente nuevamente.")
            return
        
        print(f"\nSe obtuvieron {len(self.data)} Pokémon:")
        self._display_data()
    
    def _change_limit(self):
        """Cambia la cantidad de Pokémon a mostrar."""
        try:
            limit = int(input("\nIngrese el número de Pokémon a mostrar (1-50): "))
            if 1 <= limit <= 50:
                self._fetch_data(limit=limit)
            else:
                print("Por favor ingrese un número entre 1 y 50.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
    
    def _sort_menu(self):
        """Muestra las opciones de ordenamiento y maneja la selección del usuario."""
        print("\nAlgoritmos de ordenamiento disponibles:")
        for num, (name, _) in sorted(self.sorters.items()):
            print(f"{num}. {name}")
        
        algo_choice = input("\nSeleccione un algoritmo de ordenamiento (1-9): ").strip()
        if algo_choice not in self.sorters:
            print("Selección inválida.")
            return
        
        print("\nCriterios de ordenamiento disponibles:")
        print("1. ID")
        print("2. Nombre")
        print("3. Altura")
        print("4. Peso")
        print("5. Experiencia Base")
        
        key_map = {
            '1': 'id',
            '2': 'name',
            '3': 'height',
            '4': 'weight',
            '5': 'base_experience'
        }
        
        key_choice = input("\nSeleccione un criterio de ordenamiento (1-5): ").strip()
        if key_choice not in key_map:
            print("Selección de criterio inválida.")
            return
        
        sort_key = key_map[key_choice]
        reverse_choice = input("¿Ordenar en orden descendente? (s/n): ").strip().lower()
        reverse = reverse_choice == 's'
        
        sorter_name, sorter = self.sorters[algo_choice]
        print(f"\nOrdenando por {sort_key} ({"descendente" if reverse else "ascendente"}) usando {sorter_name}...")
        
        try:
            start_time = time.time()
            sorted_data = sorter.sort(self.data, sort_key, reverse)
            end_time = time.time()
            
            if sorted_data is not None:
                self.data = sorted_data
                print(f"\nOrdenamiento completado en {end_time - start_time:.6f} segundos")
                self._display_data()
            else:
                print("Error en el ordenamiento.")
                
        except Exception as e:
            print(f"\nError durante el ordenamiento: {str(e)}")
    
    def _display_data(self):
        """Muestra los datos actuales de Pokémon en formato tabla"""
        if not self.data:
            print("No hay datos para mostrar.")
            return
            
        # Definir encabezados y anchos de columna
        headers = ["ID", "Nombre", "Altura", "Peso", "Exp. Base"]
        col_widths = [5, 15, 8, 8, 10]
        
        # Imprimir encabezado
        header_row = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        print("\n" + "-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))
        
        # Imprimir Data rows
        for pokemon in self.data:
            row = [
                str(pokemon['id']),
                pokemon['name'].capitalize(),
                str(pokemon['height']),
                str(pokemon['weight']),
                str(pokemon['base_experience'])
            ]
            row_str = " | ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths))
            print(row_str)
        
        print("-" * len(header_row))
        print(f"Total de Pokémon: {len(self.data)}\n")

# EJECUCION DE LA APLICACION
if __name__ == "__main__":
    try:
        app = PokemonSorterApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
