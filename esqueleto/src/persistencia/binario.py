"""Persistencia binaria de recetas con registros de longitud fija."""

import struct
from pathlib import Path

from src.dominio.receta import Receta
from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada

# id, nombre (30 bytes), tiempo_min, dificultad (10 bytes), categoria (15 bytes)
FORMATO = struct.Struct("<I30sH10s15s")
HEADER = struct.Struct("<4s1sI")
TEMA = b"R"
MAGIA = b"AYED"


def _a_bytes(texto, ancho):
    datos = str(texto).encode("utf-8")
    if len(datos) > ancho:
        raise ValueError(f"El texto '{texto}' supera el máximo de {ancho} bytes.")
    return datos.ljust(ancho, b"\x00")


def _a_texto(datos):
    return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(receta):
    return (
        int(receta.id),
        _a_bytes(receta.nombre, 30),
        int(receta.tiempo_min),
        _a_bytes(receta.dificultad, 10),
        _a_bytes(receta.categoria, 15),
    )


def _tupla_a_item(datos):
    return Receta(
        datos[0],
        _a_texto(datos[1]),
        datos[2],
        _a_texto(datos[3]),
        _a_texto(datos[4]),
    )


def _leer_cabecera(archivo):
    cabecera = archivo.read(HEADER.size)
    if len(cabecera) != HEADER.size:
        raise ArchivoInvalidoError("Binario truncado: header incompleto.")

    magia, tema, cantidad = HEADER.unpack(cabecera)
    if magia != MAGIA:
        raise ArchivoInvalidoError("Magia incorrecta: el archivo no pertenece al TP.")
    if tema != TEMA:
        raise ArchivoInvalidoError("El archivo binario no corresponde al tema Recetario.")

    return magia, tema, cantidad


def _validar_tamanio(archivo, cantidad):
    archivo.seek(0, 2)
    tamanio_esperado = HEADER.size + cantidad * FORMATO.size
    if archivo.tell() != tamanio_esperado:
        raise ArchivoInvalidoError(
            "El tamaño del archivo binario no coincide con la cantidad de registros del header."
        )


def guardar_binario(ruta, catalogo):
    """Escribe el header y todos los registros del catálogo."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    try:
        with ruta.open("wb") as archivo:
            archivo.write(HEADER.pack(MAGIA, TEMA, catalogo.tamanio()))
            for receta in catalogo:
                archivo.write(FORMATO.pack(*_item_a_tupla(receta)))
    except (OSError, struct.error, UnicodeEncodeError, ValueError) as error:
        raise ArchivoInvalidoError(f"No se pudo guardar el archivo binario: {error}") from error


def cargar_binario(ruta):
    """Lee y valida el archivo binario. Devuelve una ListaEnlazada de recetas."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    try:
        with ruta.open("rb") as archivo:
            _, _, cantidad = _leer_cabecera(archivo)
            _validar_tamanio(archivo, cantidad)
            archivo.seek(HEADER.size)

            catalogo = ListaEnlazada()
            for _ in range(cantidad):
                datos = archivo.read(FORMATO.size)
                if len(datos) != FORMATO.size:
                    raise ArchivoInvalidoError("Binario truncado: falta uno o más registros.")
                catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))

            return catalogo
    except (OSError, struct.error, UnicodeDecodeError) as error:
        raise ArchivoInvalidoError(f"No se pudo interpretar el binario: {error}") from error


def actualizar_registro(ruta, posicion, receta):
    """Actualiza un registro existente usando acceso directo con seek()."""
    ruta = Path(ruta)
    if posicion < 0:
        raise ArchivoInvalidoError("La posición del registro no es válida.")

    try:
        with ruta.open("r+b") as archivo:
            magia, tema, cantidad = _leer_cabecera(archivo)
            _validar_tamanio(archivo, cantidad)
            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posición no corresponde a un registro existente.")

            posicion_archivo = HEADER.size + posicion * FORMATO.size
            archivo.seek(posicion_archivo)
            archivo.write(FORMATO.pack(*_item_a_tupla(receta)))
    except (OSError, struct.error, UnicodeEncodeError, ValueError) as error:
        if isinstance(error, ArchivoInvalidoError):
            raise
        raise ArchivoInvalidoError(f"No se pudo actualizar el registro: {error}") from error


def alta_binario(ruta, receta):
    """Agrega un registro al final y actualiza la cantidad del header."""
    ruta = Path(ruta)
    try:
        with ruta.open("r+b") as archivo:
            magia, tema, cantidad = _leer_cabecera(archivo)
            _validar_tamanio(archivo, cantidad)
            archivo.seek(0, 2)
            archivo.write(FORMATO.pack(*_item_a_tupla(receta)))
            archivo.seek(0)
            archivo.write(HEADER.pack(magia, tema, cantidad + 1))
    except (OSError, struct.error, UnicodeEncodeError, ValueError) as error:
        if isinstance(error, ArchivoInvalidoError):
            raise
        raise ArchivoInvalidoError(f"No se pudo agregar el registro: {error}") from error


def baja_binario(ruta, posicion):
    """Elimina un registro y reescribe los restantes actualizando el header."""
    ruta = Path(ruta)
    if posicion < 0:
        raise ArchivoInvalidoError("La posición del registro no es válida.")

    try:
        with ruta.open("r+b") as archivo:
            magia, tema, cantidad = _leer_cabecera(archivo)
            _validar_tamanio(archivo, cantidad)
            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posición no corresponde a un registro existente.")

            archivo.seek(HEADER.size)
            registros = [archivo.read(FORMATO.size) for _ in range(cantidad)]
            del registros[posicion]

            archivo.seek(0)
            archivo.truncate()
            archivo.write(HEADER.pack(magia, tema, cantidad - 1))
            for registro in registros:
                archivo.write(registro)
    except (OSError, struct.error) as error:
        if isinstance(error, ArchivoInvalidoError):
            raise
        raise ArchivoInvalidoError(f"No se pudo eliminar el registro: {error}") from error
