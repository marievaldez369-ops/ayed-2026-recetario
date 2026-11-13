from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.dominio.receta import Receta
from src.dominio.recetario import (
    Recetario, RUTA_TXT, DATA, mostrar_receta_completa,
    obtener_ingredientes_totales,
)
from src.excepciones import (
    ArchivoInvalidoError, ItemNoEncontradoError,
    PilaVaciaError, ColaVaciaError,
)
from src.persistencia.texto import guardar_texto, ENCABEZADOS
from src.persistencia.binario import (
    guardar_binario, cargar_binario, actualizar_registro,
    alta_binario, baja_binario,
)
from src.dominio.historial import HistorialCocina
from src.dominio.cola_preparacion import ColaPreparacion

RUTA_BIN = DATA / "recetas.bin"
recetario = Recetario()
historial = HistorialCocina()
cola_preparacion = ColaPreparacion()
ordenado_por = None


def mostrar_menu():
    print("\n=== Recetario — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Alta / baja / modificación")
    print("7. Historial (pila)")
    print("8. Cola de preparación")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Ingresá un número entero válido.")


def guardar_todo():
    recetario.guardar_texto()
    guardar_binario(RUTA_BIN, recetario.catalogo)


def asegurar_binario():
    if not RUTA_BIN.exists():
        guardar_binario(RUTA_BIN, recetario.catalogo)


def menu_detalle():
    id_receta = pedir_entero("ID de la receta: ")
    receta = recetario.buscar_por_id(id_receta)
    if receta is None:
        print("No se encontró una receta con ese ID.")
        return
    mostrar_receta_completa(receta)


def menu_busqueda():
    global ordenado_por
    print("1. Búsqueda lineal por nombre")
    print("2. Búsqueda binaria por nombre")
    opcion = input("> ").strip()
    if opcion not in {"1", "2"}:
        print("Opción inválida.")
        return
    nombre = input("Nombre de la receta: ").strip().casefold()
    recetas = list(recetario.catalogo)
    clave = lambda receta: receta.nombre.casefold()

    if opcion == "1":
        resultado = busqueda_lineal(recetas, nombre, obtener_clave=clave)
    else:
        if ordenado_por != "nombre":
            print("La búsqueda binaria requiere ordenar por nombre primero.")
            return
        resultado = busqueda_binaria(recetas, nombre, obtener_clave=clave)

    print(resultado.resumen() if resultado else "No se encontró la receta.")


def menu_ordenar():
    global ordenado_por
    print("1. Ordenar por nombre (selección)")
    print("2. Ordenar por tiempo de preparación (inserción)")
    opcion = input("> ").strip()
    recetas = list(recetario.catalogo)

    if opcion == "1":
        ordenadas = ordenar_seleccion(recetas, lambda receta: receta.nombre.casefold())
        ordenado_por = "nombre"
    elif opcion == "2":
        ordenadas = ordenar_insercion(recetas, lambda receta: receta.tiempo_min)
        ordenado_por = "tiempo"
    else:
        print("Opción inválida.")
        return

    recetario.reemplazar_catalogo(ordenadas)
    guardar_todo()
    print("Catálogo ordenado y guardado.")


def menu_abm():
    global ordenado_por
    while True:
        print("\n=== Administración del catálogo ===")
        print("1. Alta de receta")
        print("2. Baja de receta")
        print("3. Modificación de receta")
        print("0. Volver")
        opcion = input("> ").strip()
        if opcion == "0":
            return
        try:
            if opcion == "1":
                id_receta = pedir_entero("ID nuevo: ")
                nombre = input("Nombre: ").strip()
                tiempo = pedir_entero("Tiempo en minutos: ")
                dificultad = input("Dificultad: ").strip()
                categoria = input("Categoría: ").strip()
                if (
                    id_receta <= 0 or id_receta > 0xFFFFFFFF
                    or tiempo < 0 or tiempo > 0xFFFF
                    or not nombre or not dificultad or not categoria
                ):
                    print("Ingresá un ID positivo, un tiempo entre 0 y 65535 y todos los campos de texto.")
                    continue
                receta = Receta(id_receta, nombre, tiempo, dificultad, categoria)
                asegurar_binario()
                recetario.agregar(receta)
                alta_binario(RUTA_BIN, receta)
                recetario.guardar_texto()
                ordenado_por = None
                print("Receta agregada y guardada.")

            elif opcion == "2":
                id_receta = pedir_entero("ID a eliminar: ")
                asegurar_binario()
                posicion = recetario.buscar_posicion(id_receta)
                recetario.eliminar(id_receta)
                baja_binario(RUTA_BIN, posicion)
                recetario.guardar_texto()
                ordenado_por = None
                print("Receta eliminada y guardada.")

            elif opcion == "3":
                id_receta = pedir_entero("ID a modificar: ")
                asegurar_binario()
                posicion = recetario.buscar_posicion(id_receta)
                receta_actual = recetario.buscar_por_id(id_receta)
                nombre = input(f"Nombre [{receta_actual.nombre}]: ").strip() or receta_actual.nombre
                tiempo_texto = input(f"Tiempo en minutos [{receta_actual.tiempo_min}]: ").strip()
                tiempo = int(tiempo_texto) if tiempo_texto else receta_actual.tiempo_min
                dificultad = input(f"Dificultad [{receta_actual.dificultad}]: ").strip() or receta_actual.dificultad
                categoria = input(f"Categoría [{receta_actual.categoria}]: ").strip() or receta_actual.categoria
                if tiempo < 0 or tiempo > 0xFFFF:
                    print("El tiempo debe estar entre 0 y 65535 minutos.")
                    continue
                receta = recetario.modificar(id_receta, nombre, tiempo, dificultad, categoria)
                actualizar_registro(RUTA_BIN, posicion, receta)
                recetario.guardar_texto()
                ordenado_por = None
                print("Receta modificada y guardada por acceso directo.")
            else:
                print("Opción inválida.")
        except (ValueError, ItemNoEncontradoError, ArchivoInvalidoError) as error:
            print(error)


def menu_historial():
    while True:
        print("\n1. Registrar receta cocinada\n2. Deshacer última\n3. Ver última\n0. Volver")
        opcion = input("> ").strip()
        if opcion == "0":
            return
        try:
            if opcion == "1":
                receta = recetario.buscar_por_id(pedir_entero("ID de receta: "))
                if receta:
                    historial.registrar(receta)
                    print("Receta registrada en el historial.")
                else:
                    print("No existe esa receta.")
            elif opcion == "2":
                receta = historial.deshacer()
                print(f"Se quitó: {receta.nombre}")
            elif opcion == "3":
                receta = historial.ver_ultima()
                print(f"Última receta: {receta.nombre}")
            else:
                print("Opción inválida.")
        except PilaVaciaError as error:
            print(error)


def menu_cola():
    while True:
        print("\n1. Encolar receta\n2. Preparar próxima\n3. Ver próxima\n0. Volver")
        opcion = input("> ").strip()
        if opcion == "0":
            return
        try:
            if opcion == "1":
                receta = recetario.buscar_por_id(pedir_entero("ID de receta: "))
                if receta:
                    cola_preparacion.encolar_receta(receta)
                    print("Receta agregada a la cola.")
                else:
                    print("No existe esa receta.")
            elif opcion == "2":
                receta = cola_preparacion.siguiente_receta()
                print(f"Preparada: {receta.nombre}")
            elif opcion == "3":
                receta = cola_preparacion.ver_proxima()
                print(f"Próxima: {receta.nombre}")
            else:
                print("Opción inválida.")
        except ColaVaciaError as error:
            print(error)


def menu_archivos():
    global ordenado_por
    while True:
        print("\na) Cargar catálogo desde recetas.txt")
        print("b) Guardar catálogo en recetas.txt")
        print("c) Guardar catálogo en binario")
        print("d) Cargar catálogo desde binario")
        print("0) Volver")
        opcion = input("> ").strip().lower()
        try:
            if opcion == "0":
                return
            if opcion == "a":
                nuevo = Recetario()
                recetario.reemplazar_catalogo(nuevo.catalogo)
                guardar_binario(RUTA_BIN, recetario.catalogo)
                ordenado_por = None
                print(f"Se cargaron {recetario.catalogo.tamanio()} recetas desde texto.")
            elif opcion == "b":
                recetario.guardar_texto()
                print("Catálogo guardado en texto.")
            elif opcion == "c":
                guardar_binario(RUTA_BIN, recetario.catalogo)
                print("Catálogo guardado en binario.")
            elif opcion == "d":
                nuevo_catalogo = cargar_binario(RUTA_BIN)
                recetario.reemplazar_catalogo(nuevo_catalogo)
                ordenado_por = None
                print(f"Se cargaron {recetario.catalogo.tamanio()} recetas desde binario.")
            else:
                print("Opción inválida.")
        except (ArchivoInvalidoError, OSError) as error:
            print(f"Archivo inválido: {error}")


def main():
    global ordenado_por
    while True:
        mostrar_menu()
        opcion = input("> ").strip()
        try:
            if opcion == "0":
                print("Hasta luego.")
                break
            elif opcion == "1":
                recetario.mostrar_catalogo()
            elif opcion == "2":
                menu_detalle()
            elif opcion == "3":
                menu_busqueda()
            elif opcion == "4":
                menu_ordenar()
            elif opcion == "5":
                id_receta = pedir_entero("ID de la receta para recorrer sus subrecetas: ")
                receta = recetario.buscar_por_id(id_receta)
                if receta:
                    mostrar_receta_completa(receta)
                    print("\nIngredientes totales:", ", ".join(obtener_ingredientes_totales(receta)))
                else:
                    print("No existe esa receta.")
            elif opcion == "6":
                menu_abm()
            elif opcion == "7":
                menu_historial()
            elif opcion == "8":
                menu_cola()
            elif opcion == "9":
                menu_archivos()
            else:
                print("Opción inválida.")
        except (ArchivoInvalidoError, OSError) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    main()
