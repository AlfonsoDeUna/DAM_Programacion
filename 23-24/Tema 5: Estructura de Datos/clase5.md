# Array — Secuencia de datos de tipo fijo

## ESTRUCTURAS DE DATOS EN PYTHON

## LISTAS, DICCIONARIOS. POR DEFECTO EN PYTHON

## UTILIZAR LISTAS HAY CASOS EN LOS QUE CONVIENE UTILIZAR ARRAYS, ARREGLOS

### VENTAJA DE UTILIZAR LISTAS: FLEXIBILIDAD PERO CON MUCHOS DATOS NO SON EFICIENTES
### VENTAJA DE UTILIZAR ARRAYS: ES QUE ESTÁN HECHOS PARA SER EFICIENTES PERO NO SON TAN FLEXIBLES. 


El módulo array define una estructura de datos de secuencia que se ve muy parecida a una list, excepto que todos los miembros tienen que ser del mismo tipo primitivo. Los tipos admitidos son todos numéricos u otros tipos primitivos de tamaño fijo como bytes.

* https://rico-schmidt.name/pymotw-3/array/index.html

#### Ejemplo

```python
import array
import binascii

s = b'This is the array.'
a = array.array('b', s)

print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))
```

## IMPORTAR 

```python
import python
```

## CREAR ELEMENTOS EN EL ARRAY DESDE UNA LISTA

```python

# tipos enteros B y b
arr1 = array.array ('B', [1,4,1,4,11])


arr2 = array.array('B', range(10))
print (arr2)
```

## AÑADIR MÁS ELEMENTOS A UN ARRAY EXTEND
```python
# añadir elementos al array
arr2.extend (range(3))
print (arr2)
```

## SABER EL TIPO DEL ARRAY EL PARÁMETRO TYPECODE Y EL TAMAÑO DEL TIPO ITEMSIZE
```python


# me dice el tipo de array
print (arr2.typecode)

# preguntar por el tamaño de cada elemento en el array en bytes
print (arr2.itemsize)
```
---
#### Ejercicio crea una lista con decimales pista: 'f' y 'd'
---

## OPERACIONES BÁSICAS CON ARRAYS

# AÑADIR NUEVOS ELEMENTOS
método append(elemento)

```python
# añadir elementos
arr2.append(111)
print (arr2)
```

## longitud o número de elementos de un array
len() utiliza el método magic __len__

#### Ejercicio: Obten la longitud e la lista de ejemplo
```
print (len(arr2))

```

## Buscar la posición que ocupa un elemento en el array
arr.index(elemento)

``` python
## posición de un elemento en el array
arr2.index(111)
print ("La posición del elemento 111 es: " + str (arr2.index(111)))
```
## añadir un elemento en una posición que queramos
insert (posición y elemento)

#### Ejercicios de ejemplo:
* añade en la posición 4 el elemento 44
* añade en la posición 10 el elemento 100

## Como utilizar el array como pila con pop()

* pop() obtienes el último elemento
* pop(posición) saca de la lista el element de la posicion que le damos como parámetro

## invertir el array
* con el método reverse()

## borrar un elemento de una posición
* con el método remove (posicion)

#### Ejercicio: Como eliminar un valor concreto de la lista en una sola línea
```python
arr2.remove (arr.index(111))
```
