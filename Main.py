import xml.etree.ElementTree as ET
from xml.dom import minidom
from lista_enlazada import *
from lista_doble import *
from campo_agricola import *
from nodo_ld import *

filaXml = lista_enlazada();
columnasXml = lista_doble();

def menuPrincipal():
    print("1) Carga de archivos")
    print("2) Procesar el archvio")
    print("3) Escribir archivo de salida")
    print("4) Mostrar datos del estudiante")
    print("5) Generar gráfica")
    print("6) Salir \n")

def cargarArchivo():
    ruta =input("Ingrese la ruta del archivo: ")
    leerArchivo(ruta)

def leerArchivo(rutaArchivo):
    tree = ET.parse(rutaArchivo)
    root = tree.getroot()

    for elementos_campo in root.findall('campo'):
        id = elementos_campo.get('id')
        nombre = elementos_campo.get('nombre')
        campo = campo_agricola(id, nombre)

        for elementos_sensor in elementos_campo.find('estacionesBase').findall('estaciones'):
            id = elementos_sensor.get('id')
            nombre = elementos_sensor.get('nombre')
            estacion = nodo_ld(nombre)
            campo.estaciones_base.insertar(estacion)

        columnasXml.insertar(campo)
    columnasXml.imprimir()

if __name__=="__main__":
    pregunta = True
    while pregunta:
        menuPrincipal()
        opcion = int(input("Ingrese una de las opciones: "))
        
        if opcion == 1:
            cargarArchivo()

        elif opcion == 2:
            print("se proceso el archivo")

        elif opcion == 3:
            print("se escribio el archivo de salida")
        
        elif opcion == 4:
            print("se mosotraron los datos")

        elif opcion == 5:
            print("se genero el grafo")

        elif opcion == 6:
            break

        else:
            print("Opcion no valida, intente de nuevo")