from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta

coche1 = Coche("Rojo", 4, 180, 1600)
bicicleta1 = Bicicleta("Azul", 2, 30, 0)

print(coche1.__str__())
print(bicicleta1.__str__())


