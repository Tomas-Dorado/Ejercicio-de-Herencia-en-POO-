from Superclass.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}"