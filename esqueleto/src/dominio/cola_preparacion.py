from src.tads.cola import Cola

#Inicializamos la clase ColaPreparacion
class ColaPreparacion:
    def __init__(self):
        self._cola = Cola()
#Agregamos una receta a la cola
    def encolar_receta(self, receta):
        self._cola.encolar(receta)
#Eliminamos la receta más antigua de la cola y la devolvemos
    def siguiente_receta(self):
        return self._cola.desencolar()
#Devolvemos la receta más antigua de la cola sin eliminarla
    def ver_proxima(self):
        return self._cola.ver_frente()
#Devolvemos True si la cola está vacía, en otro caso devolvemos False
    def esta_vacia(self):
        return self._cola.esta_vacia()