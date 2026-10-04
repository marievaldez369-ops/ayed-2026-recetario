from src.tads.pila import Pila

#Iniciamos class HistorialCocina, representa el historial de recetas cocinadas.
class HistorialCocina:
    def __init__(self):
        self._pila = Pila()
#Definimos el metodo registrar, recibe una receta y la agrega a la pila del historial.
    def registrar(self, receta):
        self._pila.apilar(receta)
#Definimos el metodo deshacer, elimina la receta más reciente del historial y la devuelve.
    def deshacer(self):
        return self._pila.desapilar()
#Definimos el metodo ver_ultima, devuelve la receta más reciente del historial sin eliminarla.
    def ver_ultima(self):
        return self._pila.ver_tope()
#Definimos el metodo esta_vacio, devuelve True si el historial está vacío, en otro caso devuelve False.
    def esta_vacio(self):
        return self._pila.esta_vacia()