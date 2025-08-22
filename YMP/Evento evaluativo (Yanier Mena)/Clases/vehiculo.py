# Crear una clase vehículo con 2 hijas, donde mínimo 4 atributos y 3 métodos (1 heredado del padre sin modificar)

class Vehiculo:
    def __init__(self, marca, modelo, color, año, encendido=True):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado")
    
    
    def acelerar(self):
        if not self.encendido:
            print(f"El vehículo está apagado")
            return
        if self.marcha in ["1", "2", "3", "4", "5", "6"]:
            print(f"El vehículo {self.marca} {self.modelo} está acelerando")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no esta en una marcha valida para acelerar")
       
    def reversa(self):
        if not self.encendido:
            print(f"El vehículo esta apagado")
            return
        if self.marcha == "R":
            print(f"El vehículo {self.marca} {self.modelo} está en reversa")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está en reversa o esta acelerando")

class VehiculoManual(Vehiculo):
    def __init__(self, marca, modelo, color, año):
        super().__init__(marca, modelo, color, año)
        self.embriague_pisado = False
    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado")

    def pisar_embriague(self):
        if self.encendido:
            self.embriague_pisado = True
            print("Embrague pisado")

    def soltar_embriague(self):
        if self.encendido:
            self.embriague_pisado = False
            print("Embrague soltado")

    def cambiar_marcha(self, nueva_marcha):
        if not self.encendido:
            print("El vehículo debe estar encendido para cambiar de marcha")
            return
        if not self.embriague_pisado:
            print("No puedes cambiar de marcha sin pisar el embrague")
            return
        if nueva_marcha not in ["1", "2", "3", "4", "5", "6"]:
            print("El vehiculo no es manual")
            return
        self.marcha = nueva_marcha
        print(f"Marcha cambiada a {self.marcha}.")

class VehiculoAutomatico(Vehiculo):
    def __init__(self, marca, modelo, color, año):
        super().__init__(marca, modelo, color, año)
        self.modo = "P"  # Parking por defecto
    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado")

    def cambiar_modo(self, nuevo_modo):
        if not self.encendido:
            print("El vehículo debe estar encendido para cambiar de modo")
            return
        if nuevo_modo not in ["P", "R", "N", "D"]:
            print("El vehiculo no es automatico")
            return
        self.modo = nuevo_modo
        print(f"Modo cambiado a {self.modo}.")


# Vehículo manual
auto1 = VehiculoManual("\bToyota", "Corolla", "Rojo", 2000)
auto1.encender()
auto1.pisar_embriague()
auto1.cambiar_marcha("4")
auto1.soltar_embriague()

# Vehículo automático
auto2 = VehiculoAutomatico("\nHonda", "Civic", "Azul", 2021)
auto2.encender()
auto2.cambiar_modo("D")