# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa |  |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) |  |  |
| P05 | E2 | Seleccionar opción 5 del menú y escribir un valor no numérico |  | Mensaje de error "Ingrese un número válido. Por favor." |  |  |
| P06 | E2 | Seleccionar opción 5 del menú y escribir un número que no corresponde a ninguna receta |  | Mensaje de error "No se encontró esa receta en el catálogo." |  |  |
| P07 | E2 | Seleccionar opción 5 del menú y elegir la receta con ID 4. |  | Lista de ingredientes, y las subrecetas. |  |  |
| P08 | E2 | Seleccionar opción 5 del menú y presionar Enter sin escribir nada. |  | Mensaje de  error "Ingrese un número válido. Por favor." |  |  |
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
