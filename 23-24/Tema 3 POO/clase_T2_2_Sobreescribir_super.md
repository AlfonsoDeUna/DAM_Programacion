
### Sobrescribir Métodos y `super`

La herencia en Python no sólo permite añadir nuevos métodos a una clase existente, sino también modificar los métodos ya existentes. Por ejemplo, si queremos expandir la clase `Contact` para incluir un número de teléfono en la inicialización, necesitamos sobrescribir el método `__init__`. Sobrescribir significa reemplazar o modificar un método de la superclase con un nuevo método (con el mismo nombre) en la subclase. No se necesita una sintaxis especial para hacer esto; el método recién creado en la subclase se llamará automáticamente en lugar del método de la superclase.

```python
class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
```

Cualquier método puede ser sobrescrito, no sólo `__init__`. Sin embargo, en el ejemplo anterior, hay código duplicado para configurar las propiedades `name` y `email`, y la clase `Friend` olvida añadirse a la lista `all_contacts` que hemos creado en la clase `Contact`.

La solución es utilizar la función `super` para ejecutar el método `__init__` original en la clase `Contact`, y luego agregar el nuevo atributo `phone`:

```python
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)  # Llamada al método __init__ de la superclase
        self.phone = phone  # Inicialización específica de la subclase
```

En este ejemplo, primero obtenemos la instancia del objeto padre usando `super`, y llamamos a `__init__` en ese objeto, pasando los argumentos esperados. Luego realizamos nuestra propia inicialización, es decir, estableciendo el atributo `phone`.



