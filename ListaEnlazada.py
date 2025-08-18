from NodoLE import NodoLE

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0
    
    def insertar(self, dato):
        nuevo = NodoLE(dato)

        if self.primero == None:
            self.primero = nuevo

        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1

    def recorrer(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                return actual.dato
        actual = actual.siguiente
        contador += 1

    def imprimir(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente
        print(actual.dato)