from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta
from Subsubclass.Camioneta import Camioneta

coche1 = Coche("Rojo", 4, 180, 1600)
bicicleta1 = Bicicleta("Azul", 2, "Urbana")
camioneta1 = Camioneta("Blanco", 4, 160, 2500, 1000)

print(bicicleta1.__str__())
print(camioneta1.__str__())


