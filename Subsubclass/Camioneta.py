from Subclass.Coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc, Carga: {self.carga} Kg"