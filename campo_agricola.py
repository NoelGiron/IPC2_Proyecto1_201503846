from lista_doble import lista_doble
from celda import celda
class campo_agricola:
    def __init__(self, id_campo, nombre_campo, estaciones, sensores):
        self.id_campo = id_campo
        self.nombre_campo = nombre_campo
        self.estaciones = estaciones
        self.sensores = sensores
        self.matriz = lista_doble()
        self.matriz_frecuencias()
    
    def matriz_frecuencias(self):
        for y in range(self.estaciones):
            encabezado = self.matriz.insertar(celda(n = 0, s = 1))
            for x in range(self.sensores):
                encabezado.fila.insertar(celda(n = x, s = y))
        print("Se creo el campo agricola")

    def __str__(self):
        return f'ID: {self.id_campo} Nombre: {self.nombre_campo} Estaciones: {self.estaciones_base.imprimir()}'
