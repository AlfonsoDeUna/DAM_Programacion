# Clase 08/02/2024

## Ejemplo de serialización y desserialización JSON desde fichero

```python
import json

class Person():
    def __init__(self, name, age, nickname):
        self.name = name
        self.age = age
        self.nickname = nickname
    
    def to_dict(self):
        data = {}
        data['name'] = self.name
        data['age'] = self.age
        data['nickname'] = self.nickname
        return data
 
# crear serialización en json    
peeps = []
A = Person ("Alfonso","10","PadreNuestro")
B = Person ("perfil","10", "comercial")

peeps.append(A.to_dict())
peeps.append(B.to_dict())

with open('data.json', 'w') as outfile:
    json.dump(peeps, outfile)    
    
personas = []    
with open('data.json', 'r') as infile:
    data = json.loads(infile.read())

    for item in data:
        personas.append(Person(item['name'], item['age'], item['nickname']))
    

#recorre la lista de objetos que he cargado en el desserialización.   
for persona in personas:
    print (persona.name)
```

## Ejercicio: crea una clase que deserialice la siguiente llamada JSON

https://jsonplaceholder.typicode.com/todos/

#### EN EL FICHERO DEL DÍA 07/02/2024 TENÉIS UN EJEMPLO DE CÓMO REALIZAR UNA LLAMADA A UN API REST
https://github.com/AlfonsoDeUna/DAM_Programacion/blob/main/23-24/Tema4_Entrada_Salida/20240207X.md


Ejemplo de la salida de la llamada API REST:
```json

[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  }
]
```
