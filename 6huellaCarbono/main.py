from registros import agregarOficina, calculo_luz, calculo_dispositivos, calculo_transporte , ver_co2, mayor_co2
def menu ():
    print("\n Menu")
    print("1. registrar nombre de la oficina")
    print("2. registrar dependencia")
    print("3. ver CO2 producido")
    print("4. dependencia que produce mayor CO2")
    print("5. SALIR")

def submenu ():
   print("1. dependecia luz") 
   print("2. dependecia transporte") 
   print("3. dependecia dispositivos") 
   
oficina = []

def main ():
    
    while True:    
        menu()    
        opmenu = int(input("ingrese una opcion del menu: "))
        if opmenu == 1:
            agregarOficina()
        elif opmenu == 2:
            try:
                submenu()
                opmenu = int(input("ingrese opcion"))
                if opmenu == 1:
                    calculo_luz()
                elif opmenu == 2:
                    calculo_transporte()
                elif opmenu == 3:
                    calculo_dispositivos()
            except:
               ("error con los datos ingresados no son acorde a lo pedido")
        elif opmenu == 3:
           ver_co2()
        elif opmenu == 4:
            mayor_co2()
        elif opmenu == 5:
            print("adios!")
            break           






if __name__ == "__main__":
    main()
               
