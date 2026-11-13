# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Nota: las pruebas anteriores de E3 se identifican como E3-P09 a E3-P12 para reservar P09–P12 a los casos de E4 indicados en la guía.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo. | Catálogo inicial | Lista no vacía, sin traceback. | pasa | Se mostró el catálogo sin errores. |
| P02 | E1 | Elegir un ítem inexistente. | ID = -1 | Mensaje claro, el menú sigue funcionando. | no corrido | |
| P03 | E2 | Ejecutar la operación recursiva sobre un ítem con cadena de subrecetas. | ID 4, Pizza margarita | Imprime la cadena completa. | pasa | Mostró la receta y sus dos subrecetas. |
| P04 | E2 | Ejecutar la operación recursiva sobre un ítem sin derivados. | ID 1, Milanesa con puré | Muestra solo el ítem (caso base). | pasa | Mostró la receta sin subrecetas. |
| P05 | E2 | Seleccionar la opción 5 del menú e ingresar un valor no numérico. | `x` | Mensaje de error: "Ingrese un número válido. Por favor." | pasa | Mostró el mensaje y volvió al menú. |
| P06 | E2 | Seleccionar la opción 5 del menú e ingresar un número que no corresponde a ninguna receta. | `999` | Mensaje de error: "No se encontró esa receta en el catálogo." | pasa | Mostró el mensaje y volvió al menú. |
| P07 | E2 | Seleccionar la opción 5 del menú y elegir la receta con ID 4. | ID 4 | Muestra los ingredientes y las subrecetas. | pasa | Mostró ingredientes, masa casera y salsa de tomate. |
| P08 | E2 | Seleccionar la opción 5 del menú y presionar Enter sin escribir nada. | Entrada vacía | Mensaje de error: "Ingrese un número válido. Por favor." | pasa | Mostró el mensaje y volvió al menú. |
| E3-P09 | E3 | Seleccionar la opción 1 y agregar una receta al menú. | Milanesa | La receta se agrega correctamente al menú semanal. | pasa | El sistema confirmó el agregado de la receta. |
| E3-P10 | E3 | Seleccionar la opción 2 para listar el menú. | Menú con la receta Milanesa | Se muestra la receta cargada en el menú semanal. | pasa | La receta apareció correctamente en el listado. |
| E3-P11 | E3 | Seleccionar la opción 3 para deshacer la última receta agregada. | Milanesa | Se muestra la última receta almacenada en la pila. | pasa | Se verificó el funcionamiento LIFO de la pila. |
| E3-P12 | E3 | Seleccionar la opción 4 para preparar la siguiente receta. | Milanesa | Se procesa la primera receta agregada a la cola. | pasa | Se verificó el funcionamiento FIFO de la cola. |
| P09 | E4 | Realizar una búsqueda lineal de un nombre existente. | Pizza margarita | Encuentra y muestra la receta. | pasa | Verificado con ejecución automatizada del menú. |
| P10 | E4 | Realizar una búsqueda lineal de un nombre inexistente. | Sushi | Informa que no se encontró, sin traceback. | pasa | Verificado con ejecución automatizada del menú. |
| P11 | E4 | Intentar una búsqueda binaria con el catálogo desordenado por nombre. | Pizza margarita | Avisa que debe ordenarse por nombre o realiza el ordenamiento antes de buscar; no devuelve un resultado incorrecto. | pasa | El menú avisa que primero debe ordenarse por nombre y no ejecuta la búsqueda binaria. |
| P12 | E4 | Ordenar por un criterio y luego por otro. | Nombre y luego ID | El orden del catálogo cambia según el criterio seleccionado. | pasa | Se verificaron los algoritmos y la actualización del orden del catálogo. |
| P13 | E5 | Guardar el catálogo en formato de texto, cerrar el programa, volver a ejecutarlo y cargar el archivo. | `recetas.txt` con 30 recetas | Se recuperan las recetas guardadas y se conserva la información. | pasa | Se informó la carga de 30 recetas desde el archivo de texto. |
| P14 | E5 | Guardar el catálogo en binario, modificar una receta por ID y volver a cargar el archivo binario. | ID 3, Sofrito. Cambiar tiempo de 25 a 30 minutos. | Al recargar el archivo, la receta conserva el nuevo valor. | pasa | Se modificó Sofrito, se recargaron las 30 recetas y se comprobó que el tiempo quedó en 30 minutos. |
| P15 | E5 | Intentar cargar un archivo binario con una magia incorrecta. | Archivo binario con encabezado inválido. | Se informa que el archivo es inválido, sin traceback. | pasa | Mostró: "Archivo inválido: Magia incorrecta: el archivo no pertenece al TP." |
| P16 | E5 | Intentar cargar un archivo binario truncado o incompleto. | Copia de un binario válido a la que se le quitaron bytes. | Se informa que el archivo es inválido, sin traceback. | no corrido | Pendiente de ejecutar con una copia para conservar el archivo binario válido. |
| P17 | E5 | Intentar cargar un archivo de texto con encabezado o registros incorrectos. | Copia de `recetas.txt` con datos alterados. | Se informa que el archivo es inválido, sin traceback. | no corrido | Pendiente de ejecutar con una copia para conservar el archivo original. |
| E6-P18 | E6 | Iniciar el programa y listar el catálogo. | Dataset inicial de la cátedra | Se muestran las recetas disponibles sin errores. | no corrido | Prueba de regresión del catálogo. |
| E6-P19 | E6 | Buscar una receta existente mediante búsqueda lineal. | Chimichurri | Se encuentra la receta correcta. | no corrido | Prueba de regresión de búsqueda lineal. |
| E6-P20 | E6 | Buscar una receta inexistente mediante búsqueda lineal. | Sushi | Se informa que no se encontró la receta, sin traceback. | no corrido | Prueba de regresión de búsqueda lineal. |
| E6-P21 | E6 | Ordenar el catálogo por nombre y realizar una búsqueda binaria. | Chimichurri | Se encuentra la receta correcta. | no corrido | La búsqueda binaria debe realizarse sobre el catálogo ordenado por nombre. |
| E6-P22 | E6 | Intentar una búsqueda binaria sin ordenar previamente por nombre. | Chimichurri | El sistema advierte que debe ordenar el catálogo antes de buscar. | no corrido | Prueba de validación del requisito de ordenamiento. |
| E6-P23 | E6 | Ordenar el catálogo por tiempo de preparación. | Catálogo completo | Las recetas quedan ordenadas de menor a mayor tiempo. | no corrido | Prueba de regresión del algoritmo de ordenamiento. |
| E6-P24 | E6 | Ordenar el catálogo por nombre. | Catálogo completo | Las recetas quedan ordenadas alfabéticamente. | no corrido | Prueba de regresión del algoritmo de ordenamiento. |
| E6-P25 | E6 | Ejecutar la operación recursiva sobre una receta con subrecetas. | Hamburguesa casera | Se muestra la receta y toda su cadena de subrecetas. | no corrido | Prueba de regresión de recursión. |
| E6-P26 | E6 | Ejecutar la operación recursiva sobre una receta sin subrecetas. | Receta sin derivados | Se muestra la receta y finaliza correctamente. | no corrido | Prueba de regresión del caso base. |
| E6-P27 | E6 | Agregar dos recetas a la pila y consultar o desapilar el último elemento. | Dos recetas diferentes | Se obtiene primero la última receta agregada. | no corrido | Comprueba el comportamiento LIFO de la pila. |
| E6-P28 | E6 | Desapilar elementos hasta dejar la pila vacía e intentar desapilar nuevamente. | Pila vacía | El sistema informa que no hay elementos, sin producir errores inesperados. | no corrido | Comprueba el manejo de pila vacía. |
| E6-P29 | E6 | Encolar dos recetas y procesar la siguiente. | Dos recetas diferentes | Se procesa primero la receta que ingresó primero. | no corrido | Comprueba el comportamiento FIFO de la cola. |
| E6-P30 | E6 | Procesar elementos hasta dejar la cola vacía e intentar desencolar nuevamente. | Cola vacía | El sistema informa que no hay elementos, sin producir errores inesperados. | no corrido | Comprueba el manejo de cola vacía. |
| E6-P31 | E6 | Guardar el catálogo en texto, salir del programa, volver a ingresar y cargar el archivo. | `recetas.txt` | Se recuperan las recetas y sus datos correctamente. | no corrido | Prueba de regresión de persistencia en texto. |
| E6-P32 | E6 | Guardar el catálogo en binario, modificar un registro, volver a cargarlo y consultar la receta modificada. | ID 3, Sofrito | El cambio realizado se conserva después de cargar nuevamente el archivo. | no corrido | Prueba de regresión de persistencia binaria y modificación de registros. |
