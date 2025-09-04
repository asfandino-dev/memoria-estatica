# Práctica de Memoria Estática y Dinámica en Python

Este proyecto fue creado con el objetivo de explorar y demostrar el uso de la memoria estática y dinámica en Python, a través de los conceptos de inmutabilidad y mutabilidad.

## Descripción

El programa simula un sistema de gestión de calificaciones de un estudiante. Para ello, se utilizan dos estructuras de datos principales:

- **Tuplas (inmutables):** Para almacenar la lista de cursos, que no debe cambiar durante la ejecución del programa.
- **Diccionarios (mutables):** Para gestionar las calificaciones, permitiendo agregar, modificar y eliminar notas de forma dinámica.

## Tecnologías Utilizadas

Este proyecto está desarrollado íntegramente en Python. No se requieren bibliotecas externas, ya que se basa en las estructuras de datos nativas del lenguaje.

## Conceptos Clave: Mutabilidad e Inmutabilidad

Este proyecto se centra en la diferencia entre datos mutables e inmutables en Python:

- **Inmutabilidad (Tuplas y str):** La tupla cursos y la cadena de texto estudiante son inmutables. Esto significa que una vez que se crean en la memoria, no se pueden modificar. Cualquier cambio aparente crearía un nuevo objeto en una dirección de memoria diferente. Esto los hace ideales para datos que no deben alterarse, como una lista fija de materias.

- **Mutabilidad (Listas y Diccionarios):** El diccionario calificaciones es mutable. Esto nos permite modificar sus contenidos, como las listas de notas, sin cambiar su dirección de memoria original. Esta característica es fundamental para un sistema de registro de notas que necesita agregar, modificar o eliminar datos dinámicamente.

## Uso del Programa

Para ejecutar el programa, simplemente corre el script desde tu terminal de Python.

Una vez que lo inicies, el programa te presentará un menú interactivo con las siguientes opciones:

- **Añadir calificaciones:** Te permitirá agregar una nueva nota a la lista de notas de un curso existente.
- **Modificar calificaciones:** Podrás cambiar una nota específica de un curso ya existente. El programa te pedirá la posición de la nota que deseas modificar.
- **Eliminar calificaciones:** Te permitirá "eliminar" una nota, reemplazándola con un valor de 0. El programa te pedirá la posición de la nota a eliminar.
- **Promedio general:** Calculará y mostrará el promedio de todas las notas en todos los cursos.

Para salir del programa, simplemente digita cualquier número que no esté en el menú de opciones.
