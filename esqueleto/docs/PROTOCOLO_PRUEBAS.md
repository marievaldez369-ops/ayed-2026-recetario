# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Nota: las pruebas anteriores de E3 se identifican como E3-P09 a E3-P12 para reservar P09–P12 a los casos de E4 indicados en la guía.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | catálogo inicial | lista no vacía, sin traceback | pasa | Se mostró el catálogo sin errores. |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | no corrido |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ID 4, Pizza margarita | imprime la cadena completa | pasa | Mostró la receta y sus dos subrecetas. |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | ID 1, Milanesa con puré | solo el ítem (caso base) | pasa | Mostró la receta sin subrecetas. |
| P05 | E2 | Seleccionar opción 5 del menú y escribir un valor no numérico | x | Mensaje de error "Ingrese un número válido. Por favor." | pasa | Mostró el mensaje y volvió al menú. |
| P06 | E2 | Seleccionar opción 5 del menú y escribir un número que no corresponde a ninguna receta | 999 | Mensaje de error "No se encontró esa receta en el catálogo." | pasa | Mostró el mensaje y volvió al menú. |
| P07 | E2 | Seleccionar opción 5 del menú y elegir la receta con ID 4. | ID 4 | Lista de ingredientes, y las subrecetas. | pasa | Mostró ingredientes, masa casera y salsa de tomate. |
| P08 | E2 | Seleccionar opción 5 del menú y presionar Enter sin escribir nada. | entrada vacía | Mensaje de  error "Ingrese un número válido. Por favor." | pasa | Mostró el mensaje y volvió al menú. |
| E3-P09 | E3 |Seleccionar la opción 1 y agregar una receta al menú. | "milanesa" | La receta se agrega correctamente al menú semanal. | pasa | El sistema confirmó el agregado de la receta. |
| E3-P10 | E3 | Seleccionar la opción 2 para listar el menú. | Menú con la receta "milanesa". | Se muestra la receta cargada en el menú semanal. | pasa | La receta apareció correctamente en el listado. |
| E3-P11 | E3 | Seleccionar la opción 3 para deshacer la última receta agregada. | "milanesa" | Se muestra la última receta almacenada en la pila. | pasa | Se verificó el funcionamiento LIFO de la pila. |
| E3-P12 | E3 | Seleccionar la opción 4 para preparar la siguiente receta. | "milanesa" | Se procesa la primera receta agregada a la cola. | pasa | Se verificó el funcionamiento FIFO de la cola. |
| P09 | E4 | Búsqueda lineal de un nombre que existe | Pizza margarita | lo encuentra | pasa | Se encontró la receta. |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | Sushi | no encontrado, sin traceback | pasa | Mostró el mensaje de receta no encontrada y el menú siguió. |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | Pizza margarita | avisa o reordena; no da un falso hit | pasa | Ordenó por nombre, avisó y encontró la receta. |
| P12 | E4 | Ordenar por un criterio y después por otro | Nombre y luego ID | el orden cambia | pasa | Se verificaron ambos ordenamientos desde el menú. |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
