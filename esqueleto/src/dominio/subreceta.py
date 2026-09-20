class Subreceta:
  def __init__ (self, id_receta, nombre, ingredientes=None, subrecetas=None):
    self.id = id_receta
    self.nombre = nombre
    self.ingredientes = ingredientes or []
    self.subrecetas = subrecetas or []

  def resumen(self):
    return f"{self.id} - {self.nombre}" 

def obtener_ingredientes_totales(receta, recetario=None):
  ingredientes = list(receta.ingredientes)

  for subrecetas in receta.subrecetas:
    ingredientes.extend (
      obtener_ingredientes_totales(subreceta, recetario)
    )
    
  return ingredientes


