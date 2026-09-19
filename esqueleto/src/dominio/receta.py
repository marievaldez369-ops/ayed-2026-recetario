class Receta: 
  def __init__(self, id_receta, nombre, ingrediente=None, subreceta=None)
  self.id = = id_receta
        self.nombre = nombre
        self.ingredientes = ingredientes or []
        self.subrecetas = subrecetas or []

    def resumen(self):
        return f"{self.id} - {self.nombre}"

