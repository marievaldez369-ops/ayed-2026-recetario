"""Lectura y validación de los CSV originales entregados por la cátedra."""

import csv
from pathlib import Path

from src.excepciones import ArchivoInvalidoError

ENCABEZADOS_RECETAS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
ENCABEZADOS_INGREDIENTES = ["receta_id", "nombre", "cantidad", "unidad"]
ENCABEZADOS_SUBRECETAS = ["receta_id", "subreceta_id"]


def _leer_csv(ruta, encabezados):
    """Lee un CSV y valida encabezados, cantidad de campos y valores vacíos."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise ArchivoInvalidoError(f"No existe el archivo CSV: {ruta}")

    try:
        with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != encabezados:
                raise ArchivoInvalidoError(
                    f"Encabezados inválidos en {ruta.name}. Se esperaba: {', '.join(encabezados)}."
                )

            filas = []
            for numero, fila in enumerate(lector, start=2):
                if None in fila or any(fila.get(campo) is None for campo in encabezados):
                    raise ArchivoInvalidoError(
                        f"La línea {numero} de {ruta.name} tiene una cantidad incorrecta de campos."
                    )

                if any(not fila[campo].strip() for campo in encabezados):
                    raise ArchivoInvalidoError(
                        f"La línea {numero} de {ruta.name} contiene campos vacíos."
                    )

                filas.append({campo: fila[campo].strip() for campo in encabezados})

            return filas
    except UnicodeDecodeError as error:
        raise ArchivoInvalidoError(
            f"El archivo {ruta.name} no tiene una codificación UTF-8 válida."
        ) from error
    except csv.Error as error:
        raise ArchivoInvalidoError(f"No se pudo leer {ruta.name}: {error}") from error
    except OSError as error:
        raise ArchivoInvalidoError(f"No se pudo abrir {ruta.name}: {error}") from error


def cargar_recetas_csv(ruta):
    """Carga las recetas de la cátedra y valida sus identificadores y tiempos."""
    filas = _leer_csv(ruta, ENCABEZADOS_RECETAS)
    ids = set()

    for numero, fila in enumerate(filas, start=2):
        try:
            id_receta = int(fila["id"])
            tiempo = int(fila["tiempo_min"])
        except ValueError as error:
            raise ArchivoInvalidoError(
                f"La línea {numero} contiene un ID o tiempo que no es entero."
            ) from error

        if id_receta <= 0:
            raise ArchivoInvalidoError(f"La línea {numero} tiene un ID no válido.")
        if tiempo < 0:
            raise ArchivoInvalidoError(f"La línea {numero} tiene un tiempo negativo.")
        if id_receta in ids:
            raise ArchivoInvalidoError(f"El ID {id_receta} está repetido en {Path(ruta).name}.")
        ids.add(id_receta)

    return filas


def cargar_ingredientes_csv(ruta, ids_recetas):
    """Carga ingredientes agrupados por ID de receta."""
    filas = _leer_csv(ruta, ENCABEZADOS_INGREDIENTES)
    ids_recetas = set(ids_recetas)
    ingredientes = {}

    for numero, fila in enumerate(filas, start=2):
        try:
            id_receta = int(fila["receta_id"])
        except ValueError as error:
            raise ArchivoInvalidoError(
                f"La línea {numero} de ingredientes.csv tiene un ID inválido."
            ) from error

        # Si la receta fue dada de baja del catálogo persistente, se omiten
        # sus ingredientes originales al reconstruir el catálogo.
        if id_receta not in ids_recetas:
            continue

        detalle = f'{fila["nombre"]}: {fila["cantidad"]} {fila["unidad"]}'
        ingredientes.setdefault(id_receta, []).append(detalle)

    return ingredientes


def cargar_subrecetas_csv(ruta, ids_recetas):
    """Carga las relaciones entre recetas y subrecetas."""
    filas = _leer_csv(ruta, ENCABEZADOS_SUBRECETAS)
    ids_recetas = set(ids_recetas)
    relaciones = {}

    for numero, fila in enumerate(filas, start=2):
        try:
            id_receta = int(fila["receta_id"])
            id_subreceta = int(fila["subreceta_id"])
        except ValueError as error:
            raise ArchivoInvalidoError(
                f"La línea {numero} de subrecetas.csv contiene un ID inválido."
            ) from error

        # Las relaciones que incluyan recetas dadas de baja dejan de aplicarse.
        if id_receta not in ids_recetas or id_subreceta not in ids_recetas:
            continue

        relaciones.setdefault(id_receta, []).append(id_subreceta)

    return relaciones
