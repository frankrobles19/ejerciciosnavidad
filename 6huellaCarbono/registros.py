# emision kwh por hora = 0.5
# valor de la unidad de kwh es de = 374.24
# (recibo de luz/ unidad de kwh) * emicion por hora 0.5

dic_oficinas = {
    "oficinas" : []
}

def agregarOficina():
    nombre_oficina = input("ingrese el nombre de la oficina: ")
    dic_oficinas["oficinas"].append({'oficina': nombre_oficina, 'valor_CO2' : {'luz' : [],  'transporte' : [],
    'dispositivos' : [] }}) 
    print(f"la oficina {nombre_oficina} se registro con exito")



def calculo_luz():
    try:
        oficina = input("Ingrese el nombre de la oficina a registrar: ")
        for buscarOfi in dic_oficinas["oficinas"]: 
            if buscarOfi['oficina'] == oficina:
                oficina_encontrada = buscarOfi
                calcularLuz = float(input("ingrese el valor de su recibo en el mes: "))
                calculoLuz = ((calcularLuz/374.24)*0.5)
                oficina_encontrada['valor_CO2']['luz'].append(calculoLuz) 
                break        
            else:
                print("oficina no encontrada!")
    except: ValueError
    
        
def calculo_transporte():
    try:
        oficina = input("Ingrese el nombre de la oficina a registrar:  ")
        for buscarOfi in dic_oficinas["oficinas"]: 
            if buscarOfi['oficina'] == oficina:
                oficina_encontrada = buscarOfi
                transporte = int(input("ingrese los kilometros recorridos del trabajo a su casa: "))
                calculo_transporte = (transporte*2.3)
                oficina_encontrada['valor_CO2']['transporte'].append(calculo_transporte) 
                break        
            else:
                print("oficina no encontrada!")
    except: ValueError
    
        
       
        
def calculo_dispositivos():
    try:
        oficina = input("Ingrese el nombre de la oficina a registrar:  ")
        for buscarOfi in dic_oficinas["oficinas"]: 
            if buscarOfi['oficina'] == oficina:
                oficina_encontrada = buscarOfi
                dispositivos_tiempo = int(input("ingrese el tiempo en horas usando dispositivos, ejemplo: (8), solo el numero: "))
                potencia_dispositivos = int(input("ingrese la potencia del dispositivo "))
                calculo_dispositivos = ((potencia_dispositivos*dispositivos_tiempo) / 1000)
                oficina_encontrada['valor_CO2']['dispositivos'].append(calculo_dispositivos) 
                break        
            else:
                print("oficina no encontrada!")
    except: ValueError

       
def ver_co2():
    try:
        oficina = input("Ingresa el nombre de la oficina para ver sus emisiones CO2: ")
        for buscarOfi in dic_oficinas["oficinas"]:
            if buscarOfi['oficina'] == oficina:
                oficinaEncontrada = buscarOfi
                if oficinaEncontrada:
                    print(f"la oficina: {oficina}")
                    print(f"su valor de CO2: {oficinaEncontrada['valor_CO2']}") 
    except: ValueError            


def mayor_co2():
    try:
        oficina = input("Ingresa el nombre de la oficina para ver mayor CO2 de una dependencia: ")
        for buscarOfi in dic_oficinas["oficinas"]:
            if buscarOfi['oficina'] == oficina:
                oficinaEncontrada = buscarOfi
                if oficinaEncontrada:
                    print(f"la oficina: {oficina}")
                    print(f"tiene una mayor produccion de CO2 :{(max(oficinaEncontrada['valor_CO2']))}")
    except: ValueError            

