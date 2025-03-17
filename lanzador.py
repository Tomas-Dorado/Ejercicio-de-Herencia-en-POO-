from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta
from Subsubclass.Camioneta import Camioneta
from Subsubclass.Motocicleta import Motocicleta

def lanzadera_main():
    # Crear ejemplos de los diferentes vehículos
    coche = Coche("Rojo", 4, "Gasolina", 150)
    bicicleta = Bicicleta("lujo", "Montaña","Azul","Urbana",2)
    camioneta = Camioneta("Negro", 4, 200, 1000, "Haudi", 1990, 98)
    motocicleta = Motocicleta("Blanca", 2, 180,1000, "Deportiva", "linux", 1999)
    
    # Retornar los vehículos en una lista
    return [coche, bicicleta, camioneta, motocicleta]

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if hasattr(vehiculo, 'ruedas') and vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(vehiculo)
    else:
        for vehiculo in vehiculos:
            print(vehiculo)

# Ejecución de las funciones
vehiculos = lanzadera_main()
catalogar(vehiculos, 2)