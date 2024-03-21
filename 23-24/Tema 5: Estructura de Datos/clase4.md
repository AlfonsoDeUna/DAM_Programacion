# Python Collections Module

Ya hemos visto los tipos de estrcuturas básicas de python, tuplas, listas y diccionarios para organizar y almacenar información. Collections se ha creado para tener estructuras que son más eficientes para trabajar con ellas.

Y te ayudan a trabajar con tuples, diccionarios y listas. Por ejemplo, usaremos namedtuples para crear tuplas con campos con nombre, defaultdict para agrupar de forma concisa la información en diccionarios, y deque para añadir elementos de forma eficiente a cualquier lado de un objeto lista.

# Collections Jerarquía de estructura de datos

| collections |
|-------------|
| Counter     |
| DefaultDict |
| ChainMap    |
| Deque       |
| namedtuple  |
| OrderedDict |

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

## Ejercicios

1. Escribe un programa para iterar sobre una serie de números tantas veces como le indiquemos.

```python
from collections import Counter
d = {
    "a":2,
    "b":4
}
c1 = Counter (d)
valor = input ("damevalor")
c = Counter(a=int(valor), b=3, c=2, d=2)

# Print the elements in th2e Counter 'c' as a list
print(list(c.elements()))
```
   
3. Escribe un programa que busque los elementos más comunes y que cuente el número de ocurrencias en un texto
   ¿Qué método existe en Counter para buscar las más comunes?

4. Ejercicio a partir de un fichero que lea el texto de un libro nos de el número de veces que aparece la palabra en el texto.
```python
from collections import Counter

with open("./el_quijote.txt","r",encoding="iso-8859-1") as f:
    texto = f.read()
    texto = texto.split(" ")
    c = Counter (texto)
    print (c.most_common(30))
```   

# DefaultDict

Es una subclase de dict, diseñada para cuando no tienes claves. La principal diferencia entre dict y defaultdict es que cuando tienes que crear
un diccionario y no tienes valores para una clave te crea un valor por defecto.

### Ejemplo:

```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

sorted(d.items())

```


#### Ejemplo. ¿Qué ocurre si creas el siguiente código?
```python
def_dict=defaultdict(list())
``` 

#### Ejercicio. Crea un defaultdict contando las palabras de un fichero de texto
código de ejemplo
```python
from collections import defaultdict
word_counts = defaultdict(int)
for word in lines:
    word_counts[word] += 1
```

#### Ejercicio: Agrupaciones con defaultdict

```python
dep = [('Ventas', 'PePe Doe'),
       ('Ventas', 'Aaron Smith'),
       ('Administración', 'Jaime Doe'),
       ('Marketing', 'Eli Smith'),
       ('Marketing', 'Alfonso Doe')]

from collections import defaultdict

dep_dd = defaultdict(list)

for department, employee in dep:
    dep_dd[department].append(employee)

dep_dd
```

Añade un valor repetido a la lista origina y observa que ocurre

#### Ejercicio Agregaciones.
```python
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]
# enter float as argument        
dd = defaultdict(float)  # collections.defaultdict
for product, income in incomes:
    dd[product] += income
# defaultdict(float, {'Books': 3970.0, 'Tutorials': 1940.0, 'Courses': 7680.0})
for product, income in dd.items():
    print(f"Total income for {product}: ${income:,.2f}")
```

#### Ejercicio: A partir de un Excel abre un excel en python carga los valores en una lista y utiliza la agregación para sumar una columna

Importa la librería openyxl
```python
pip install openpyxl
```
código de ejemplo
```python

# Import openpyxl 
import openpyxl 
  
# Open the spreadsheet 
workbook = openpyxl.load_workbook("data.xlsx") 
  
# Get the first sheet 
sheet = workbook.worksheets[0] 
  
# Create a list to store the values 
names = [] 
  
# Iterate over the rows in the sheet 
for row in sheet: 
    # Get the value of the first cell 
    # in the row (the "Name" cell) 
    name = row[0].value 
    # Add the value to the list 
    names.append(name) 
  
# Print the list of names 
print(names)
```



# ChainMap

maneja una secuencia de diccionarios, y busca a través de ellos en el orden en que se les da para encontrar valores asociados con llaves. Un ChainMap hace un buen contenedor de «contexto», ya que se puede tratar como una pila para la cual ocurren cambios a medida que la pila crece, con estos cambios siendo descartados nuevamente a medida que la pila se reduce.

# Deque

Una cola doblemente terminada, o deque, admite agregar y eliminar elementos de cualquier extremo de la cola. Las pilas y colas más comunes son formas degeneradas de deques, donde las entradas y salidas están restringida a un solo extremo.

# namedtuple — Subclase de tupla con campos con nombre

# OrderedDict — Recuerde el orden en que las claves se agregan a un diccionario
