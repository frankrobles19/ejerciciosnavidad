# 4. Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

# a. Total de números ingresados
# b. Total de números pares ingresados
# c. Promedio de los números pares
# d. Promedio de los números impares
# e. Cuantos números son menores que 10
# f. Cuantos números están entre 20 y 50
# g. Cuantos números son mayores que 100

dictNumeros = {
    "numeros_pares": [],
    "Numeros_Ingresados": [],
    "mayores_10": [],
    "entre_20y50": [],
    "mayores_100": []
}
promedioImpar = []
promedioPar = []

def comparacion(numero):
    dictNumeros["Numeros_Ingresados"].append(numero)

    if numero > 10:
        dictNumeros["mayores_10"].append(numero)

    if 20 < numero < 50:
        dictNumeros["entre_20y50"].append(numero)

    if numero >= 100:
        dictNumeros["mayores_100"].append(numero)
        
    if numero % 2 == 0:
            promedioPar.append(numero)
            dictNumeros["numeros_pares"].append(numero)

    if (numero % 2) != 0:
        promedioImpar.append(numero)
    
nNumero = int(input("Ingrese la cantidad de numeros que quiere comparar: "))
for i in range(nNumero):
    numero = int(input("Ingrese el número natural: "))
    comparacion(numero)

# Imprimir los resultados
print("Numeros ingresados:", dictNumeros["Numeros_Ingresados"])
print("Mayores a 10:", dictNumeros["mayores_10"])
print("Entre 20 y 50:", dictNumeros["entre_20y50"])
print("Mayores o iguales a 100:", dictNumeros["mayores_100"])
print("Numeros pares:", dictNumeros["numeros_pares"])
print("Promedio de impares:", sum(promedioImpar) / len(promedioImpar))
print("Promedio de pares:", sum(promedioPar) / len(promedioPar))


