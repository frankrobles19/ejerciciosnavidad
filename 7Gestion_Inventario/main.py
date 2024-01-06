from registros import agregar_producto, ver_productos, actualizar_producto, minimo_limite, ganancia


def menu():
    print("1. registro de producto")
    print("2. visualizacion de productos")
    print("3. actualizacion del stock")
    print("4. informe de productos criticos")
    print("5. calculo de ganancia potencial")
    print("6. SALIR")

def main():
    bandera = True
    while(bandera):
        menu()
        opmenu = int(input("ingrese una opcion del menu"))
        if (opmenu == 1):
            agregar_producto()
        elif(opmenu == 2):
            ver_productos()
        elif(opmenu == 3):
            actualizar_producto()
        elif(opmenu == 4):
            minimo_limite()  
        elif(opmenu == 5):
            ganancia()
        elif(opmenu == 6):
            break

         




if __name__ == "__main__":
    main()