# IPC2_Proyecto1_201503846
El problema de diseño de distribución de estaciones base consiste en determinar la cantidad
óptima de estaciones base necesarias para recolectar toda la información en tiempo real, por
lo que se trata de un problema combinatorio

## Variables del programa
La metodología de agrupamiento propuesta consiste en identificar una matriz de frecuencias
para “n” estaciones base y “s” sensores de suelo (F[n,s]); y otra matriz de frecuencias para
las mismas “n” estaciones base y “t” sensores de cultivo (F[n,t]) implementados en un campo
agrícola “x”, identificando de esta forma qué estación base recibe datos de qué sensores de
suelo y de cultivo.

![image_Alt](/imagenes/Screenshot%202025-08-10%20202221.png)

El proceso de agrupamiento consiste en transformar las matrices de frecuencias F[n,s] y F[n,t]
en sus respectivas matrices de patrones Fp[n,s] y Fp[n,t], eso lo hacemos identificando que casilla de la matriz F tiene un valor mayor a 0, luego en la matriz Fp en esa misma posicon colocamos un 1, si el valor que hay en la casilla de la matriz F es igual a 0 colocaremos en la matriz Fp un 0. 

![image_Alt](/imagenes/Screenshot%202025-08-10%20203425.png)

luego se busca que filas de ambas matrices tengan el mismo patron, en este caso la fila n1 y n3 tiene el mismo patron [1,1,0,1] (el patron incluye ambas matrices) y la final n2 y n5 [0,0,1,1] luego se suman los datos de la matriz F[n,s] de las filas con el mismo patron

![image_Alt](/imagenes/Screenshot%202025-08-10%20204416.png)

esto data como resultado una matriz reducida Fr[n,s], Fr[n,t]

## Reportes
Se deberá utilizar la herramienta Graphviz para crear un grafo que muestre de manera gráfica
las matrices de frecuencia F[n,s] y F[n,t], las matrices de patrones Fp[n,s] y Fp[n,t] o las
matrices reducidas Fr[n,s] y Fr[n,t] para cualquier campo agrícola configurado en la aplicación
a desarrollar.

## Archivos de Entrada y Salida
Los archivos de entrada y salida consistirán en archivos con extensión y estructura xm

## Menú
La aplicación deberá contar con un menú en consola, con las siguientes opciones

* Menú principal:
* * Cargar Archivo: Esta Opción solicitará la ruta y el nombre del archivo a cargar.
* * Procesar el Archivo: Esta opción será la encargada de procesar la información
cargada en memoria, durante el proceso se deben ir mostrando mensajes al usuario
para tener el conocimiento de lo que está pasando en el sistema
* * Escribir Archivo de salida: Esta opción será la encargada de escribir el archivo con
la salida específica.
* * Mostrar datos del estudiante: Mostrar los datos del estudiante, carné, nombre,
curso, carrera, semestre y enlace de acceso a documentación.
* * Generar gráfica: El programa deberá permitir que el usuario elija un campo agrícola
ingresado en el archivo de entrada, luego debe solicitar si se desea graficar la matriz de frecuencias, la matriz de patrones o la matriz reducida de dicho campo agrícola.
Finalmente, se mostrará la gráfica