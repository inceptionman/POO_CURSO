class Animal:
    # método constructor
    def __init__(self, nombre, edad, especie, vivo=True):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.vivo = True
    
    def comer(self):
        print(f"{self.nombre} está comiendo.")
    
    def caminar(self):
        if self.vivo:
            print(f"{self.nombre} está caminando.")
        else:
            print(f"{self.nombre} no puede caminar porque no está vivo.")
    
class invertebrados(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad, especie)
        self.especie = especie
    def comer(self):
        print(f"{self.nombre} está comiendo.")
    
    def caminar(self):
        if self.vivo:
            print(f"{self.nombre} se esta arrastrando.")
        else:
            print(f"{self.nombre} no se puede arrastrar porque no está vivo.")

class vertebrados(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad, especie)
        self.especie = especie
    def comer(self):
        print(f"{self.nombre} está comiendo.")
    
    def caminar(self):
        if self.vivo:
            print(f"{self.nombre} se esta arrastrando.")
        else:
            print(f"{self.nombre} no se puede arrastrar porque no está vivo.")


animalito = invertebrados("Luna", 3, "Lombriz")
animalito.vivo = False
animalote = vertebrados("Don Cangrejo", 2, "Cangrejo")
animalote.vivo = True
print(animalito.vivo)
print(animalote.vivo)
animalito.comer()
animalote.comer()
animalito.caminar()
animalote.caminar()
'''
animalito2 = Animal(input(f"Nombre del animal: "), int(input("Edad del animal: ")), input("Especie del animal: "))
print(f"Nombre: {animalito2.nombre}, Edad: {animalito2.edad}, Especie: {animalito2.especie}")
animalote = Animal("Sharon", 35, "Elefante")
animalito.vivo = False
print(animalito.vivo)
print(animalote.edad)
animalito.comer()
animalito2.comer()
animalito.caminar()
animalito2.caminar()
'''



    