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

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
