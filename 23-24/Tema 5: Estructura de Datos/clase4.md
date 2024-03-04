# Collections Jerarquía de estructura de datos

## Counter

Un Counter es un contenedor que registra cuántas veces se agregan valores equivalentes. Se puede usar para implementar los mismos algoritmos para los cuales otros lenguajes comúnmente usan una bolsa o una estructuras de conjunto múltiple.

### Constructor
admite tres formas de inicialización. Su constructor se puede llamar con una secuencia de elementos, un diccionario que contiene claves y recuentos, o usando argumentos de palabra clave que mapean nombres cadena a los conteos.

```python

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

```

#### Actualizar

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

#### operaciones

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
