from Superclass.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc"