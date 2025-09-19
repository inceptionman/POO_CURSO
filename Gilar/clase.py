#Crear una clase vehículo con 2 hijas, donde mínimo 4 atributos y 3 métodos (1 heredado del padre sin modificar)
# Clase Padre
class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_maxima = velocidad_maxima

    # Método heredado sin modificar
    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} ha sido encendido.")

    # Método que las hijas pueden redefinir
    def mover(self):
        print(f"El vehículo {self.marca} {self.modelo} se está moviendo.")

    def detener(self):
        print(f"El vehículo {self.marca} {self.modelo} se ha detenido.")


# Clase Hija 1
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, puertas):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.puertas = puertas

    def mover(self):
        print(f"El coche {self.marca} {self.modelo} está conduciendo por la carretera.")


# Clase Hija 2
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, tipo):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.tipo = tipo   # ej: deportiva, scooter

    def mover(self):
        print(f"La moto {self.marca} {self.modelo} está rodando sobre dos ruedas.")


coche1 = Coche("Toyota", "Corolla", "Rojo", 180, 4)
moto1 = Moto("Yamaha", "R15", "Azul", 150, "deportiva")

coche1.encender()
moto1.encender()
coche1.mover()
moto1.mover()
coche1.detener()
moto1.detener()
