from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta
from Subsubclass.Camioneta import Camioneta
from Subsubclass.Motocicleta import Motocicleta
from lanzador import lanzador_main

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Crear Coche")
    print("2. Crear Bicicleta")
    print("3. Crear Camioneta")
    print("4. Crear Motocicleta")
    print("5. Ordenas por tipo de ruedas")
    print("6. Salir")


def obtener_datos_vehiculo(opcion):
    if opcion == 1:
        color = input("Ingrese el color del coche: ")
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        ruedas = int(input("Ingrese el número de ruedas: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))

        return Coche(color, ruedas, velocidad, cilindrada)
    elif opcion == 2:
        marca = input("Ingrese la marca de la bicicleta: ")
        modelo = input("Ingrese el modelo de la bicicleta: ")
        color = input("Ingrese el color de la bicicleta: ")
        tipo = input("Ingrese el tipo de bicicleta (montaña, carretera, etc.): ")
        return Bicicleta(marca, modelo, color, tipo, ruedas=2)
    elif opcion == 3:
        color = input("Ingrese el color de la camioneta: ")
        ruedas = int(input("Ingrese el número de ruedas: "))
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        marca = input("Ingrese la marca de la camioneta: ")
        modelo = input("Ingrese el modelo de la camioneta: ")
        capacidad_carga = float(input("Ingrese la capacidad de carga en toneladas: "))
        return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga)
    elif opcion == 4:
        color = input("Ingrese el color de la motocicleta: ")
        ruedas = int(input("Ingrese el número de ruedas: "))
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        tipo = input("Ingrese el tipo de motocicleta (deportiva, scooter, etc.): ")
        marca = input("Ingrese la marca de la motocicleta: ")
        modelo = input("Ingrese el modelo de la motocicleta: ")
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        return Motocicleta(color, ruedas,velocidad, cilindrada, tipo, marca, modelo)
    elif opcion == 5:
        lanzador_main().catalogar(vehiculos)
        def catalogar(vehiculos, ruedas=None):
            if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for vehiculo in vehiculos_filtrados:
                print(f"{type(vehiculo).__name__}: {vehiculo.ruedas} ruedas")
            else:
            for vehiculo in vehiculos:
                print(f"{type(vehiculo).__name__}: {vehiculo.ruedas} ruedas")

    else:
        return None


if __name__ == "__main__":
	while True:
		mostrar_menu()
		opcion = int(input("Seleccione una opción: "))
		if opcion == 6:
			break
		vehiculo = obtener_datos_vehiculo(opcion)
		if vehiculo:
			print(f"Vehículo creado: {vehiculo}")
		else:
			print("Opción no válida, intente de nuevo.")
	lanzador_main()



