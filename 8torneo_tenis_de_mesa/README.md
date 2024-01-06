el programa consiste en registrar a jugadores dependiendo su edad se les asigna una categoria, las categorias son novato, intermedio, experto o avanzado, el programa esta construido con 8 modulos y cada uno de ellos tiene la una funcion:

1 - main.py(el menu principal): este es el que nos va a enrutar segun la opcion que escojamos 

2 - registrar.jugador.py: este modulo pide las entradas como nombre, edad, y algun tipo de id identificador en numero, eso se le asigna a una lista que contiene un diccionario y con los otros datos como, partidas ganadas, partidas jugadas, partidas perdidas, puntos a favor, puntos por partida ganados

3 - validar_categoria.py: valida el numero de jugadores ya que tiene que ser minimo 5 jugadores para poder empezar a registrar el juego, si no son suficientes imprime que el numero de jugadores no es suficiente y muestra la cantidad del minimos que son 5, si valida que son 5, llama a la funcion para empezar el juego de dicha categoria

4 -juego_novato, intermedio, experto.py:  el juego empieza cuando dos entradas son veraderas, el nombre y el codigo ig que ingreso el jugador, si no coiniciden con con lo que ingreso anteriormente no podra empezar el juego y lo sacara de esa seccion, si todo es verdadero entonces, empezara el juego y luego cuando acanben los dos sets dependiendo si gano un jugador y perdio el otro va a iterrar en los diccionarios y almacenar los datos de los resultados en los sets, esta funcion es la misma para los tres tipos de categorias  

5 - bucar_jugador.py: este modulo pide dos entradas una es ingresar la categoria a la que esta inscrito el jugador y la otra el el id con que el jugador se inscribio, iteramos sobre los diferentes diccionarios dependiendo de la categoria y luego imprimimos la informacion, manejando las ecepciones, se pide ingresar la categoria ya que se manejan tres listas cada una con una categoria, y asi si por casulalidad existe informacion duplicada no salgan errores 

6 - ganador_categoria.p: este modulo se basa en buscar el jugador con mas puntos de cada categoria y mostrarlos, en caso de que encuentre un empate, en vez de mostrar el primero que encuentre, buscamos los puntos a favor que tiene el juegados, itramos en ellos y luego usamos las funciones len(), max() y lambda para poder conseguir asi el puntaje maximo y imprimir dicho jugador ganador de cada categoria 

7 - se utilizaron listas, diccionarios, funciones propias y integradas, bucles, condicionales etc...
