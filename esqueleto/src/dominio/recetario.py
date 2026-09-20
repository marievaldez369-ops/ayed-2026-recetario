
from src.dominio.receta import Receta
from src.dominio.subreceta import Subreceta, obtener_ingredientes_totales

class Recetario:
    def __init__(self):
        self.recetas = {}
        self._cargar_iniciales()

    def _cargar_iniciales(self):


#sub-recetas
        masa_casera = Subreceta(
            5, "Masa casera", 
            ["harina", "agua", "levadura", "sal"])
        salsa_tomate = Subreceta(
            6, "Salsa de tomate", 
            ["tomate", "ajo", "condimentos"])
        medallon = Subreceta(
            9, "Medallón de carne casero",
            ["carne picada", "huevo", "pan rallado", "sal", "pimienta"])
        pan = Subreceta(
            10, "Pan de hamburguesa casero",
            ["harina", "levadura", "agua", "azúcar", "sal", "manteca", "huevo"])

#recetas simples
        milanesa = Receta(
            1, "Milanesa con puré", 
            ["carne", "pan rallado", "huevo", "papas"])
        tarta = Receta(
            2, "Tarta de jamón y queso", 
            ["masa", "jamón", "queso", "huevo"])
        ensalada = Receta(
            3, "Ensalada César", 
            ["lechuga", "pollo", "crutones", "queso parmesano"])
      

#recetas con sub-recetas
        pizza = Receta(
            4, "Pizza margarita", 
            ["mozzarella", "albahaca"], [masa_casera, salsa_tomate])
        hamburguesa = Receta(
            11, "Hamburguesa completa", 
            ["lechuga", "tomate", "queso"], [medallon, pan])

#catalogo de recetas
        self.agregar_receta(milanesa)
        self.agregar_receta(tarta)
        self.agregar_receta(ensalada)
        self.agregar_receta(pizza)
        self.agregar_receta(masa_casera)
        self.agregar_receta(salsa_tomate)
        self.agregar_receta(medallon)
        self.agregar_receta(pan)
        self.agregar_receta(hamburguesa)

    def agregar_receta(self, receta):
        self.recetas[receta.id] = receta

    def mostrar_catalogo(self):
        print("Catálogo de Recetas:")
        for receta in self.recetas.values():
            print(receta.resumen())



#catalogo para el menu 
_recetario_global = None

def Mostrar_catalogo():
    global _recetario_global
    if _recetario_global is None:
        _recetario_global = Recetario()
    _recetario_global.mostrar_catalogo()

def mostrar_receta_completa(receta, nivel=0):
    sangria = "    " * nivel

    print(f"\n{ sangria}--- {receta.nombre.upper()} ---")

    if receta.ingredientes:
        print(f"{sangria}Ingredientes:")

        for ingrediente in receta.ingredientes:
            print(f"{sangria}- {ingrediente}")

    for subreceta in receta.subrecetas:
        print(f"\n{sangria}SUB-RECETA: {subreceta.nombre.upper()}")

        print(f"{sangria}Ingredientes:")

        for ingrediente in subreceta.ingredientes:
            print(f"{sangria}- {ingrediente}")

        if subreceta.subrecetas:
            mostrar_receta_completa(subreceta, nivel + 1)


def buscar_receta_por_id():
    global _recetario_global

    if _recetario_global is None:
        _recetario_global = Recetario()

    try:
        print("\nIngrese el número de la receta que desea consultar:")
        opcion = input("> ").strip()

        id_receta = int(opcion)
        receta = _recetario_global.recetas.get(id_receta)

        if receta:
            mostrar_receta_completa(receta)

        else:
            print("No se encontró esa receta en el catálogo.")

    except ValueError:
        print("Ingrese un número válido. Por favor.")
