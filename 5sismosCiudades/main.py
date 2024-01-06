
from registro_sismos import registrar_sismo, calcular_promedio_sismos

def menu_principal(ciudades):
    global cantidad_sismos
    while True:
        print("\n----- Menú -----")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            cantidad_sismos = int(input("Ingrese la cantidad de sismos a registrar por ciudad: "))
            ciudades.append({"nombre": nombre_ciudad, "cantidad_sismos": cantidad_sismos, "sismos": []})
            print(f"Ciudad {nombre_ciudad} registrada exitosamente.")

        elif opcion == "2":
            if not ciudades:
                print("Primero registre al menos una ciudad.")
            else:
                nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
                magnitud_sismo = float(input("Ingrese la magnitud del sismo: "))
                registrar_sismo(ciudades, nombre_ciudad, magnitud_sismo)

        elif opcion == "3":
            if not ciudades:
                print("Primero registre al menos una ciudad.")
            else:
                nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
                for ciudad in ciudades:
                    if ciudad["nombre"] == nombre_ciudad:
                        print(f"Sismos registrados en {nombre_ciudad}: {ciudad['sismos']}")
                        break
                else:
                    print("Ciudad no encontrada.")

        elif opcion == "4":
            if not ciudades:
                print("Primero registre al menos una ciudad.")
            else:
                for ciudad in ciudades:
                    promedio = calcular_promedio_sismos(ciudad["sismos"])
                    if promedio < 2.5:
                        print(f"{ciudad['nombre']}: Amarillo (Sin riesgo)")
                    elif 2.5 <= promedio <= 4.5:
                        print(f"{ciudad['nombre']}: Naranja (Riesgo medio)")
                    else:
                        print(f"{ciudad['nombre']}: Rojo (Riesgo alto)")

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    ciudades = []
    menu_principal(ciudades)
