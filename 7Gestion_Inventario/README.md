este programa hace enfoque en tener el control del inventario de un negocio, tiene en cuenta varios aspectos como de opcion como agregar, ver, actualizar, informa, ver ganancias de productos, es un programa sencillo conformado por dos modulos, uno que contiene el menu y el otro que registra, actualiza, informa y muestra los producto, contiene todos los procesos para que el programa funcione.

una breve explicacion de lo que hace el programa:

main.py
Funciones Principales:
menu():
Imprime un menú de opciones para que el usuario elija una operación.
No hay manejo de excepciones para opciones no numéricas.

main():
Inicia un bucle principal que ejecuta las operaciones del menú hasta que el usuario elija salir.
Llama a funciones del módulo registros.py según la opción seleccionada.


registros.py

Funciones Principales:
agregar_producto():
Solicita información sobre un nuevo producto y lo agrega a la lista de productos.

ver_productos():
Muestra la lista completa de productos en formato JSON.

actualizar_producto():
Permite al usuario actualizar el stock máximo o mínimo de un producto.

minimo_limite():
Informa sobre los productos con un stock por debajo de un límite constante.

ganancia():
Calcula y muestra la ganancia potencial de cada producto.