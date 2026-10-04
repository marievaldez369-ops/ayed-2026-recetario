from src.tads.nodo import Nodo
#Definición de la clase ListaEnlazada
class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""
#definición de los métodos de la clase ListaEnlazada
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0
#Devuelve True si la lista está vacía, False en caso contrario.
    def esta_vacia(self):
        return self._cabeza is None
#Devuelve el tamaño de la lista.
    def tamanio(self):
        return self._tamanio
#Devuelve el dato del nodo en la posición indicada, si la posición es inválida devuelve None.
    def insertar_al_inicio(self, dato):
        nuevo=Nodo(dato,self._cabeza)
        self._cabeza=nuevo
        self._tamanio += 1
#Inserta un nodo al final de la lista.
    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1
#Inserta un nodo en la lista de manera ordenada según el valor de la clave proporcionada.
    def insertar_ordenado(self, dato, clave):
        nuevo = Nodo(dato)
        if self.esta_vacia(): 
            self._cabeza = nuevo
            self._tamanio += 1
            return
        if getattr(dato, clave) < getattr(self._cabeza.dato, clave):
            nuevo.siguiente = self._cabeza
            self._cabeza = nuevo
            self._tamanio += 1
            return
        
        actual = self._cabeza
        while actual.siguiente is not None and getattr(actual.siguiente.dato, clave) < getattr(dato, clave):   
                actual = actual.siguiente
        
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        self._tamanio += 1
#Elimina el primer nodo que contiene el dato especificado. Si la lista está vacía o el dato no se encuentra, no hace nada.
    def eliminar(self, dato):
        if self.esta_vacia():
            return
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return
        actual = self._cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self._tamanio -= 1
                return
            actual = actual.siguiente
#Devuelve el nodo que contiene el dato. Si la lista está vacía o el dato no se encuentra, devuelve None.
    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual   
            actual = actual.siguiente
        return None
#Devuelve un iterador que recorre los elementos de la lista.
    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente