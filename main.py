from Subclass.Coche import Coche
from Subclass.Bicicleta import Bicicleta
from Subsubclass.Camioneta import Camioneta
from Subsubclass.Motocicleta import Motocicleta
from lanzador import lanzadera_main

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Crear Coche")
    print("2. Crear Bicicleta")
    print("3. Crear Camioneta")
    print("4. Crear Motocicleta")
    print("5. Salir")


def obtener_datos_vehiculo(opcion):
    if opcion == 1:
        color = input("Ingrese el color del coche: ")
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        ruedas = int(input("Ingrese el número de ruedas: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))

        return lanzadera_main(Coche(color, ruedas, velocidad, cilindrada))
    elif opcion == 2:
        marca = input("Ingrese la marca de la bicicleta: ")
        modelo = input("Ingrese el modelo de la bicicleta: ")
        color = input("Ingrese el color de la bicicleta: ")
        tipo = input("Ingrese el tipo de bicicleta (montaña, carretera, etc.): ")
        return lanzadera_main(Bicicleta(marca, modelo, color, tipo, ruedas=2))
    elif opcion == 3:
        color = input("Ingrese el color de la camioneta: ")
        ruedas = int(input("Ingrese el número de ruedas: "))
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        marca = input("Ingrese la marca de la camioneta: ")
        modelo = input("Ingrese el modelo de la camioneta: ")
        capacidad_carga = float(input("Ingrese la capacidad de carga en toneladas: "))
        return lanzadera_main(Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga))
    elif opcion == 4:
        color = input("Ingrese el color de la motocicleta: ")
        ruedas = int(input("Ingrese el número de ruedas: "))
        velocidad = int(input("Ingrese la velocidad máxima en km/h: "))
        tipo = input("Ingrese el tipo de motocicleta (deportiva, scooter, etc.): ")
        marca = input("Ingrese la marca de la motocicleta: ")
        modelo = input("Ingrese el modelo de la motocicleta: ")
        cilindrada = int(input("Ingrese la cilindrada en cc: "))
        return lanzadera_main(Motocicleta(color, ruedas,velocidad, cilindrada, tipo, marca, modelo))
    else:
        return None


if __name__ == "__main__":
	while True:
		mostrar_menu()
		opcion = int(input("Seleccione una opción: "))
		if opcion == 5:
			break
		vehiculo = obtener_datos_vehiculo(opcion)
		if vehiculo:
			print(f"Vehículo creado: {vehiculo}")
		else:
			print("Opción no válida, intente de nuevo.")
	lanzadera_main()



