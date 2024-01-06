import os
from registrarJugador import jugadores_intermedios, jugadores_expertos, jugadores_novatos, limpiar_consola
from juego_novatos import validar_datos_novatos
from juego_intermedio import validar_datos_intermedio
from juego_avanzados import validar_datos_avanzado

def submenu2():
    print("1. NOVATO")
    print("2. NIVEL INTERMEDIO")
    print("3. NIVEL AVANZADO")

def empezarJuego():
    try:
        print("""
            ++++++++++++++++++++++++++++++
            ++     REGISTRO DEL JUEGO   ++
            ++++++++++++++++++++++++++++++  
              """)
        submenu2()
        opmenuCategory = int(input("¿que categoria va a empezar el juego? :)_"))
        limpiar_consola()
    except ValueError:
        print("ERROR,!ingrese solo numeros enteros!")
    else:

        if opmenuCategory == 1:
                if  len(jugadores_novatos) >= 2: #son 5 jugadores como minimo pero uso 2 para probar el programa mas rapido
                        validar_datos_novatos()
                else:
                    print("los jugadores no son sufucientes")
                    print("! MINIMO 5 JUGADORES!")
        elif opmenuCategory == 2:
                if  len(jugadores_intermedios) >= 2: #son 5 jugadores como minimo pero uso 2 para probar el programa mas rapido
                      validar_datos_intermedio()
                else:
                    print("los jugadores no son sufucientes")
                    print("! MINIMO 5 JUGADORES!")
        elif opmenuCategory == 3:
                if  len(jugadores_expertos) >= 2:#son 5 jugadores como minimo pero uso 2 para probar el programa mas rapido
                      validar_datos_avanzado
                else:
                    print("los jugadores no son sufucientes")
                    print("! MINIMO 5 JUGADORES!")
