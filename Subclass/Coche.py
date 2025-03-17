from Superclass.Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self,color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.cilindrada = cilindrada
        self.velocidad = velocidad
    
    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc"