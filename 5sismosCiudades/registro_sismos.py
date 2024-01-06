def registrar_sismo(ciudades, nombre_ciudad, magnitud):
    for ciudad in ciudades:
        if ciudad["nombre"] == nombre_ciudad:
            if len(ciudad["sismos"]) < ciudad["cantidad_sismos"]:
                ciudad["sismos"].append(magnitud)
                print(f"Sismo registrado en {nombre_ciudad}: Magnitud {magnitud}")
            else:
                print(f"Ya se registraron {ciudad['cantidad_sismos']} sismos en {nombre_ciudad}")
            return
    print("Ciudad no encontrada.")


def calcular_promedio_sismos(sismos):
    return sum(sismos) / len(sismos) if sismos else 0
