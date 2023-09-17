# Tipos de Datos en Python

## 1. Introducción Teórica (15 minutos)

- **Enteros (int)**: Representan números sin decimales. Ejemplos: `-3`, `0`, `42`.
- **Flotantes (float)**: Representan números con decimales. Ejemplos: `-3.14`, `0.0`, `42.5`.
- **Cadenas de caracteres (str)**: Representan secuencias de caracteres. Ejemplos: `"Hola"`, `"1234"`, `"¡Bienvenido a Python!"`.
- **Booleanos (bool)**: Representan valores de verdad: `True` o `False`.
- **Listas**: Colecciones ordenadas y modificables de elementos. Ejemplo: `[1, 2, 3, 4]` o `["manzana", "banana", "cereza"]`.
- **Tuplas**: Colecciones ordenadas e inmutables. Ejemplo: `(1, 2, 3)` o `("manzana", "banana", "cereza")`.
- **Diccionarios**: Colecciones no ordenadas de pares clave-valor. Ejemplo: `{"nombre": "Juan", "edad": 30}`.

## 2. Ejercicios Prácticos en Clase

### Ejercicio de identificación (10 minutos)

Identifiquen el tipo de dato en Python. Por ejemplo:

```python
5       # int
5.5     # float
"5"     # str
True    # bool
[1, 2, 3]  # list
(1, 2, 3)  # tuple
{"clave": "valor"}  # dict
```
### Ejercicio de creación (15 minutos)

intérprete interactivo de Python 
Por ejemplo, para listas:

```python
colores = ["rojo", "verde", "azul"]
print(colores)
```
---
Aquí es importante hablar de la diferencia entre tupla y una lista en python

### Diferencias entre Tuplas y Listas en Python

Tanto las tuplas como las listas en Python son estructuras de datos que permiten almacenar colecciones de elementos. Sin embargo, presentan diferencias clave:

### 1. Mutabilidad:
- **Lista**: Es mutable, lo que significa que puedes modificar su contenido después de que ha sido creada. Puedes agregar, eliminar o cambiar elementos en una lista después de su definición.
- **Tupla**: Es inmutable, lo que significa que una vez que se crea una tupla, no puedes alterar su contenido.

### 2. Sintaxis:
- **Lista**: Se define utilizando corchetes `[]`. Ejemplo: `mi_lista = [1, 2, 3]`.
- **Tupla**: Se define utilizando paréntesis `()`. Ejemplo: `mi_tupla = (1, 2, 3)`.

### 3. Métodos:
- **Lista**: Tiene varios métodos disponibles, como `append()`, `remove()`, `pop()`, `insert()`, entre otros.
- **Tupla**: Debido a su inmutabilidad, las tuplas tienen un conjunto limitado de métodos, principalmente `count()` e `index()`.

### 4. Uso:
- **Lista**: Se utiliza cuando se necesita una colección que puede cambiar durante la ejecución del programa.
- **Tupla**: Se utiliza cuando se desea representar una colección que no debe ser modificada.

### 5. Rendimiento:
- Las tuplas, al ser inmutables, pueden ser ligeramente más rápidas que las listas en ciertas operaciones debido a optimizaciones internas.

### 6. Almacenamiento:
- Las listas, al ser dinámicas, generalmente consumen más memoria que las tuplas para almacenar la misma cantidad de elementos.

En resumen, aunque las listas y las tuplas parecen similares, se utilizan en diferentes escenarios dependiendo de si necesitas una colección mutable o inmutable.


---
### Ejercicio de manipulación (20 minutos)

 fragmentos de código y pídeles que predigan el resultado. ejecutar y verificar resultados

```python
Copy code
# Fragmento 1
texto = "Python es genial"
print(texto[7:10])

# Fragmento 2
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

# Fragmento 3
datos = {"nombre": "Ana", "edad": 28}
print(datos["nombre"])
```

### Tarea para Casa
Escribir un pequeño programa en Python que utilice al menos tres tipos diferentes de datos y que realice alguna operación.

Por ejemplo, un programa que tome una lista de números, calcule su promedio y luego imprima un mensaje que diga si el promedio es mayor o menor que un número dado.


