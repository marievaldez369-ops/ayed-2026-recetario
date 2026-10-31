def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve el ítem cuya clave coincide, o None."""
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        else:
            if obtener_clave(elemento) == clave:
                return elemento
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave=None):
    """La colección tiene que estar ordenada por obtener_clave."""
    izq = 0
    der = len(coleccion_ordenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        elemento = coleccion_ordenada[medio]

        valor_clave = obtener_clave(elemento) if obtener_clave else elemento

        if valor_clave == clave:
            return elemento
        elif valor_clave < clave:
            izq = medio + 1
        else:
            der = medio - 1
    return None
