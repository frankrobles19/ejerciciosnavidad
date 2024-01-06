
from registrarJugador import categorias
from validar_categoria import empezarJuego
from buscar_jugador import Ver_registro_Jugador
from ganador_categoria import ganador_intermedio,ganador_experto,ganador_Novatos
import os



def menu():
    print("1. registrarse en una categoria")
    print("2. registrar juego")
    print("3. ver registro del jugador")
    print("4. ver ganador por categoria")
    print("5. SALIR")

def submenu():
    print("1. NOVATO")
    print("2. NIVEL INTERMEDIO")
    print("3. NIVEL AVANZADO")


def main ():  
    while True:    
        try:
            menu()    
            opmenu = int(input("ingrese una opcion del menu :)_ "))
        except ValueError:
            print("ingrese solo numeros")
        else:        
            if opmenu == 1:
                categorias()   
            elif opmenu == 2:
                empezarJuego()
            elif opmenu == 3:
                Ver_registro_Jugador()
            elif opmenu == 4:
                ganador_Novatos()
                ganador_intermedio()
                ganador_experto()
            elif opmenu == 5:
                print("adios!")
                break           




if __name__ == "__main__":
    main()