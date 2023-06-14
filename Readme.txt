Instrucciones
La NASA va a aterrizar un escuadrón de robots exploradores en una meseta de Marte.

Esta meseta, curiosamente rectangular, debe ser recorrida por los robots para que sus cámaras a bordo puedan obtener 
una vista completa del terreno circundante y enviarla a la Tierra.

Tu tarea consiste en desarrollar una API que movilice a los robots por la meseta.

En esta API, la meseta se representa como una cuadrícula de 10x10, y un robot tiene un estado que consta de dos partes:

Su posición en la cuadrícula (representada por una pareja de coordenadas X,Y)
La dirección de la brújula hacia la que está orientado (representada por una letra, una de N, S, E, W)
Input
El input del programa es una cadena de comandos de movimiento de un carácter:

L y R rotan la dirección en la que está orientado el robot
M mueve el vehículo una casilla hacia delante en la dirección en la que se encuentra en ese momento.
Si un rover llega al final de la meseta, da un giro al final de la cuadrícula.

Output
El output del programa es la posición final del robot después de que se hayan ejecutado todos los comandos de movimiento.
La posición se representa como una pareja de coordenadas y una dirección, unidas por dos puntos para formar una cadena.
Por ejemplo: un robot cuya posición es 2:3:W está en la casilla (2,3), mirando al oeste.

Obstáculos
La cuadrícula puede tener obstáculos. Si una secuencia de comandos determinada encuentra un obstáculo, el robot se desplaza hasta el último punto posible 
e informa del obstáculo anteponiendo O: a la cadena de posición que devuelve. Por ejemplo,  O:1:1:N  significaría que el robot ha encontrado un obstáculo en la posición (1, 2).

Ejemplos
En una cuadrícula sin obstáculos, el input MMRMMLM da un output de 2:3:N
En una cuadrícula sin obstáculos, el input MMMMMMMMMM da un output de 0:0:N (debido al giro)
En una cuadrícula con un obstáculo en (0, 3), el input MMMM da un output de O:0:2:N