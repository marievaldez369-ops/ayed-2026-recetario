from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class MenuSemanal:
    def __init__(self, tope=7):
        self._recetas = ListaEnlazada()
        self._tope = tope

    def agregar(self, receta):
        if self._recetas.tamanio() >= self._tope:
            raise ColeccionLlenaError("El menú semanal está lleno.")
        self._recetas.insertar_al_final(receta)

    def eliminar(self, receta):
        self._recetas.eliminar(receta)

    def listar(self):
        for r in self._recetas:
            print(f"- {r.nombre}")