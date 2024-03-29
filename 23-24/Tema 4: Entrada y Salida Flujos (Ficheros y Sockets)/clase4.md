# Clase 07/02/2024

* Entrada desde teclado.
* Salida a pantalla. Almacenamiento de información en ficheros:
* Ficheros de datos. Registros.
* Apertura y cierre de ficheros. Modos de acceso.
* Escritura y lectura de información en ficheros.
* ==> **Almacenamiento de objetos en ficheros. Persistencia. Serialización.**
* Utilización de los sistemas de ficheros.
* Creación y eliminación de ficheros y directorios. Interfaces gráficos de usuario simples. Concepto de evento. Creación de controladores de eventos.

# Serialización de objetos.

## Pickle

Pickle es un elemento básico. Es un formato de serialización de objetos nativo de Python. 
La interfaz pickle proporciona cuatro métodos: `dump, dumps, load, y loads`. 
El método `dump()` se serializa en un archivo abierto (objeto similar a un archivo). 
El método `dumps()` se serializa en una cadena. El método load() se deserializa a partir de un objeto abierto similar a un archivo. 
El método `loads()` se deserializa a partir de una cadena.

1. Crea una clase llamada simple con un parámetro y un método magic __eq__ para poder comparar objetos

Ejemplo de serialización en cadena:

```python
import cPickle as pickle
pickle.dumps(simple)
```
En binario

```python
pickle.dumps(simple, protocol=pickle.HIGHEST_PROTOCOL)
```

## Serializar a fichero: pasamos a un fichero

```python
pickle.dump(simple, open('simple1.pkl', 'w'))
pickle.dump(simple, open('simple2.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
```
Observa cuánto ocupa cada uno en disco.

## Deserializar

```python
x = pickle.load(open('simple1.pkl'))
```
Compara con una instancia que tenga el mismo valor 

```
assert objeto_creado = x
```

## JSON

JSON (JavaScript Object Notation) forma parte de la biblioteca estándar de Python desde Python 2.5. 
Lo consideraré un formato nativo en este momento.
Es un formato basado en texto y es el rey no oficial de la web en lo que respecta a la serialización de objetos

```python
import json
print json.dumps(simple)
```
NOTA!: FALLA SERIALIZAR OBJETOS COMPLEJOS EN JSON
https://reqbin.com/code/python/pbokf3iz/python-json-dumps-example

```python
import pickle as pickle
import json

class Simple:
    def __init__ (self, a):
        self.a = a
        
        
    def __eq__ (self, obj):
        if (self.a == obj.a):
            return True
        else:
            return False  
        
class Traductor(json.JSONEncoder):
    def default(self, obj):
            return [obj.a]          
        
simple = Simple ("alfonso")

ser = json.dumps (simple, cls=Traductor)
print (ser)
```

### Ejercicio: Guarda el resultado en un fichero llamado: horoscope_data.json
```python
import requests
import json

# Make the GET request to the horoscope API
response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convert the response to JSON
```

### Ejercicio: Interpreta como del json somos capaces de guardarlo en una estructura

```python
import json

# Retrieve JSON data from the file
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Access and process the retrieved JSON data
date = data["data"]["date"]
horoscope_data = data["data"]["horoscope_data"]

# Print the retrieved data
print(f"Horoscope for date {date}: {horoscope_data}")
```
### Ejercicio: Como en el caso anterior podríamos recuperar el valor para un objeto. Crea el objeto horoscopo y a partir del json crea la instancia.

```python
```
