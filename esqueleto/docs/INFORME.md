# Informe del TP

## 1. Grupo y tema

- **Tema:** Recetario.
- **Motivo de elección:** Elegimos trabajar con un recetario porque cocinar y consultar recetas son actividades cotidianas. El tema permite representar información relacionada, como recetas, ingredientes y subrecetas, y organizarla mediante estructuras de datos. Además, ofrece ejemplos concretos para aplicar los contenidos de la materia y probar las operaciones del sistema con información de recetas.

## 2. Modelo

Un elemento del catálogo es una instancia de `Receta`. Cada receta contiene un identificador, nombre, tiempo de preparación, dificultad, categoría, una lista de ingredientes y una lista de subrecetas.

- **Datos mutables:** el catálogo, las listas de ingredientes y las listas de subrecetas pueden modificarse durante la ejecución. Los atributos de una receta también se actualizan en las operaciones de modificación.
- **Datos inmutables:** los valores de tipo `str`, `int` y otros tipos escalares son inmutables como objetos de Python. Sin embargo, eso no significa que los atributos de una receta sean inmutables: el programa puede asignarles nuevos valores.

**Relación entre las estructuras:**

- `Recetario` administra el catálogo, que se almacena en una `ListaEnlazada` de objetos `Receta`.
- Cada objeto `Receta` puede contener ingredientes y referencias a otras recetas que funcionan como subrecetas.
- `HistorialCocina` utiliza una `Pila` para registrar recetas cocinadas y permitir consultar o deshacer la última acción (LIFO).
- `ColaPreparacion` utiliza una `Cola` para organizar las recetas pendientes de preparación (FIFO).
- `MenuSemanal` permanece como módulo del proyecto, pero no es utilizado por el menú principal actual.

## 3. Recursión (E2)

El proyecto utiliza las funciones `mostrar_receta_completa()` y `obtener_ingredientes_totales()` para recorrer una receta y sus subrecetas de forma recursiva.

- **Caso base:** una receta no tiene subrecetas. Se muestran o se devuelven sus propios ingredientes y termina ese recorrido.
- **Caso recursivo:** si una receta tiene subrecetas, se llama nuevamente a la función para recorrer cada una de ellas.

**Ejemplo con el dataset incluido en esta versión:**

- Receta principal: `Hamburguesa casera` (ID 27).
- Subreceta asociada: `Pico de gallo` (ID 8).
- La operación muestra los datos e ingredientes de la hamburguesa y luego recorre la subreceta Pico de gallo.

Como ejemplo de caso base se puede utilizar `Chimichurri` (ID 1), que no tiene subrecetas asociadas.

## 4. TADs (E3)

| TAD | Operaciones utilizadas | Invariante / comportamiento |
| --- | --- | --- |
| Lista enlazada | Insertar al final, buscar, eliminar y recorrer | Los nodos se enlazan mediante referencias al siguiente nodo y el tamaño se mantiene actualizado. |
| Pila | Apilar, desapilar, consultar el tope y comprobar si está vacía | LIFO: el último elemento agregado es el primero en salir. |
| Cola | Encolar, desencolar, consultar el frente y comprobar si está vacía | FIFO: el primer elemento agregado es el primero en salir. |

**Uso en el dominio:** la lista enlazada almacena las recetas del catálogo; la pila se utiliza en `HistorialCocina` para registrar recetas cocinadas; y la cola se utiliza en `ColaPreparacion` para administrar las recetas pendientes respetando el orden de llegada.

## 5. Complejidad (E4)

En la tabla, `n` representa la cantidad de recetas del catálogo, `m` la cantidad total de recetas y subrecetas visitadas en un recorrido recursivo, y `h` la profundidad máxima de la recursión.

| Operación | Tiempo | Espacio adicional | Justificación |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre una vez las recetas para mostrarlas. |
| Búsqueda lineal | O(1) mejor / O(n) peor | O(1) | Puede encontrar el primer elemento; en el peor caso recorre toda la colección. |
| Preparar colección para búsqueda binaria | O(n) | O(n) | El menú convierte la lista enlazada en una lista de Python para poder acceder por índice. |
| Búsqueda binaria | O(log n) | O(1) | En cada comparación descarta aproximadamente la mitad del rango. La colección debe estar ordenada por la misma clave utilizada en la búsqueda. |
| Búsqueda binaria desde el menú, incluyendo la conversión | O(n) | O(n) | El costo de convertir el catálogo a lista domina al costo O(log n) del algoritmo binario. |
| Ordenamiento por selección | O(n²) | O(1) | Compara los elementos restantes para seleccionar el menor de cada posición. |
| Ordenamiento por inserción | O(n) mejor / O(n²) promedio y peor | O(1) | Si la colección ya está ordenada realiza pocas comparaciones; en el peor caso desplaza muchos elementos. |
| Mostrar receta completa recursivamente | O(m) | O(h) | Visita cada receta/subreceta alcanzable una vez y utiliza la pila de llamadas hasta la profundidad máxima. |
| Obtener ingredientes totales recursivamente | O(m) | O(m) para la lista resultado, más O(h) de llamadas | Recorre las recetas y construye una lista con los ingredientes reunidos. |
| Alta o baja de receta en el catálogo | O(n) | O(1) adicional | Primero se busca la receta o se verifica que el ID no exista; la búsqueda domina el costo. |
| Modificar receta | O(n) | O(1) adicional | Se busca la receta por ID y luego se actualizan sus atributos. |
| Apilar, desapilar o consultar el tope | O(1) | O(1) adicional por operación | La pila enlazada opera sobre el extremo superior. |
| Encolar, desencolar o consultar el frente | O(1) | O(1) adicional por operación | La cola mantiene referencias a sus extremos y opera sobre ellos. |

**Mediciones de E4:** el registro de mediciones que se conserva en esta versión corresponde a las pruebas realizadas entonces con un catálogo de 9 elementos y una copia de 90 elementos. No se deben interpretar como mediciones sobre las 30 recetas del dataset que acompaña a esta versión. Para búsquedas se promediaron 1.000 ejecuciones buscando un nombre inexistente; para cada ordenamiento se promediaron 10 ejecuciones sobre copias nuevas. Los tiempos dependen del equipo.

| Operación | n | Segundos promedio por ejecución |
| --- | ---: | ---: |
| Búsqueda lineal (nombre inexistente) | 9 | 0.000000463 |
| Búsqueda lineal (nombre inexistente) | 90 | 0.000003482 |
| Búsqueda binaria (nombre inexistente, colección ordenada) | 9 | 0.000000574 |
| Búsqueda binaria (nombre inexistente, colección ordenada) | 90 | 0.000000921 |
| Ordenamiento por selección (nombre) | 9 | 0.000006745 |
| Ordenamiento por selección (nombre) | 90 | 0.000329847 |
| Ordenamiento por inserción (ID) | 9 | 0.000001350 |
| Ordenamiento por inserción (ID) | 90 | 0.000172881 |

## 6. Persistencia (E5)

El sistema permite guardar y recuperar los datos del catálogo mediante un archivo de texto y un archivo binario.

### Persistencia en texto

- El archivo `data/recetas.txt` almacena los campos `id`, `nombre`, `tiempo_min`, `dificultad` y `categoria`.
- Se utiliza el módulo `csv` de Python y una fila de encabezados.
- Al cargar, se valida que el encabezado coincida, que los registros tengan la cantidad correcta de campos, que no haya campos vacíos, que los ID sean enteros positivos y únicos y que el tiempo sea un entero no negativo.

### Layout del registro binario

Se utiliza `struct.Struct("<I30sH10s15s")`. El prefijo `<` indica orden little-endian y tamaños estándar sin alineación nativa.

| Campo | Código `struct` | Tamaño |
| --- | --- | ---: |
| ID | `I` | 4 bytes |
| Nombre | `30s` | 30 bytes |
| Tiempo de preparación | `H` | 2 bytes |
| Dificultad | `10s` | 10 bytes |
| Categoría | `15s` | 15 bytes |
| **Total por registro** | | **61 bytes** |

Los campos de texto se codifican en UTF-8 y se completan con bytes nulos (`\0`) hasta alcanzar el ancho establecido. Si el texto supera el ancho disponible, la escritura se rechaza.

### Header

La cabecera utiliza `struct.Struct("<4s1sI")` y ocupa 9 bytes.

| Campo | Valor / función | Tamaño |
| --- | --- | ---: |
| Magia | `AYED`, identifica el formato del TP | 4 bytes |
| Tema | `R`, identifica el tema Recetario | 1 byte |
| Cantidad | Cantidad de registros almacenados | 4 bytes |
| **Total** | | **9 bytes** |

### Actualización de un registro por posición

La función `actualizar_registro()` abre el archivo en modo `r+b`, valida el header y el tamaño total, calcula el desplazamiento del registro y utiliza `seek()` para escribir únicamente en esa posición.

La posición inicial de un registro se calcula así:

`HEADER.size + posicion * FORMATO.size`

Como el header ocupa 9 bytes y cada registro ocupa 61 bytes, el desplazamiento se obtiene a partir del número de registro y del tamaño fijo del registro.

### Manejo de archivos inválidos

Se utiliza `ArchivoInvalidoError` para informar problemas de lectura o escritura. Entre las validaciones implementadas se encuentran:

- Header binario incompleto.
- Magia incorrecta o tema distinto de Recetario.
- Tamaño binario que no coincide con la cantidad indicada en el header.
- Archivo de texto inexistente, encabezado incorrecto, campos vacíos o cantidad incorrecta de campos.
- ID repetido o no válido y tiempo negativo en el archivo de texto.

### Estado de las pruebas de persistencia

Los resultados marcados como aprobados se verificaron mediante pruebas automatizadas de las funciones de persistencia y del modelo. Esto comprueba la lógica involucrada, aunque no equivale a ejecutar manualmente todos los pasos desde el menú CLI.

| Prueba | Descripción | Estado documentado |
| --- | --- | --- |
| P13 | Guardar en texto y recuperar los datos desde una nueva instancia de `Recetario`. | Pasa: se guardó el TXT y una nueva instancia recuperó los 30 registros. No se simuló el cierre completo de la aplicación. |
| P14 | Guardar en binario, modificar Sofrito (ID 3) de 25 a 30 minutos y volver a cargar. | Pasa según la ejecución informada: se recargaron 30 recetas y Sofrito conservó 30 minutos. El código implementa la actualización mediante `seek()`. |
| P15 | Cargar un binario con magia incorrecta. | Pasa según la ejecución informada: se mostró un mensaje de archivo inválido sin traceback. |
| P16 | Cargar una copia de un binario válido que fue truncada. | Pasa: la carga detectó el tamaño incorrecto y lanzó `ArchivoInvalidoError`, sin aceptar el archivo. |
| P17 | Cargar una copia de `recetas.txt` con encabezado o registro incorrecto. | Pasa: la validación detectó el encabezado incorrecto y lanzó `ArchivoInvalidoError`. |

## 7. Reparto de trabajo (E6)

Este apartado debe completarse con el reparto real del grupo. No se asignan tareas por suposición.

| Integrante | Qué hizo en el proyecto | Qué puede defender en la exposición |
| --- | --- | --- |
| Wendy Patiño Pinto | . | . |
| Mariela Valdez Ibáñez | . | . |
| Natalia Villano | . | . |
