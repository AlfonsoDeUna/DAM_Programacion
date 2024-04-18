"""
1. A partir de un párrafo crea un diccionario donde cuente el número de palabras


2. A partir de un fichero mediante collections utiliza un diccionario donde cuente el número de palabras


3. Busca una palabra y que muestre el número de palabras


4.Recorre el diccionario (collections) para que salga la palabra con el nº de veces que aparece en el texto


5. Obtener la palabrá más común


6. Junta los dos diccionarios sumando las palabras que se repitan


------------------------------default dict -------------------------------------------------------------------

Dada una lista de tuplas que representan abreviaturas de CIUDADES y SU CLAVE, 
cree un defaultdict donde las claves sean abreviaturas de CIUDADES y los valores sean listas de CIUDADES

[('MADRID','M'),('SALAMANCA','SA'),...]
"""

"""
crear un programa de gestión de incidencias donde:
cada incidencia hay que guardar clave, descripción, tipo de incidencia usuario que pone incidencia y nombre técnico, 
Tiene que tener un contador del tipo de incidencia para ir contabilizando las incidencias por tipo

Tienes que utilizar al menos 2 clases de collections
    
"""
from collections import defaultdict,Counter,deque

incidencias = defaultdict(list)

a1 = [(1,"texto descripción", "sw", "usuario1", "tecnico1"), (2,"texto descripción2", "sw", "usuario2", "tecnico2")]

for  clave,desc,tipo,usu,tec in a1:
    incidencias[clave] = [desc,tipo,usu,tec]

print (incidencias)

c = Counter() 
for clave,valor in incidencias.items():
   c[valor[1]] += 1
   
print (c)  
"""
Ejercicio2:

Un colegio necesita un programa para contabilizar el número de suspensos por clase 
en todo el colegio.

Para ello te dan las notas de cada clase con el identificador del alumno y su nota
1eso = [1:5,2:4]
2eso = [1:10,2:6,3:6,4:5]


Crea el programa utilizando Collections para dar la información.

Tienes que utilizar al menos dos clases de collections

"""
"""
Ejercicio 3: 

Crea un programa para apilar peticiones de trabajo:
Las peticiones de trabajo tienen un id y prioridad 
Las prioridades pueden ser 1, 2 ,3

Hay que ir recorriendo la pila para quedarte con la tarea de prioridad mayor
y sacar el trabajo de la pila.

Si la incidencia que vas recorriendo tiene menor prioridad la devuelves a la pila
de tal manera que se tienen que ir resolviendo las incidencias por prioridad.

"""

lista_trabajo = deque()
 
 # añadir los tickets

lista_trabajo.append (("id1",2))
lista_trabajo.append (("id2",1))
lista_trabajo.append (("id3",2))

## sacando de lista y comprobando por prioridad



prioridad = 1
contador = 0
while (len(lista_trabajo)>0):
    elemento = lista_trabajo.pop()
    if (elemento[1] == prioridad):
        print ("haciendo trabajo")
        print ( elemento)
        contador +=1
    else:
        if (len(lista_trabajo)-1 >= contador):
            lista_trabajo.appendleft(elemento)
            contador +=1
        else:
            prioridad +=1
        
    
