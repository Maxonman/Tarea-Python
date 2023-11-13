Elias William Abraham Valle Arias 202173537-2

Para la correcta ejecución de este codigo se necesita tener los archivo codigo.txt y config.txt, los cuales
deben ser incluidos en la misma carpeta del programa.

En caso de que no esten los archivos el programa este lanzara un error por la terminal.

Si es que este funciona correctamente se generara un archivo llamado formateado.txt . 

El Formater funciona de la manera en que si se encuentra algo que las expresiones regulares
no pudieron detectar, por ejemplo: "int var; ??=== while(a==b){}", en este caso las expresiones solo detectarian
"int var;" y "while(a==b){}", luego se haria una segunda revision, usando una ultima expresion regular que detecta conjuntos de
caracteres cualquiera en la cual se comprobaria que "??===" no esta dentro de las normas de las expresiones regulares, por lo que 
seria marcada su posicion y se haria un formateo hasta antes de su aparicion.


Ademas de esto, se tiene una comprobacion de bloques de manera que con una pila se ve si cada llave abierta tiene una llave cerrada, por ejemplo {}, aqui se añadiria la posicion de la primera llave a la pila y luego al encontrar el cierre esta se borraria.
En el caso "while(true){while()true{}" , la primera llave es la que no se cerraria, porque el formater llegaria hasta la posicion de la llave-1, que es donde encontro el error.
Tambien se tiene lo mismo pero para cuando hay mas llaves cerradas que abiertas, se formatea hasta la posicion de la llave-1.

Ademas se tiene agregado que no puede haber un else{}, sin antes haber un if(){}, en este caso, se formatearia hasta la posicion del else-1.
