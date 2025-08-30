from lista_doble import lista_doble
from celda import celda
class campo_agricola:
    def __init__(self, id_campo, nombre_campo):
        self.id_campo = id_campo
        self.nombre_campo = nombre_campo
        self.matriz = lista_doble()
    
    def matriz_frecuencias(self, estaciones, sensores):
        for y in range(estaciones):
            encabezado = self.matriz.insertar(celda(n = 0, s = 1))
            for x in range(sensores):
                encabezado.fila.insertar(celda(n = x, s = y))
        print("Se creo el campo agricola")

    def __str__(self):
        return f'ID: {self.id_campo} Nombre: {self.nombre_campo} Estaciones: '
