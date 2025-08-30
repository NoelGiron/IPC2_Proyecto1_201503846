from nodo_le import nodo_le

class lista_enlazada:
    def __init__(self):
        self.primero = None
        self.size = 0

    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, dato):
        nuevo = nodo_le(dato)

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
        return None

    def imprimir(self):
        if self.primero == None:
            print("La lista esta vacia")
            return 
        
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente
        print(actual.dato)

    def obtener_posicion(self, x):
        actual = self.primero
        while actual != None:
            if actual.dato.s == x:
                return actual
            actual = actual.siguiente
        return None
    
    def graficar_celda(self):
        actual = self.primero
        cadena = ""
        while actual != None:
            cadena = f'<TD WIDTH="50" HEIGHT="50" >{actual.dato.frecuencia}</TD>\n'
            actual = actual.siguiente
        return cadena