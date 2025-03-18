from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta
from Subsubclass.Camioneta import Camioneta
from Subsubclass.Motocicleta import Motocicleta
from Superclass.Vehiculo import Vehiculo

def lanzador_main():
    # Crear ejemplos de los diferentes vehículos
    coche1 = Coche("Rojo", 4, "Gasolina", 150)
    coche2 = Coche("Azul", 4, "Diesel", 180)
    coche3 = Coche("Negro", 4, "Eléctrico", 200)
    coche4 = Coche("Blanco", 4, "Híbrido", 170)
    coche5 = Coche("Gris", 4, "Gasolina", 160)

    bicicleta1 = Bicicleta("lujo", "Montaña", "Verde", "Urbana", 2)
    bicicleta2 = Bicicleta("estándar", "Carretera", "Amarillo", "Deportiva", 2)
    bicicleta3 = Bicicleta("lujo", "Eléctrica", "Negro", "Urbana", 2)
    bicicleta4 = Bicicleta("estándar", "Plegable", "Blanco", "Recreativa", 2)
    bicicleta5 = Bicicleta("lujo", "BMX", "Rojo", "Deportiva", 2)

    camioneta1 = Camioneta("Negro", 4, 200, 1000, "Ford", 2015, 120)
    camioneta2 = Camioneta("Blanco", 4, 250, 1200, "Chevrolet", 2018, 130)
    camioneta3 = Camioneta("Gris", 4, 220, 1100, "Toyota", 2020, 140)
    camioneta4 = Camioneta("Azul", 4, 240, 1300, "Nissan", 2017, 125)
    camioneta5 = Camioneta("Rojo", 4, 210, 1150, "Honda", 2019, 135)

    motocicleta1 = Motocicleta("Blanca", 2, 180, 1000, "Deportiva", "Yamaha", 2015)
    motocicleta2 = Motocicleta("Negra", 2, 200, 1200, "Cruiser", "Harley-Davidson", 2018)
    motocicleta3 = Motocicleta("Roja", 2, 220, 900, "Naked", "Kawasaki", 2020)
    motocicleta4 = Motocicleta("Azul", 2, 190, 1100, "Touring", "BMW", 2017)
    motocicleta5 = Motocicleta("Gris", 2, 210, 950, "Sport", "Ducati", 2019)

    lista = []
    lista.append(coche1)
    lista.append(coche2)
    lista.append(coche3)
    lista.append(coche4)
    lista.append(coche5)
    lista.append(bicicleta1)
    lista.append(bicicleta2)
    lista.append(bicicleta3)
    lista.append(bicicleta4)
    lista.append(bicicleta5)
    lista.append(camioneta1)
    lista.append(camioneta2)
    lista.append(camioneta3)
    lista.append(camioneta4)
    lista.append(camioneta5)
    lista.append(motocicleta1)
    lista.append(motocicleta2)
    lista.append(motocicleta3)
    lista.append(motocicleta4)
    lista.append(motocicleta5)
    # Retornar los vehículos en una lista
    return lista

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = filter(lambda v: getattr(v, 'ruedas', None) == ruedas, vehiculos)
        vehiculos_filtrados = list(vehiculos_filtrados)
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(vehiculo)
    else:
        print("Lista completa de vehículos:")
        for vehiculo in vehiculos:
            print(vehiculo)

# Ejecución de las funciones
lanzador_main()