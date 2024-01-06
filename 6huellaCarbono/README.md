este programa ayuda a calcular el co2 producido por los diferentes medios como lo son los dispositivos, transporte, luz et..., en este programa solo se tienen en cuenta esas tres opciones como entradas, las cuales para calcular el co2 producido por cada una de ellas no se piden directamente una cantidad que el usuario no sepa como interpretar o calcular, ejemplo en la entrada para calcular el co2 de la luz se pide el a cuanto le llego el recibo de la luz y luego se hace unas conversiones de cantidades para obtener el dato correto para luego poder hacer los procesos y imprimir las salidas, 

una descripcion mas detallada de como se conforma el codigo:

Módulo main.py:

Funciones:
menu():
Propósito: Presenta un menú de opciones principal.
Opciones:
Registrar nombre de la oficina.
Registrar dependencia.
Ver CO2 producido.
Dependencia que produce mayor CO2.
Salir.

submenu():
Propósito: Presenta un submenú de opciones para registrar dependencias.
Opciones:
Dependencia luz.
Dependencia transporte.
Dependencia dispositivos.

main():
Propósito: Controla el flujo principal del programa.
Opciones:
Registro de oficinas y dependencias.
Cálculos de emisiones de CO2.
Visualización de emisiones y dependencia con mayor CO2.

Cómo Usar el Programa:
Registro de Oficinas y Dependencias:
Selecciona las opciones del menú para registrar oficinas y dependencias asociadas.

Cálculos de Emisiones de CO2:
Utiliza las opciones del menú para calcular las emisiones de CO2 asociadas a distintas dependencias.

Visualización de Emisiones y Dependencia con Mayor CO2:
Utiliza las opciones del menú para ver las emisiones de CO2 de una oficina específica y la dependencia que produce mayor CO2.

Salir del Programa:
Selecciona la opción de salir cuando hayas terminado.

Módulo registros.py:

Funciones:
agregarOficina():
Propósito: Registra una nueva oficina junto con su nombre y las dependencias asociadas.
Entrada: Nombre de la oficina.
Salida: Actualiza la lista de oficinas con la nueva entrada.

calculo_luz():
Propósito: Calcula las emisiones de CO2 asociadas al consumo de luz en una oficina.
Entrada: Nombre de la oficina y el valor del recibo de luz.
Salida: Actualiza la lista de emisiones de CO2 asociadas a la dependencia de luz.

calculo_transporte():
Propósito: Calcula las emisiones de CO2 asociadas al transporte en una oficina.
Entrada: Nombre de la oficina y los kilómetros recorridos diariamente por los empleados.
Salida: Actualiza la lista de emisiones de CO2 asociadas a la dependencia de transporte.

calculo_dispositivos():
Propósito: Calcula las emisiones de CO2 asociadas al uso de dispositivos en una oficina.
Entrada: Nombre de la oficina, tiempo en horas usando dispositivos y potencia de los dispositivos.
Salida: Actualiza la lista de emisiones de CO2 asociadas a la dependencia de dispositivos.

ver_co2():
Propósito: Muestra las emisiones de CO2 de una oficina específica.
Entrada: Nombre de la oficina.
Salida: Información detallada de las emisiones de CO2 de la oficina.

mayor_co2():
Propósito: Muestra la dependencia que produce la mayor cantidad de CO2 en una oficina específica.
Entrada: Nombre de la oficina.
Salida: Dependencia con la mayor producción de CO2.