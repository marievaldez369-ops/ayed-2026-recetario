# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Recetario
- Por qué lo eligieron (5–8 líneas):
-  Elegimos como tema a trabajar el recetario por que cocinar es una labor que hacemos todos los días; planear y buscar recetas es algo habitual y fácil de hacer, además nos permite trabajar con varios elementos, relacionarlo entre sí , de esa manera representar información detallada sobre las recetas, mostrando sus ingredientes y sus pasos a seguir. Al mismo tiempo nos da la posibilidad de aplicar estructuras de datos que vamos aprendiendo en la materia, un recetario nos da un amplio margen de ideas pudiendo agregar mas recetas, sub-recetas o ingredientes sin tener que complicar la búsqueda, también nos resulta entretenido, divertido, cultural y utilizable, lo cual hace mas fácil el trabajo en grupo y que todas podamos probar el sistema con ejemplos reales e incluso poner nuevas ideas de recetas o ingredientes que compartimos en la vida real, pudiendo incluso planear nuestra alimentacion con esta nueva herramienta.
 
## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```
Un item del catálogo sería cada receta individual , compuesta por su nombre y una lista de ingredientes. 

-Mutables: listas y diccionarios(recetas e ingredientes), son dinámicas y pueden cambiar.

-Inmutables: nombre de receta(strings) para evitar efectos secundarios y proteger la identidad de cada receta.

-Relación catálogo/colección/pila/cola:

-El catálogo es la lista principal y almacena las recetas disponibles.

-La colección representa la estructura base que organiza cada receta.

-La pila se usó para administrar los pasos de preparación.

-La cola se usó para manejar tareas en orden.

## 3. Recursión (E2)
- Función: En esta entrega usamos una función recursiva que llamamos mostrar_receta_completa() para descomponer recetas que contiene sub-recetas, la recursión nos permite descomponer sin importar cuantos niveles haya. El objetivo es mostrar cómo una receta puede estar compuesta por más recetas y cómo el programa desglosa todos los ingredientes hasta llegar a las hojas.
  
- Caso Base: Cuando la receta no tiene subrecetas, devuelve sus ingredientes.

- Caso recursivo: Cuando la receta tiene subrecetas, acumula sus ingredientes y sigue explorando cada subreceta hasta terminar y agrega los demás ingredientes.

- Traza de un ejemplo real del dataset:

 Ejemplo paso a paso:

 1- Hamburguesa completa = ingredientes propios: lechuga, tomate, queso.
  
 2- Subreceta Medallón de carne = carne picada, huevo, pan rallado, sal, pimienta.
 
 3- Subreceta Pan casero = harina, levadura, agua, azúcar, sal, manteca, huevo.

Resultado final: combinación de todos los ingredientes.

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar, eliminar, buscar y recorrer |mantenemos los elementos unidos mediante nodos y conservamos el tamaño actualizado de la lista|
| Pila | apilar, desapilar y ver tope |el último elemento agregado es el primero en salir (LIFO)|
| Cola | encolar, desencolar y ver frente|  el primer elemento agregado es el primero en salir (FIFO)|

Dónde se usa cada uno en el dominio.

-En los pasos de preparación de la recta.

- Pedidos de recetas en la cocina.
ListaEnlazada: la usamos para almacenar las recetas del catálogo.
Pila: la usamos para guardar un historial de acciones realizadas.
Cola: la usamos para administrar los pedidos respetando el orden de llegada. 
## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) adicional | Recorre una vez las n recetas para imprimirlas. |
| Búsqueda lineal | O(1) mejor / O(n) peor | O(1) adicional | Puede encontrar el primer elemento; en el peor caso revisa todos. |
| Búsqueda binaria (algoritmo) | O(log n) | O(1) | En cada comparación descarta aproximadamente la mitad del rango. Requiere colección ordenada por la misma clave. |
| Preparar lista para búsqueda binaria desde el catálogo | O(n) | O(n) | El catálogo del dominio es un diccionario y se crea una lista de sus valores para acceder por posición. Por eso, el costo total de esta preparación más la búsqueda es O(n), aunque el algoritmo binario es O(log n). |
| Ordenar por selección | O(n²) | O(1) adicional | Los dos bucles comparan los elementos restantes en cada posición. |
| Ordenar por inserción | O(n) mejor / O(n²) promedio y peor | O(1) adicional | Si ya está ordenada, hace pocas comparaciones; en el peor caso desplaza muchos elementos. |
| Ver detalle recursivo | O(m) | O(h) de pila | Visita cada receta/subreceta alcanzable una vez; h es la profundidad máxima de anidamiento. |
| Agregar/eliminar en menú semanal | O(n) | O(1) adicional | La estructura busca la receta a través de sus elementos antes de modificarla. |
| Registrar/deshacer historial (pila) | O(1) | O(1) adicional por operación | Apilar y desapilar operan en el tope de la pila. |
| Encolar/desencolar preparación (cola) | O(1) | O(1) adicional por operación | Las operaciones actúan sobre los extremos de la cola. |

Mediciones con `time.perf_counter`: se usó el catálogo inicial de 9 elementos y una copia repetida 10 veces (90 elementos). Para búsquedas se promediaron 1.000 ejecuciones buscando un nombre inexistente (peor caso para lineal); para cada ordenamiento se promediaron 10 ejecuciones sobre copias nuevas. Los tiempos dependen del equipo y pueden variar.

| Operación | n | segundos promedio por ejecución |
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

En esta entrega incorporamos la persistencia de los datos para poder guardar y recuperar el catálogo de recetas, utilizando archivos de texto simple (`.txt`) y archivos binarios.

**- Persistencia en texto:**

- Se utiliza el archivo `recetas.txt` para almacenar las recetas del catálogo.
- Los datos se guardan en formato CSV, con un encabezado que identifica los campos.
- Para leer y escribir se utiliza el módulo `csv` de Python.
- Al cargar el archivo, se valida que los encabezados y los valores numéricos sean correctos.

**- Layout del registro binario (campos, `struct`, anchos):**

Se utiliza el módulo `struct` de Python para convertir los datos de cada receta en registros binarios de longitud fija.

Formato de registro utilizado:

`struct.Struct("<I 30s H 10s 15s")`

| Campo | Tipo | Tamaño |
|---|---|---:|
| ID | Entero sin signo (`I`) | 4 bytes |
| Nombre | Cadena de 30 bytes (`30s`) | 30 bytes |
| Tiempo de preparación | Entero sin signo corto (`H`) | 2 bytes |
| Dificultad | Cadena de 10 bytes (`10s`) | 10 bytes |
| Categoría | Cadena de 15 bytes (`15s`) | 15 bytes |
| **Total** | | **61 bytes** |

Las cadenas se codifican en bytes y se completan con bytes nulos (`\0`) cuando no alcanzan el tamaño establecido. De esta manera, todos los registros mantienen la misma longitud.

**- Header:**

El archivo binario cuenta con una cabecera que permite identificar el archivo y conocer la cantidad de registros almacenados.

Formato utilizado:

`struct.Struct("<4s 1s I")`

| Campo | Descripción | Tamaño |
|---|---|---:|
| Magia | Identifica el archivo mediante `AYED` | 4 bytes |
| Tema | Identifica el tema del proyecto (`R`) | 1 byte |
| Cantidad | Indica el número de recetas almacenadas | 4 bytes |
| **Total** | | **9 bytes** |

**- Cómo se actualiza un registro por posición:**

Para modificar una receta sin tener que reescribir manualmente todo el archivo, se utiliza el acceso directo mediante `seek()`.

El procedimiento consiste en:

1. Buscar la posición que ocupa la receta dentro del catálogo.
2. Calcular el desplazamiento correspondiente dentro del archivo binario.
3. Utilizar `seek()` para ubicar el cursor en el registro que se desea modificar.
4. Escribir los nuevos datos sobre esa posición.

La posición se calcula mediante la siguiente fórmula:

`HEADER.size + posicion * FORMATO.size`

Esto permite actualizar un registro específico utilizando su posición, sin recorrer ni reconstruir todos los registros anteriores.

**- Manejo de archivos inválidos:**

Se implementó la excepción `ArchivoInvalidoError` para controlar errores durante la lectura de archivos.

Se contemplan situaciones como:

- Archivos binarios incompletos o truncados.
- Archivos con una magia incorrecta.
- Archivos de texto con encabezados o registros inválidos.

De esta manera, el programa puede mostrar mensajes de error claros sin finalizar inesperadamente.

**- Pruebas realizadas:**

| Prueba | Descripción | Resultado |
|---|---|---|
| P13 | Guardar el catálogo en texto, cerrar el programa y volver a cargar las recetas. | Pasa |
| P14 | Guardar el catálogo en binario, modificar Sofrito (ID 3) de 25 a 30 minutos y volver a cargar el archivo. | Pasa |
| P15 | Intentar cargar un archivo con magia incorrecta y comprobar el mensaje de error. | Parcial: faltan probar binario truncado y TXT inválido. |

En las pruebas realizadas se comprobó que el catálogo pudo recuperarse correctamente con sus 30 recetas y que la modificación de Sofrito se mantuvo después de volver a cargar el archivo binario.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
