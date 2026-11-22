# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Nota: las pruebas anteriores de E3 se identifican como E3-P09 a E3-P12 para reservar P09–P12 a los casos de E4 indicados en la guía.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar el catálogo. | Catálogo inicial | Lista no vacía, sin traceback. | pasa | Se mostró el catálogo sin errores. |
| P02 | E1 | Elegir un ítem inexistente desde la opción de detalle. | ID = -1 | Mensaje claro y el menú continúa funcionando. | pasa | Verificado en el flujo de `menu_detalle()`: si el ID no existe, informa que no se encontró y vuelve al menú. |
| P03 | E2 | Ejecutar la operación recursiva sobre un ítem con cadena de subrecetas. | ID 4, Pizza margarita (datos de la entrega E2). | Imprime la receta y la cadena de subrecetas. | pasa | Se conserva el resultado informado para E2. No corresponde al dataset actual. |
| P04 | E2 | Ejecutar la operación recursiva sobre un ítem sin derivados. | ID 1, Milanesa con puré (datos de la entrega E2). | Muestra solo el ítem (caso base). | pasa | Se conserva el resultado informado para E2. No corresponde al dataset actual. |
| P05 | E2 | Seleccionar la opción 5 e ingresar un valor no numérico. | `x` | Mensaje de error y retorno al menú. | pasa | Se informó que mostró el mensaje y volvió al menú. |
| P06 | E2 | Seleccionar la opción 5 e ingresar un ID inexistente. | `999` | Mensaje de que no se encontró la receta y retorno al menú. | pasa | Se informó que mostró el mensaje y volvió al menú. |
| P07 | E2 | Seleccionar la opción 5 y elegir una receta con subrecetas. | ID 4, según el dataset de E2. | Muestra ingredientes y subrecetas. | pasa | Se conserva el resultado informado para E2. No corresponde al dataset actual. |
| P08 | E2 | Seleccionar la opción 5 y presionar Enter sin escribir nada. | Entrada vacía | Mensaje de entrada inválida y retorno al menú. | pasa | Se informó que mostró el mensaje y volvió al menú. |
| E3-P09 | E3 | Seleccionar la opción 1 y agregar una receta al menú semanal. | Milanesa | La receta se agrega correctamente. | pasa | Resultado histórico informado para E3. |
| E3-P10 | E3 | Seleccionar la opción 2 para listar el menú semanal. | Menú con Milanesa | Se muestra la receta cargada. | pasa | Resultado histórico informado para E3. |
| E3-P11 | E3 | Seleccionar la opción 3 para deshacer la última receta agregada. | Milanesa | Se obtiene la última receta almacenada en la pila. | pasa | Resultado histórico informado para E3; comprueba LIFO. |
| E3-P12 | E3 | Seleccionar la opción 4 para preparar la siguiente receta. | Milanesa | Se procesa la primera receta agregada a la cola. | pasa | Resultado histórico informado para E3; comprueba FIFO. |
| P09 | E4 | Realizar una búsqueda lineal de un nombre existente. | Chimichurri | Encuentra y muestra la receta correcta. | pasa | Se reemplazó Pizza margarita porque no existe con ese nombre en el dataset actual. La búsqueda se había verificado con ejecución automatizada del menú. |
| P10 | E4 | Realizar una búsqueda lineal de un nombre inexistente. | Sushi | Informa que no se encontró, sin traceback. | pasa | Verificado con ejecución automatizada del menú. |
| P11 | E4 | Intentar una búsqueda binaria sin haber ordenado previamente por nombre. | Chimichurri | Avisa que primero debe ordenarse por nombre y no ejecuta una búsqueda que pueda dar un resultado incorrecto. | pasa | El menú mostró el aviso correspondiente. |
| P12 | E4 | Ordenar por nombre y luego por tiempo de preparación. | Catálogo completo | El orden cambia de acuerdo con cada criterio seleccionado. | pasa | Se verificaron ambos algoritmos y la actualización del orden del catálogo. |
| P13 | E5 | Guardar el catálogo en texto y crear una nueva instancia del recetario para recuperar el archivo. | `data/recetas.txt`, 30 recetas | Se recuperan las recetas y sus datos desde el TXT guardado. | pasa | Verificado con guardado y carga desde una nueva instancia de `Recetario`; se recuperaron los 30 registros. No se simuló el cierre completo de la aplicación. |
| P14 | E5 | Guardar el catálogo en binario, modificar una receta por ID y volver a cargar el archivo binario. | ID 3, Sofrito; cambiar 25 a 30 minutos. | Al recargar, Sofrito conserva 30 minutos. | pasa | Se informó que se modificó Sofrito, se recargaron 30 recetas y el detalle mostró 30 minutos. El código utiliza `seek()` en `actualizar_registro()`. |
| P15 | E5 | Intentar cargar un archivo binario con magia incorrecta. | Copia de un archivo binario con header alterado. | Informa que el archivo es inválido, sin traceback. | pasa | Se informó el mensaje: “Magia incorrecta: el archivo no pertenece al TP”. |
| P16 | E5 | Intentar cargar una copia de un archivo binario válido a la que se le quitaron bytes. | Copia temporal de `recetas.bin` truncada. | Informa que el binario está incompleto o tiene tamaño incorrecto, sin traceback. | pasa | Verificado con una copia temporal truncada; `cargar_binario()` detectó el tamaño incorrecto y lanzó `ArchivoInvalidoError`. |
| P17 | E5 | Intentar cargar una copia de `recetas.txt` con encabezado o cantidad de campos incorrectos. | Copia temporal de `recetas.txt` alterada. | Informa que el archivo de texto es inválido, sin traceback. | pasa | Verificado con un TXT temporal de encabezado incorrecto; `cargar_texto()` detectó la estructura inválida y lanzó `ArchivoInvalidoError`. |
| E6-P18 | E6 | Iniciar el programa y listar el catálogo. | Dataset original de la cátedra. | Se muestran las 30 recetas sin errores. | pasa | Verificado: se cargaron y recorrieron 30 recetas sin errores. |
| E6-P19 | E6 | Elegir búsqueda lineal por nombre. | `Chimichurri` | Se encuentra la receta con ID 1. | pasa | Verificado con búsqueda lineal; devuelve Chimichurri, ID 1. |
| E6-P20 | E6 | Elegir búsqueda lineal por nombre. | `Sushi` | Informa que no se encontró la receta, sin traceback. | pasa | Verificado con búsqueda lineal; devuelve `None` para Sushi. |
| E6-P21 | E6 | Ordenar por nombre y luego elegir búsqueda binaria por nombre. | `Chimichurri` | Se encuentra la receta con ID 1. | pasa | Verificado con el catálogo ordenado alfabéticamente; la búsqueda binaria encuentra Chimichurri, ID 1. |
| E6-P22 | E6 | Sin ordenar por nombre, intentar búsqueda binaria. | `Chimichurri` | Muestra el aviso de que primero debe ordenar por nombre. | pasa | Verificado en la condición de `menu_busqueda()`: sin `ordenado_por == "nombre"`, informa que primero debe ordenar y retorna sin buscar. |
| E6-P23 | E6 | Elegir ordenar por tiempo de preparación. | Catálogo completo. | Las recetas quedan ordenadas de menor a mayor tiempo. | pasa | Verificado mediante ejecución del ordenamiento por inserción; los tiempos quedan de menor a mayor. |
| E6-P24 | E6 | Elegir ordenar por nombre. | Catálogo completo. | Las recetas quedan en orden alfabético. | pasa | Verificado mediante ejecución del ordenamiento por selección; los nombres quedan en orden alfabético. |
| E6-P25 | E6 | Elegir operación recursiva e ingresar el ID de una receta con subreceta. | ID 27, Hamburguesa casera. | Muestra la hamburguesa y su subreceta Pico de gallo (ID 8), incluidos sus ingredientes. | pasa | Verificada la relación del dataset: Hamburguesa casera (ID 27) contiene Pico de gallo (ID 8); la función recursiva recorre la relación. |
| E6-P26 | E6 | Elegir operación recursiva para una receta sin subrecetas. | ID 1, Chimichurri. | Muestra la receta y sus ingredientes; no intenta recorrer subrecetas inexistentes. | pasa | Verificado el caso base: Chimichurri (ID 1) no tiene subrecetas y la función recursiva devuelve sus ingredientes. |
| E6-P27 | E6 | Abrir Historial; registrar dos recetas; consultar la última. | Primero ID 1 y después ID 2. | La última registrada es Salsa criolla (ID 2). | pasa | Verificado con dos registros: `ver_ultima()` devuelve ID 2, el último apilado. |
| E6-P28 | E6 | En Historial, deshacer dos registros y volver a intentar deshacer con la pila vacía. | IDs 1 y 2. | Se quita primero ID 2 y luego ID 1; al vaciarse, muestra un mensaje controlado. | pasa | Verificado el comportamiento LIFO: desapila ID 2 y luego ID 1; la pila queda vacía. |
| E6-P29 | E6 | Abrir Cola; encolar dos recetas y consultar la próxima. | Primero ID 1 y después ID 2. | La próxima receta es Chimichurri (ID 1). | pasa | Verificado con dos elementos: `ver_proxima()` devuelve ID 1, el primero encolado. |
| E6-P30 | E6 | En Cola, preparar dos recetas y volver a intentar preparar con la cola vacía. | IDs 1 y 2. | Se prepara primero ID 1 y luego ID 2; al vaciarse, muestra un mensaje controlado. | pasa | Verificado el comportamiento FIFO: desencola ID 1 y luego ID 2; la cola queda vacía. |
| E6-P31 | E6 | Guardar catálogo en texto, cerrar el programa, volver a iniciarlo y comprobar la carga desde el TXT. | `data/recetas.txt`. | Se recupera la misma cantidad de recetas y los datos guardados. | pasa | Verificado guardando el TXT y creando una nueva instancia de `Recetario`; se recuperan los 30 registros. No se simuló el cierre completo de la aplicación. |
| E6-P32 | E6 | Guardar en binario, modificar Sofrito, cargar el binario y consultar el detalle. | ID 3; tiempo 25 → 30. | Después de cargar, el detalle de Sofrito indica 30 minutos. | pasa | Verificado guardando el binario, actualizando Sofrito (ID 3) de 25 a 30 minutos y recargando; el registro conserva 30 minutos. |

## Observaciones para ejecutar las pruebas E6

- Ejecutar P18–P32 desde una copia limpia del proyecto o restaurar los archivos de datos al finalizar.
- Las operaciones de pila y cola mantienen su estado durante la ejecución del programa; para repetirlas desde cero, reiniciar el programa.
- Para P16 y P17 se utilizaron archivos temporales de prueba; los archivos válidos del proyecto se conservaron.
- Los casos marcados `pasa` con verificación automatizada validan la lógica y los datos de las funciones involucradas; no deben describirse como ejecuciones manuales completas del menú.
