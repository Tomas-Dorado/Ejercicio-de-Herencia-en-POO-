from Subclass.Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc, Tipo: {self.tipo}"

