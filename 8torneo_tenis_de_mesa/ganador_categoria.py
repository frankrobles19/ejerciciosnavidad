from registrarJugador import jugadores_novatos,jugadores_intermedios, jugadores_expertos
import json
def print_anuncio_novatos():
    print("""
       +++++++++++++++++++++++++++++++++++++++++
       ++  GANADORES POR CATEGORIA (NOVATOS)  ++
       +++++++++++++++++++++++++++++++++++++++++
      """)
    
def print_anuncio_intermedios():
    print("""
       ++++++++++++++++++++++++++++++++++++++++++++
       ++  GANADORES POR CATEGORIA (INTERMEDIOS) ++
       ++++++++++++++++++++++++++++++++++++++++++++
      """)
    
def print_anuncio_avanzados():
    print("""
       ++++++++++++++++++++++++++++++++++++++++++++
       ++  GANADORES POR CATEGORIA (AVANZADOS )  ++
       ++++++++++++++++++++++++++++++++++++++++++++
      """)  
      
def ganador_Novatos():
    print_anuncio_novatos()
    global max_valor, diccionarios_maximos
    max_valor = max(jugadores_novatos, key=lambda x: x['puntos'])
    # Utiliza una lista de comprensión para obtener todos los diccionarios con el valor máximo
    diccionarios_maximos = [d for d in jugadores_novatos if d['puntos'] == max_valor['puntos']]
    print("el ganador es:")
    if len(diccionarios_maximos) == len(diccionarios_maximos):
        max_PA_Jugadores = max(jugadores_novatos, key=lambda x: x['PA'])
        print(json.dumps(max_PA_Jugadores, indent=2))
    elif diccionarios_maximos:
        print(json.dumps( max_valor['nombre'], max_valor,indent=2 ))

def ganador_intermedio():
    print_anuncio_intermedios()
    global max_valor, diccionarios_maximos
    max_valor = max(jugadores_intermedios, key=lambda x: x['puntos'])
    # Utiliza una lista de comprensión para obtener todos los diccionarios con el valor máximo
    diccionarios_maximos = [d for d in jugadores_intermedios if d['puntos'] == max_valor['puntos']]
    print("el ganador es:")
    if len(diccionarios_maximos) == len(diccionarios_maximos):
        max_PA_Jugadores = max(jugadores_intermedios, key=lambda x: x['PA'])
        print(json.dumps(max_PA_Jugadores, indent=2))
    elif diccionarios_maximos:
        print(json.dumps( max_valor['nombre'], max_valor,indent=2 ))


def ganador_experto():
    print_anuncio_avanzados()
    global max_valor, diccionarios_maximos
    max_valor = max(jugadores_expertos, key=lambda x: x['puntos'])
    # Utiliza una lista de comprensión para obtener todos los diccionarios con el valor máximo
    diccionarios_maximos = [d for d in jugadores_expertos if d['puntos'] == max_valor['puntos']]
    print("el ganador es:")
    if len(diccionarios_maximos) == len(diccionarios_maximos):
        max_PA_Jugadores = max(jugadores_expertos, key=lambda x: x['PA'])
        print(json.dumps(max_PA_Jugadores, indent=2))
    elif diccionarios_maximos:
        print(json.dumps( max_valor['nombre'], max_valor,indent=2 ))