from Superclass.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tipo, ruedas):
        super().__init__(color, ruedas)
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}"