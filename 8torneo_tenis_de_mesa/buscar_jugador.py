from registrarJugador import jugadores_novatos, jugadores_intermedios, jugadores_expertos, limpiar_consola
import json

def submenu():
    print("1. NOVATO")
    print("2. NIVEL INTERMEDIO")
    print("3. NIVEL AVANZADO")


def Ver_registro_Jugador():
    limpiar_consola()
    submenu()
    try: 
        opmenu = int(input("ingrese la categoria para buscar jugador :)_"))
    except ValueError:
        print("ERROR!!!, por favor ingresa una opcion valida")
    else:
        if opmenu == 1:
            try:
                opcion = int(input("ingrese un numero de ID del jugador para ver registro :)_"))
            except ValueError:
                print("ERROR!!! Por favor Ingrese el Numero de Identificacion Correcto ")
            else:
                for i in jugadores_novatos:
                    if opcion == i['id_del_jugador'] :
                        print("REGISTRO FINAL")    
                        print(json.dumps(i,indent=2))
                    else:
                        print("ERROR! ese id no existe!!")    
        elif opmenu == 2:
            try:
                opcion = int(input("ingrese un numero de ID del jugador para ver registro :)_"))
            except ValueError:
                print("ERROR!!! Por favor Ingrese el Numero de Identificacion Correcto ")
            else:
                for i in jugadores_intermedios:
                    if opcion == i['id_del_jugador'] :
                        print("REGISTRO FINAL")    
                        print(json.dumps(i,indent=2))
                    else:
                        print("ERROR! ese id no existe!!")        
        elif opmenu == 3:
            try:
                opcion = int(input("ingrese un numero de ID del jugador para ver registro :)_"))
            except ValueError:
                    print("ERROR!!! Por favor Ingrese el Numero de Identificacion Correcto ")
            else:
                for i in jugadores_expertos:
                    if opcion == i['id_del_jugador'] :
                        print("REGISTRO FINAL")    
                        print(json.dumps(i,indent=2))
                    else:
                        print("ERROR! ese id no existe!!")         
        

    