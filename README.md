# Taken-IDA-3x3
Este programa resuelve el juego del Taken 3x3 utilizando el algoritmo IDA*.

**Lenguaje utilizado**: Python

## Funciones

 ### **'__ init __(self, tablero)'**
 Este el constructor de la clase Taken que recibe como parametro una lista de numeros desordenadas que será guardado como el tablero.
 
  ### **'mover(self, direccion, tablero)'**
  Esta función mueve el espacio en blanco del tablero a la dirección indicada y devuelve el tablero movido.
 
 ### **'h(self, tablero)'**
 Esta función se encarga de la heuristica del programa, utiliza la distancia Manhattan y devuelve el valor de la heuristica del nodo introducido como parametro de la función.
 
 ### **'movimientosPosibles(self, tablero)'**
 Esta función devuelve una lista de las direcciones a las cuales se puede mover el espacio en blanco en el tablero pasado como parametro.
 
  ### **'inverso(self, pos1, pos2)'**
  Esta función devuelve True si pos1 y pos2 son inversos, por ejemplo "n" y "s" o "e" y "o" son inversos. Está función sirve para evitar que el proximo movimiento no acabe en la posición anterior.
 
 ### **'idaStar(self, tablero)'**
  Esta función recibe como parametro el tablero a partir del cual iniciará el programa y devolverá la solución del problema en caso de que la función busqIDA() haya encontrado solución y en caso de que no haya encontrado solución actualiza el valor de la cota.
 
 ### **'busqIDA(self, camino, profundidad, cota, direcciones)'**
Esta función devuelve la solución del problema en caso de que haya encontrado solución y en caso de no encontrar solución devuelve el valor heuristico minimo de los nodos analizados. 
 
 ## Como utilizar el código
 Para poder utilizar el código se tiene que crear una instancia de la clase "Taken" añadiendole como parametro una lista desordenada de numeros y luego llamar a la funcion idaStar() dandole como parametro la lista a ordenar. El resultado de la ejecución será una serie de letras que indican los movimientos que se tienen que realizar para resolver ese problema.
 
 Donde:
 
 n = Mover el 0 hacia arriba.
 
 s = Mover el 0 hacia abajo.
 
 o = Mover el 0 hacia la izquierda.
 
 e = Mover el 0 hacia la derecha.
 
A continuación se presenta un ejemplo de como utilizar el código:

![image](https://user-images.githubusercontent.com/125157604/229379180-97961285-1902-460a-821f-4366b6cd3b87.png)

