# CLASE 26/10/2023

# TEMA 2 OBJETOS


"In the programming world, duplicate code is considered evil. We should not have
multiple copies of the same, or similar, code in different places."


# HERENCIA

La herencia es una característica clave en la programación orientada a objetos que permite a una clase heredar atributos y métodos de otra clase.

Esto facilita la creación de clases relacionadas y reduce la redundancia del código

```Python
class ClaseBase:
    pass
class ClaseDerivada(ClaseBase):
    pass
```

Clase Base: Es la clase de la cual otras clases heredarán atributos y métodos.
Clase Derivada: Es la clase que hereda de la clase base.

## ¿Cómo aplicar la herencia?

Claro, el código que has compartido es un buen ejemplo práctico para entender la herencia en Python. A continuación, se desglosa en pasos de ejercicios:

### Ejercicio 1: Crear y Comprender la Clase Base

1. Crea una clase llamada `Contact` que tenga un método `__init__` para inicializar los atributos `name` y `email` de un contacto.
```python
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
```

### Ejercicio 2: Crear y Comprender la Clase Derivada

1. Crea una clase llamada `Supplier` que herede de `Contact`.
2. Agrega un método `order` a `Supplier` para realizar un pedido.
```python
class Supplier(Contact):
    def order(self, order):
        print("Si este fuera un sistema real, enviaríamos el pedido '{}' a '{}'".format(order, self.name))
```

### Ejercicio 3: Instanciar y Trabajar con Objetos

1. Crea una instancia de `Contact` y una de `Supplier`.
```python
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
```

2. Imprime los atributos `name` y `email` de estas instancias.
```python
print(c.name, c.email, s.name, s.email)
```

### Ejercicio 4: Explorar la Lista de Contactos

1. Examina el atributo de clase `all_contacts` y observa cómo se han agregado tanto `c` como `s` a la lista.
```python
print(c.all_contacts)
```

### Ejercicio 5: Entender la Restricción de Métodos

1. Intenta llamar al método `order` en la instancia de `Contact` y observa el error.
```python
c.order("I need pliers")
```

2. Ahora, llama al método `order` en la instancia de `Supplier` y observa el resultado.
```python
s.order("I need pliers")
```

La diferencia entre `c.all_contacts` y `self.all_contacts` es un concepto importante en la programación orientada a objetos en Python, y se relaciona con cómo se accede a los atributos de la clase y de la instancia. Vamos a explorar esto con los siguientes pasos y ejercicios.

### Ejercicio 6: Explorar Atributos de Clase y de Instancia

1. **Comprender Atributos de Clase**:
   - Explique que `all_contacts` es un atributo de la clase `Contact`, lo que significa que es compartido por todas las instancias de `Contact` y sus clases derivadas, como `Supplier`.

```python
print(Contact.all_contacts)  # Mostrará todas las instancias de Contact y Supplier
```

2. **Acceso a través de una Instancia**:
   - Muestre que aunque `all_contacts` es un atributo de la clase, aún puede accederse a través de una instancia utilizando `c.all_contacts` o `s.all_contacts`.

```python
print(c.all_contacts)  # También mostrará todas las instancias de Contact y Supplier
print(s.all_contacts)  # También mostrará todas las instancias de Contact y Supplier
```

3. **Modificación de Atributos de Clase**:
   - Explique que modificar un atributo de clase a través de una instancia, como en `c.all_contacts = []`, no cambiará el atributo de clase, sino que creará un nuevo atributo de instancia.

```python
c.all_contacts = []
print(c.all_contacts)  # Mostrará una lista vacía
print(Contact.all_contacts)  # Aún mostrará todas las instancias de Contact y Supplier
```

### Ejercicio 7: Explorar self

1. **Comprender `self`**:
   - Explique que `self` es una referencia a la instancia actual, y se utiliza para acceder a los atributos y métodos de la instancia.

2. **Acceso a Atributos de Clase con `self`**:
   - Muestre cómo `self.all_contacts` en un método de `Contact` o `Supplier` se referirá al atributo de clase `all_contacts`, a menos que se haya creado un atributo de instancia `all_contacts`.

```python
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def show_all_contacts(self):
        print(self.all_contacts)

c = Contact("Some Body", "somebody@example.net")
c.show_all_contacts()  # Mostrará todas las instancias de Contact y Supplier
```

3. **Modificación de Atributos de Clase con `self`**:
   - Explique cómo modificar `self.all_contacts` dentro de un método cambiará el atributo de clase si no hay un atributo de instancia `all_contacts`, y cómo evitar esto.

```python
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def clear_all_contacts(self):
        self.all_contacts = []  # Esto creará un nuevo atributo de instancia, no modificará el atributo de clase

c = Contact("Some Body", "somebody@example.net")
c.clear_all_contacts()
print(c.all_contacts)  # Mostrará una lista vacía
print(Contact.all_contacts)  # Aún mostrará todas las instancias de Contact y Supplier
```

### Ejercicio: Extender una Clase Incorporada y Agregar Funcionalidad Personalizada

#### Parte 1: Crear la Clase `ContactList`
1. Comienza creando una clase llamada `ContactList` que herede de la clase incorporada `list`.
```python
class ContactList(list):
    pass  # por ahora dejamos la clase vacía
```

#### Parte 2: Agregar un Método de Búsqueda a `ContactList`
1. Agrega un método llamado `search` a la clase `ContactList` que tome un argumento `name`.
2. Dentro del método `search`, inicializa una lista vacía llamada `matching_contacts`.
3. Itera sobre la lista `self` y verifica si el `name` proporcionado está contenido en el nombre del contacto. Si es así, agrega el contacto a `matching_contacts`.
4. Retorna `matching_contacts` al final del método.
```python
class ContactList(list):
    def search(self, name):
        '''Devuelve todos los contactos que contienen el valor de búsqueda en su nombre.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
```

#### Parte 3: Crear la Clase `Contact`
1. Crea una clase llamada `Contact`.
2. Dentro de la clase `Contact`, declara un atributo de clase `all_contacts` e inicialízalo con una instancia de `ContactList`.
3. Define el método `__init__` que acepte `name` y `email` como argumentos, y asigna estos valores a las variables de instancia correspondientes. También, agrega la nueva instancia de `Contact` a `all_contacts`.
```python
class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
```

#### Parte 4: Prueba la Funcionalidad
1. Crea tres instancias de `Contact` con diferentes nombres y correos electrónicos.
2. Utiliza el método `search` de `all_contacts` para buscar contactos por nombre y verifica que la salida sea la esperada.
```python
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")

# Probando la funcionalidad de búsqueda
print([c.name for c in Contact.all_contacts.search('John')])  # Debería imprimir ['John A', 'John B']
```

#### Parte 5: Comprender la Extensión de la Clase Incorporada
1. Comprende cómo hemos cambiado la sintaxis incorporada `[]` a algo de lo que podemos heredar, al extender la clase `list` con `ContactList`.
2. Verifica que crear una lista vacía con `[]` es lo mismo que usar `list()`.
```python
print([] == list())  # Debería imprimir True
```

1. **Sintaxis Azucarada (Syntax Sugar)**:
   - La sintaxis `[]` es una forma abreviada y más legible de crear una lista, pero en realidad, lo que ocurre detrás de escena es que se llama al constructor `list()`. Esta simplificación se conoce como "sintaxis azucarada" porque hace el código más "dulce" o agradable a la vista, sin agregar funcionalidad nueva.

2. **Extensión de Clases Incorporadas**:
   - En Python, las clases incorporadas como `list`, `dict`, `str`, entre otras, son extensibles. Esto significa que puedes crear nuevas clases que hereden de estas clases incorporadas, añadiendo o modificando comportamientos.

3. **Herencia de `object`**:
   - Todas las clases en Python, incluidas las clases incorporadas como `list` y `dict`, heredan de la clase base `object`. Esto se demuestra con el ejemplo `isinstance([], object)`, que devuelve `True`, indicando que una lista es una instancia de `object`.

4. **Extensión de la Clase `dict`**:
   - Se presenta un ejemplo donde se extiende la clase `dict` para crear una nueva clase `LongNameDict`. Esta nueva clase tiene un método adicional `longest_key` que devuelve la clave más larga en el diccionario.

5. **Extensión de Otros Tipos Incorporados**:
   - Se menciona que muchos otros tipos incorporados pueden ser extendidos de manera similar, incluyendo `object`, `list`, `set`, `dict`, `file`, `str`, así como los tipos numéricos `int` y `float`. Esto permite una gran flexibilidad para personalizar y extender las funcionalidades existentes en Python según las necesidades del programador.

En resumen, este fragmento proporciona una visión sobre cómo las clases incorporadas en Python pueden ser extendidas para añadir funcionalidades personalizadas, y cómo algunas sintaxis comunes en Python son en realidad simplificaciones de operaciones más complejas que ocurren detrás de escena. También destaca la herencia universal de la clase `object`, lo que subraya la naturaleza orientada a objetos de Python.
