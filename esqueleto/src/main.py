from src.config import TEMA
from src.dominio.recetario import Mostrar_catalogo, buscar_receta_por_id
from src.dominio.menu_semanal import MenuSemanal
from src.dominio.historial import HistorialCocina
from src.dominio.cola_preparacion import ColaPreparacion
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}
#Instancias globales del dominio, se colocan aca para que todas las funciones puedan acceder a ellas.
menu_semanal = MenuSemanal()
historial = HistorialCocina()
cola_preparacion = ColaPreparacion()

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")
#Definimos el menu para el menu semanal, permite agregar, eliminar y listar recetas.
def menu_menu_semanal():
    while True:
        print("=== Menú semanal ===")
        print("1. Agregar receta")
        print("2. Eliminar receta")
        print("3. Listar recetas")
        print("0. Volver al menú principal")
        
        opcion = input("> ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            try:
                receta_id = int(input("Ingrese el ID de la receta a agregar: "))
                receta = buscar_receta_por_id(receta_id)
                if receta:
                    menu_semanal.agregar(receta)
                    print(f"Receta '{receta.nombre}' agregada al menú semanal.")
                else:
                    print("Receta no encontrada.")
            except ColeccionLlenaError as e:
                print(f"{e}")
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == "2":
            try:
                receta_id = int(input("Ingrese el ID de la receta a eliminar: "))
                receta = buscar_receta_por_id(receta_id)
                if receta:
                    menu_semanal.eliminar(receta)
                    print(f"Receta '{receta.nombre}' eliminada del menú semanal.")
                else:
                    print("Receta no encontrada.")
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == "3":
            print("Recetas en el menú semanal:")
            menu_semanal.listar()

def menu_historial():
    while True:
        print("=== Historial de cocina ===")
        print("1. Registrar receta cocinada")
        print("2. Deshacer última receta cocinada")
        print("3. Ver última receta cocinada")
        print("0. Volver al menú principal")
        
        opcion = input("> ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            try:
                receta_id = int(input("Ingrese el ID de la receta cocinada: "))
                receta = buscar_receta_por_id(receta_id)
                if receta:
                    historial.registrar(receta)
                    print(f"Receta '{receta.nombre}' registrada en el historial.")
                else:
                    print("Receta no encontrada.")
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == "2":
            try:
                receta = historial.deshacer()
                if receta:
                    print(f"Receta '{receta.nombre}' eliminada del historial.")
                else:
                    print("No hay recetas en el historial.")
            except PilaVaciaError as e:
                print(f"{e}")
        elif opcion == "3":
            try:
                receta = historial.ver_ultima()
                if receta:
                    print(f"Última receta cocinada: '{receta.nombre}'.")
                else:
                    print("No hay recetas en el historial.")
            except PilaVaciaError as e:
                print(f"{e}")
def menu_cola_preparacion():
    while True:
        print("=== Cola de preparación ===")
        print("1. Agregar receta a preparar")
        print("2. Preparar próxima receta")
        print("3. Ver próxima receta a preparar")
        print("0. Volver al menú principal")

        opcion = input("> ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            try:
                receta_id = int(input("Ingrese el ID de la receta a agregar: "))
                receta = buscar_receta_por_id(receta_id)
                if receta:
                    cola_preparacion.encolar_receta(receta)
                    print(f"Receta '{receta.nombre}' agregada a la cola de preparación.")
                else:
                    print("Receta no encontrada.")
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == "2":
            try:
                receta = cola_preparacion.siguiente_receta()
                print(f"Receta '{receta.nombre}' preparada.")
            except ColaVaciaError as e:
                print(f"{e}")
        elif opcion == "3":
            try:
                receta = cola_preparacion.ver_proxima()
                print(f"Próxima receta a preparar: '{receta.nombre}'.")
            except ColaVaciaError as e:
                print(f"{e}")
def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            Mostrar_catalogo() 
        elif opcion == "5":
            buscar_receta_por_id()
        elif opcion == "6":
            menu_menu_semanal()
        elif opcion == "7":
            menu_historial()
        elif opcion == "8":
            menu_cola_preparacion()
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
