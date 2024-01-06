import os
jugadores_novatos = []
jugadores_intermedios = []
jugadores_expertos = []

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def submenu():
    print("1. NOVATO (15 a 16 años)")
    print("2. NIVEL INTERMEDIO (17 a 20 años)")
    print("3. NIVEL AVANZADO (20 en adelante)")



def categorias():
    global edadCategorias
    try:
        limpiar_consola()
        print("LAS CATEGORIAS SE ASIGNAN SEGUN LA EDAD")
        submenu()
        edadCategorias = int(input("Ingrese su edad :)_ "))
    except ValueError:
        print("Por favor, ingrese un número.")
    else:
        if 15 <= edadCategorias <= 16:
            category_registration_novices()
        elif 17 <= edadCategorias <= 20:
            category_registration_intermediate()
        elif edadCategorias >= 20:
            category_registration_expert()
        else:
            print("Con esa edad no puedes jugar.")
            limpiar_consola()

def category_registration_novices(): 
        nombre = input("Ingrese su nombre:)_ ")
        id_jugador = int(input("Ingrese su número de identificación :)_ "))
        jugadores_novatos.append({'nombre': nombre, 'edad': edadCategorias, 'id_del_jugador': id_jugador, 'PJ' : 0, 'PG' : 0, 'PP' : 0, 'PA' : 0,'TP' : 0, 'puntos' : 0})
        limpiar_consola()

def category_registration_intermediate():
    nombre = input("Ingrese su nombre :)_ ")
    id_jugador = int(input("Ingrese su número de identificación :)_ "))
    jugadores_intermedios.append({'nombre': nombre, 'edad': edadCategorias, 'id_del_jugador': id_jugador,'PJ' : 0, 'PG' : 0, 'PP' : 0, 'PA' : 0, 'TP' : 0, 'puntos' : 0})
    limpiar_consola()
def category_registration_expert():
    nombre = input("Ingrese su nombre :)_")
    id_jugador = int(input("Ingrese su número de identificación :)_"))
    jugadores_expertos.append({'nombre': nombre, 'edad': edadCategorias, 'id_del_jugador': id_jugador,'PJ' : 0, 'PG' : 0, 'PP' : 0, 'PA' : 0, 'TP' : 0, 'puntos' : 0})
    limpiar_consola()


