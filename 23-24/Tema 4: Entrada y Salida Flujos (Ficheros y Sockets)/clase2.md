# Clase 
## Repaso de programación orientada a objetos

``` python
# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius
```

### Uso del dir
 ```
>>> dir(Circle.radius)
[..., 'deleter', ..., 'getter', 'setter']
 ```

## CREACIÓN DE GETTERS Y SETTERS sin @properties
``` python
# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )
```

## Ejercicios de repaso:
### Crea la clase Punto con los atributos x e y (privados) con métodos que podamos obtener y settear sus valores con @ properties
### Crea la clase Punto con los atributos x e y (privados) con métodos que podamos obtener y settear sus valores sin @ properties

# CAJÓN DE SASTRE DE LAS COSAS QUE NOS QUEDAN POR CONTAR DEL TEMA

## Copiar ficheros en python
https://j2logo.com/como-copiar-un-fichero-con-python/

## Copiar mover ficheros en python
https://micro.recursospython.com/recursos/como-copiar-o-mover-un-archivo.html

## Flujos de Entrada y salida:

Cuando sabemos como escribir en ficheros y solicitar información al usuario, la pregunta que nos podemos hacer es, ¿Cómo hace Python para conectar pantalla y teclado?. La respuesta es, a través de los flujos de entrada y salida de datos. Estos flujos son los mecanismos que nos permiten realizar operaciones de entrada y salida en nuestros programas.

Teclado (entrada|input) → Programa → Pantalla (salida|output)

La mayoría de los Sistemas Operativos ofrecen tres flujos de entrada y salida de datos por defecto, cada uno de ellos para un propósito específico.

Entrada de datos estándar (stdin), es un canal de comunicación entre el programa y la entrada de datos (normalmente en formato texto desde un teclado).
Salida de datos estándar (stdout), es un canal de comunicación entre el programa y la salida de datos (normalmente en formato texto a través de una pantalla).
Salida de Errores (stderr), es un canal de comunicación para mostrar errores y mensajes de diagnóstico de un programa (normalmente en formato texto a través de la pantalla).
Cuando usamos la función input() estamos usando el canal de comunicación de entrada de datos STDIN. La función print() es un claro ejemplo de un flujo de datos STDOUT. Si ejecutas un script escrito en Python y recibes un error, ese error probablemente es impreso usando el canal de comunicación STDERR.

## ¿Qué es un STREAM?

* ----------------- STREAMS --------------------- 
* |  ORIGEN   | ==>==>==>==>==>==>  |-DESTINO--| 
* ------------------flujo Bytes salida--------------

Un stream es una secuencia de bytes producidos (output) o consumidos (input) por un programa. 
Normalmente un stream está asociado con un fichero o un device, como un terminal; 
en algunos sistemas, un stream se puede asociar a lo que se llama un pipe, que es un mecanismo de comunicación entre diferentes programas.

### Cuestión. Pon un ejemplo de stream de entrada y salida en python


# Un poco de práctica con StringIO (Stream de cadenas)
https://medium.com/techtofreedom/stringio-in-python-eebf31d18f43
