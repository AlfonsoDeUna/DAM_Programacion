# Clase 21/02/2025

## Estructuras de Datos

## Repaso a Listas y más cosas

* list.append(x)
  Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].

* list.extend(iterable)
  Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.

* list.insert(i, x)
  Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x).

* list.remove(x)
  Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.

* list.pop([i])
  Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

* list.clear()
  Elimina todos los elementos de la lista. Equivalente a del a[:].

*  list.index(x[, start[, end]])
  Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. Lanza una excepción ValueError si no existe tal elemento.
  Los argumentos opcionales start y end son interpretados como la notación de rebanadas y se usan para limitar la búsqueda a un segmento particular de la lista. El índice retornado se calcula de manera relativa al inicio de la secuencia completa en lugar de hacerlo con respecto al argumento start.

* list.count(x)
  Retorna el número de veces que x aparece en la lista.

* list.sort(*, key=None, reverse=False)
  Ordena los elementos de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, ver sorted() para su explicación).

* list.reverse()

---
### Ejercicio. Crea un programa en python utilizando todos los tipos de métodos que muestro en este tema
---

## Listas como Pilas
  
  Los métodos de lista hacen que resulte muy fácil usar una lista como una pila, donde el último elemento añadido es el primer elemento retirado («último en entrar, primero en salir»). Para agregar un elemento a la cima 
  de la pila, utiliza append(). Para retirar un elemento de la cima de la pila, utiliza pop() sin un índice explícito.

  ```python

  ```


  


  Invierte los elementos de la lista in situ.

* list.copy()
  Retorna una copia superficial de la lista. Equivalente a a[:].
