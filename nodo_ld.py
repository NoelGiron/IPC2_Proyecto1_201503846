from lista_enlazada import *
class nodo_ld:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.fila = lista_enlazada()