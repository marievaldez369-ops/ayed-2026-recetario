"""Modelo y operaciones del catálogo de recetas."""

from pathlib import Path

from src.dominio.receta import Receta
from src.excepciones import ItemNoEncontradoError
from src.persistencia.cargar_csv import (
    cargar_recetas_csv,
    cargar_ingredientes_csv,
    cargar_subrecetas_csv,
)
from src.persistencia.texto import ENCABEZADOS, cargar_texto, guardar_texto
from src.tads.lista_enlazada import ListaEnlazada

RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
RUTA_CSV = DATA / "recetas.csv"
RUTA_TXT = DATA / "recetas.txt"
RUTA_INGREDIENTES = DATA / "ingredientes.csv"
RUTA_SUBRECETAS = DATA / "subrecetas.csv"


class Recetario:
    """Administra el catálogo y sus relaciones con ingredientes y subrecetas."""

    def __init__(self):
        if RUTA_TXT.is_file():
            filas = cargar_texto(RUTA_TXT)
        else:
            filas = cargar_recetas_csv(RUTA_CSV)
            guardar_texto(RUTA_TXT, filas, ENCABEZADOS)

        self.catalogo = self._armar_catalogo(filas)

    def _armar_catalogo(self, filas):
        """Construye los objetos Receta y enlaza ingredientes y subrecetas."""
        ids_recetas = {int(fila["id"]) for fila in filas}
        ingredientes = cargar_ingredientes_csv(RUTA_INGREDIENTES, ids_recetas)
        relaciones = cargar_subrecetas_csv(RUTA_SUBRECETAS, ids_recetas)

        recetas = {}
        for fila in filas:
            id_receta = int(fila["id"])
            recetas[id_receta] = Receta(
                id_receta,
                fila["nombre"],
                fila["tiempo_min"],
                fila["dificultad"],
                fila["categoria"],
                ingredientes.get(id_receta, []),
            )

        for id_receta, ids_subrecetas in relaciones.items():
            recetas[id_receta].subrecetas = [
                recetas[id_subreceta]
                for id_subreceta in ids_subrecetas
            ]

        catalogo = ListaEnlazada()
        for receta in recetas.values():
            catalogo.insertar_al_final(receta)

        return catalogo

    def buscar_por_id(self, id_receta):
        for receta in self.catalogo:
            if receta.id == id_receta:
                return receta
        return None

    def buscar_posicion(self, id_receta):
        for posicion, receta in enumerate(self.catalogo):
            if receta.id == id_receta:
                return posicion
        raise ItemNoEncontradoError(f"No existe una receta con ID {id_receta}.")

    def agregar(self, receta):
        if self.buscar_por_id(receta.id) is not None:
            raise ValueError("Ya existe una receta con ese ID.")
        self.catalogo.insertar_al_final(receta)

    def eliminar(self, id_receta):
        receta = self.buscar_por_id(id_receta)
        if receta is None:
            raise ItemNoEncontradoError(f"No existe una receta con ID {id_receta}.")
        self.catalogo.eliminar(receta)
        return receta

    def modificar(self, id_receta, nombre, tiempo_min, dificultad, categoria):
        receta = self.buscar_por_id(id_receta)
        if receta is None:
            raise ItemNoEncontradoError(f"No existe una receta con ID {id_receta}.")

        receta.nombre = nombre
        receta.tiempo_min = int(tiempo_min)
        receta.dificultad = dificultad
        receta.categoria = categoria
        return receta

    def filas(self):
        """Convierte el catálogo a registros simples para guardarlo en TXT."""
        return [
            {
                "id": receta.id,
                "nombre": receta.nombre,
                "tiempo_min": receta.tiempo_min,
                "dificultad": receta.dificultad,
                "categoria": receta.categoria,
            }
            for receta in self.catalogo
        ]

    def guardar_texto(self):
        guardar_texto(RUTA_TXT, self.filas(), ENCABEZADOS)

    def reemplazar_catalogo(self, catalogo):
        filas = [
            {
                "id": receta.id,
                "nombre": receta.nombre,
                "tiempo_min": receta.tiempo_min,
                "dificultad": receta.dificultad,
                "categoria": receta.categoria,
            }
            for receta in catalogo
        ]
        self.catalogo = self._armar_catalogo(filas)

    def mostrar_catalogo(self):
        print("\nCatálogo de recetas de la cátedra:")
        for receta in self.catalogo:
            print(
                f"{receta.resumen()} | {receta.tiempo_min} min | "
                f"{receta.dificultad} | {receta.categoria}"
            )


def mostrar_receta_completa(receta, nivel=0):
    sangria = "    " * nivel
    print(f"\n{sangria}--- {receta.nombre.upper()} ---")
    print(
        f"{sangria}Tiempo: {receta.tiempo_min} min | "
        f"Dificultad: {receta.dificultad} | Categoría: {receta.categoria}"
    )

    if receta.ingredientes:
        print(f"{sangria}Ingredientes:")
        for ingrediente in receta.ingredientes:
            print(f"{sangria}- {ingrediente}")

    for subreceta in receta.subrecetas:
        mostrar_receta_completa(subreceta, nivel + 1)


def obtener_ingredientes_totales(receta):
    ingredientes = list(receta.ingredientes)
    for subreceta in receta.subrecetas:
        ingredientes.extend(obtener_ingredientes_totales(subreceta))
    return ingredientes
