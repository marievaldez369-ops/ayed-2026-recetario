class Receta:
    def __init__(self, id_receta, nombre, tiempo_min=0, dificultad="", categoria="",
                 ingredientes=None, subrecetas=None):
        self.id = int(id_receta)
        self.nombre = nombre
        self.tiempo_min = int(tiempo_min)
        self.dificultad = dificultad
        self.categoria = categoria
        self.ingredientes = ingredientes or []
        self.subrecetas = subrecetas or []

    def resumen(self):
        return f"{self.id} - {self.nombre}"

