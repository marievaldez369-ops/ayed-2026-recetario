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
-Catalogo: cada receta con su nombre y lista de ingredientes.  

-Mutables: listas y diccionarios(recetas e ingredientes), es dinámica y pueden cambiar.

-Inmutables: nombre de receta(strings) para evitar efectos secundarios y proteger la identidad de cada receta.

-Relación catalogo/coleccion/pila/cola:

-El catalogo es la lista principal.

-La colección representa la estructura base que organiza la receta.

-La pila se uso para mejorar pasos de preparación.

-La cola se uso para manejar pedidos o tareas en orden.

## 3. Recursión (E2)
Caso recursivo: cuando el ingrediente es sub-receta, se llama de nuevo la funcion.
- Función:Usamos una función recursiva para descomponer recetas que contiene sub-recetas.
-Caso Base: cuando el ingrediente no es sub-receta, se agrega directo.
-Caso recursivo: cuando el ingrediente es sub-receta, se llama de nuevo la funcion.
- Traza de un ejemplo real del dataset:
Ejm: pizza : incluye masa, la función entra en masa y devuelve sus ingredientes finales.

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
