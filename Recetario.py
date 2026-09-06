catalogo = [
    {"nombre": "Milanesa con puré", "ingredientes": ["carne", "pan rallado", "huevo", "papas"]},
    {"nombre": "Tarta de jamón y queso", "ingredientes": ["masa", "jamón", "queso", "huevo"]},
    {"nombre": "Ensalada César", "ingredientes": ["lechuga", "pollo", "crutones", "queso parmesano"]},
    {"nombre": "Pizza margarita", "ingredientes": ["masa", "salsa de tomate", "mozzarella", "albahaca"]}
]

def mostrar_catalogo():
    print("Catálogo de Recetas:")
    for i, receta in enumerate(catalogo, start=1):
        print(f"{i}. {receta['nombre']}")