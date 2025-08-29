from lista_doble import lista_doble
class campo_agricola:
    def __init__(self, id_campo, nombre_campo):
        self.id_campo = id_campo
        self.nombre_campo = nombre_campo
        self.estaciones_base = lista_doble();

    def __str__(self):
        return f'ID: {self.id_campo} Nombre: {self.nombre_campo} Estaciones: {self.estaciones_base.imprimir()}'
