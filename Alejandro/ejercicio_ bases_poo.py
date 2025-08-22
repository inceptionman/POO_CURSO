class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Color: {self.color}"

    def encender(self):
        return "El vehículo está encendido."

    def apagar(self):
        return "El vehículo está apagado."


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, color, puertas):
        super().__init__(marca, modelo, año, color)
        self.puertas = puertas

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Puertas: {self.puertas}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, color, tipo):
        super().__init__(marca, modelo, año, color)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Tipo: {self.tipo}"


# Ejemplo de uso
coche = Coche("Toyota", "Corolla", 2020, "Rojo", 4)
motocicleta = Motocicleta("Yamaha", "MT-07", 2021, "Negro", "Deportiva")

print(coche.mostrar_info())
print(coche.encender())
print(motocicleta.mostrar_info())
print(motocicleta.apagar())
