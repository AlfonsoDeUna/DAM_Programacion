# Python Collections Module
# Collections Jerarquía de estructura de datos

# Counter

Un Counter es un contenedor que registra cuántas veces se agregan valores equivalentes. Se puede usar para implementar los mismos algoritmos para los cuales otros lenguajes comúnmente usan una bolsa o una estructuras de conjunto múltiple.

### Constructor
admite tres formas de inicialización. Su constructor se puede llamar con una secuencia de elementos, un diccionario que contiene claves y recuentos, o usando argumentos de palabra clave que mapean nombres cadena a los conteos.

```python

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

```

### Actualizar

```python
import collections

c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict    :', c)
```

### Acceso al número de recuentos

```python
import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
```

### operaciones

```python
import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)
```

# DefaultDict

Ejemplo:

```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

sorted(d.items())

```

# ChainMap

maneja una secuencia de diccionarios, y busca a través de ellos en el orden en que se les da para encontrar valores asociados con llaves. Un ChainMap hace un buen contenedor de «contexto», ya que se puede tratar como una pila para la cual ocurren cambios a medida que la pila crece, con estos cambios siendo descartados nuevamente a medida que la pila se reduce.

# Deque

Una cola doblemente terminada, o deque, admite agregar y eliminar elementos de cualquier extremo de la cola. Las pilas y colas más comunes son formas degeneradas de deques, donde las entradas y salidas están restringida a un solo extremo.

# namedtuple — Subclase de tupla con campos con nombre

# OrderedDict — Recuerde el orden en que las claves se agregan a un diccionario
