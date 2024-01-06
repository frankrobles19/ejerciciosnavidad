# 3. Teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudiantes y poder determinar
# el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:}

# a. Cuantos estudiantes se encuentran en el peso ideal.
# b. Cuantos estudiantes se encuentran en obesidad grado I
# c. Cuantos estudiantes se encuentran en obesidad grado II
# d. Cuantos estudiantes se encuentran en obesidad grado III
# e. Cuantos estudiantes se encuentran en Sobrepeso


def IMC(imc):
    if 18.5 < imc < 24.9:
        return "Normal"
    elif 25.9 < imc < 29.9:
        return "Sobrepeso"
    elif 30 < imc < 34.9:
        return "Obesidad grado 1"
    elif 35 < imc < 39.9:
        return "Obesidad grado 2"
    elif imc > 40:
        return "Obesidad grado 3"

lista_estudiantes = []

estudiantes = 2


for i in range(estudiantes):
    dic_estudiante = {
        "nombre": '',
        "edad": '',
        "imc": 0
    }
    print(f"ESTUDIANTE {i + 1} DE {estudiantes}")
    nombre = input("Ingrese su nombre: ")
    dic_estudiante["nombre"] = nombre
    edad = input("Ingrese su edad: ")
    dic_estudiante["edad"] = edad
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kg: "))
    imc = (peso / altura)**2
    resultado_imc = IMC(imc)
    dic_estudiante["imc"] = resultado_imc

    lista_estudiantes.append(dic_estudiante)

print(lista_estudiantes)

normal = sobrepeso = obesidad_1 = obesidad_2 = obesidad_3 = 0

for estudiante in lista_estudiantes:
    categoria_imc = estudiante["imc"]
    if categoria_imc == "Normal":
        normal += 1
    elif categoria_imc == "Sobrepeso":
        sobrepeso += 1
    elif categoria_imc == "Obesidad grado 1":
        obesidad_1 += 1    
    elif categoria_imc == "Obesidad grado 2":
        obesidad_2 += 1
    elif categoria_imc == "Obesidad grado 3":
        obesidad_3 += 1

print(f"Normal: {normal} estudiantes")
print(f"Sobrepeso: {sobrepeso} estudiantes")
print(f"Obesidad grado 1: {obesidad_1} estudiantes")
print(f"Obesidad grado 2: {obesidad_2} estudiantes")
print(f"Obesidad grado 3: {obesidad_3} estudiantes")
