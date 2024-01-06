el ejercicio de registrar sismos en la ciudades se basa en como el titulo lo indica registrar los sismos en la ciudad correspodiente, mediante dos inputs que son nombre de ciudad y magnitud del sismo, los alamacena y luego accerdemos a ellos para clasificarlos por categoria de colores segun su magnutud de al mas fuete al mas suave, la explicacion de lo usa y como se estructura el codido:

Módulo registros.py:
Función registrar_sismo(ciudades, nombre_ciudad, magnitud):
Propósito: Registra sismos en la lista de ciudades.
Entrada:
ciudades: Lista que contiene información de las ciudades.
nombre_ciudad: Nombre de la ciudad donde se registrará el sismo.
magnitud: Magnitud del sismo a registrar.

Salida: Imprime mensajes sobre el registro del sismo y actualiza la información de la ciudad.
Función calcular_promedio_sismos(sismos):
Propósito: Calcula el promedio de magnitudes de sismos.
Entrada: Lista de magnitudes de sismos.
Salida: Promedio de magnitudes o 0 si no hay sismos registrados.


Módulo main.py:
Función menu_principal(ciudades):
Propósito: Presenta un menú interactivo al usuario para registrar ciudades, sismos, buscar sismos por ciudad, generar informes de riesgo y salir del programa.
Entrada: Lista ciudades que almacena información sobre las ciudades.
Salida: Interacción con el usuario y actualización de la información según las opciones seleccionadas.

Cómo Usar el Programa:
Registro de Ciudades:

Selecciona la opción 1 para registrar una nueva ciudad con su nombre y la cantidad de sismos a registrar.
Registro de Sismos:

Selecciona la opción 2 para registrar un sismo en una ciudad específica con su magnitud.
Buscar Sismos por Ciudad:

Selecciona la opción 3 para ver la lista de sismos registrados en una ciudad.
Informe de Riesgo:

Selecciona la opción 4 para obtener un informe de riesgo de cada ciudad basado en el promedio de las magnitudes de los sismos.
Salir del Programa:

Selecciona la opción 5 para salir del programa.