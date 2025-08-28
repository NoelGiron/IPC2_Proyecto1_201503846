from nodo_ld import nodo_ld

class lista_doble:
    def __init__(self):
        self.primero = None
        self.size = 0

    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, dato):
        nuevo = nodo_ld(dato)

        if self.primero == None:
            self.primero = nuevo
        
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
        self.size += 1

    def agregar(self, dato):
        nuevo = nodo_ld(dato)

        if self.primero == None:
            self.primero = nuevo

        else:
            actual = self.primero
            while actual.anterior != None:
                actual = actual.anterior
            actual.anterior = nuevo
        self.size += 1

    def recorrer(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        return None
    
    def eliminar(self, indice):
        actual = self.primero
        contador = 0
        while actual != None:
            if contador == indice:
                if actual == self.primero:
                    self.primero = actual.siguiente
                    actual.siguiente = None
                    self.primero.anterior = None
                    break

                elif actual == self.siguiente:
                    self.siguiente = actual.anterior
                    actual.anterior = None
                    self.siguiente.siguiente = None
                    break

                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    actual.siguiente = None
                    actual.anterior = None
                    break
            
            actual = actual.siguiente

    def imprimir(self):
        if self.primero == None:
            print("La lista esta vacia")
            return 
        
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente
        print(actual.dato)


