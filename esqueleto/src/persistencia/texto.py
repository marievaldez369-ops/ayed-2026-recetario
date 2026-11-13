"""Persistencia del catálogo en un archivo de texto delimitado por comas."""

import csv
from pathlib import Path

from src.excepciones import ArchivoInvalidoError

ENCABEZADOS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]


def cargar_texto(ruta):
    """Lee recetas.txt y devuelve sus registros como diccionarios validados."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    try:
        with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != ENCABEZADOS:
                raise ArchivoInvalidoError("El encabezado del archivo de texto no es válido.")

            filas = []
            ids = set()
            for numero, fila in enumerate(lector, start=2):
                if None in fila or any(fila.get(campo) is None for campo in ENCABEZADOS):
                    raise ArchivoInvalidoError(
                        f"La línea {numero} tiene una cantidad incorrecta de campos."
                    )

                fila = {campo: fila[campo].strip() for campo in ENCABEZADOS}
                if any(not valor for valor in fila.values()):
                    raise ArchivoInvalidoError(f"La línea {numero} contiene campos vacíos.")

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
                    raise ArchivoInvalidoError(f"El ID {id_receta} está repetido en el archivo.")

                ids.add(id_receta)
                filas.append(fila)

            return filas
    except UnicodeDecodeError as error:
        raise ArchivoInvalidoError(
            "El archivo no tiene una codificación de texto válida."
        ) from error
    except csv.Error as error:
        raise ArchivoInvalidoError(f"No se pudo leer el archivo: {error}") from error
    except OSError as error:
        raise ArchivoInvalidoError(f"No se pudo abrir el archivo: {error}") from error


def guardar_texto(ruta, filas, encabezados=ENCABEZADOS):
    """Guarda el catálogo completo en texto, incluyendo la fila de encabezados."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    try:
        with ruta.open("w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=encabezados,
                extrasaction="raise",
            )
            escritor.writeheader()
            escritor.writerows(filas)
    except (OSError, csv.Error) as error:
        raise ArchivoInvalidoError(f"No se pudo guardar el archivo de texto: {error}") from error
