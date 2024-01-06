from registrarJugador import jugadores_expertos, limpiar_consola
jugar_sets = 2
def validar_datos_avanzado():
    limpiar_consola()
    global nomJ1, nomJ2
    jugador1_encontrado = False
    
    nomJ1 = input("Ingrese el nombre del jugador 1:)_ ")
    jugador1 = int(input("Ingrese el código ID del jugador 1:)_"))

    for jugadorBuscar in jugadores_expertos:
        if nomJ1 == jugadorBuscar['nombre'] and jugador1 == jugadorBuscar['id_del_jugador']:
            jugador1_encontrado = True
            break  # Sale del bucle después de encontrar al jugador 1

    if not jugador1_encontrado:
        print("Jugador 1 no encontrado en la lista.")
        return  # Termina la función si el jugador 1 no se encuentra

    nomJ2 = input("Ingrese el nombre del jugador 2:)_ ")
    jugador2 = int(input("Ingrese el código ID del jugador 2:)_ "))

    for jugadorBuscar1 in jugadores_expertos:
        if nomJ2 == jugadorBuscar1['nombre'] and jugador2 == jugadorBuscar1['id_del_jugador']:
            juego_intermedio()
            break  # Sale del bucle después de encontrar al jugador 2
    else:
        print("Jugador 2 no encontrado en la lista.")
                   
                    
def juego_intermedio():
    limpiar_consola()
    print("¡Condiciones cumplidas para ambos jugadores!")
    print(f"""
            ++++++++++++++++++++++++++++++++++
            ++  {nomJ1} VS JUGADOR {nomJ2}  ++
            ++++++++++++++++++++++++++++++++++
        """)
    print(" ++++++++ SON DOS SETS LOS QUE SE JUGARÁN ++++++++")
    for i in range(jugar_sets):
        print(f" +++++++    --INICIA EL {i +1}/{jugar_sets} SET--     +++++++")
        set1jugador1 = int(input(f"ingrese cuantos puntos tubo el jugador 1 {nomJ1} :)_"))
        set1jugador2 = int(input(f"ingrese cuantos puntos tubo el jugador 2 {nomJ2} :)_"))
        if (set1jugador1 > set1jugador2):
            pts_fa1 = (set1jugador1 - set1jugador2)
            for jugador in jugadores_expertos:  
                if jugador['nombre'] == nomJ1:       
                    jugador['PJ'] += 1
                    jugador['PG'] += 1
                    jugador['PA'] += pts_fa1
                    jugador['TP'] += set1jugador1
                    jugador['PP'] += 0
                    jugador['puntos'] += 2 

            for jugadorPerdedor in jugadores_expertos:
                if jugadorPerdedor['nombre'] == nomJ2:
                    jugadorPerdedor['PJ'] += 1
                    jugadorPerdedor['PG'] += 0
                    jugadorPerdedor['TP'] += set1jugador2
                    jugadorPerdedor['PP'] += 1

        elif (set1jugador1 < set1jugador2):
            for jugador1 in jugadores_expertos:
                if jugador1['nombre'] == nomJ2:      
                    pts_fa1 = (set1jugador1 - set1jugador2)
                    jugador1['PG'] += 1
                    jugador1['PJ'] += 1
                    jugador1['PA'] += pts_fa1
                    jugador1['TP'] += set1jugador2
                    jugador1['PP'] += 0 
                    jugador1['puntos'] += 2 


            for jugadorPerdedor1 in jugadores_expertos:
                if jugadorPerdedor1['nombre'] == nomJ1:
                    jugadorPerdedor1['PJ'] += 1
                    jugadorPerdedor1['PG'] += 0
                    jugadorPerdedor1['PP'] += 1                                         
               