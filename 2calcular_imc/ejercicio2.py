# 2. El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los
# Estudiantes nuevos.

# El programa debe mostrar el nombre del estudiante, la edad, el imc y la categoría según el IMC obtenido
# Ver Imagen suministrada.

def IMC (imc):
    if 18.5 < imc <= 24.9:
        return("normal")
    elif 25.9 < imc <= 29.9:
        return("obesidad")
    elif 30 < imc <= 34.9:
        return("obesiadad 1")
    elif 35 < imc <= 39.9:
        return("obesidad tipo 2")
    elif imc > 40:
        return("obesidad tipo 3")

nombre = input("ingrese su nombre")
edad = input("ingrese su edad")
altura = float(input("ingrese su altura en metros"))
peso = float(input("ingrese su peso en kg"))
imc = (peso / altura)**2
resultado_imc = IMC(imc)
print(f"el estudiante {nombre} con edad de {edad}, tinee un IMC de {resultado_imc}")