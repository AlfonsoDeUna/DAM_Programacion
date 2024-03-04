# Lectura y escritura de información: 

## Contenido
Flujos (streams):
 * Tipos de flujos. Flujos de bytes y de caracteres.
 * Clases relativas a flujos. Jerarquías de clases.
 * Utilización de flujos.
Entrada/salida estándar:
 * Entrada desde teclado.
 * Salida a pantalla.
Almacenamiento de información en ficheros:
 * Ficheros de datos. Registros.
 * Apertura y cierre de ficheros. Modos de acceso.
 * Escritura y lectura de información en ficheros.
 * Almacenamiento de objetos en ficheros. Persistencia. Serialización.
 * Utilización de los sistemas de ficheros.
 * Creación y eliminación de ficheros y directorios.
Interfaces gráficos de usuario simples. Concepto de evento. Creación de controladores de eventos.

## Almacenamiento de información en ficheros

Aprenderemos abrir, leer, cerrar, escribir ficheros.

### Abrir ficheros en Python

```python
  fichero = open('ejemplo.txt')
```
Otro método.
Con with no es necesario cerrar el fichero.

```python
with open('ejemplo.txt', 'r') as fichero:
   fichero.read()
```

### Cerrar ficheros

Importante liberar los recursos del fichero que hemos ocupado al realizar el open

```python
fichero.close()
```


### modos de apertura

* ‘r’: Por defecto, para leer el fichero.
* ‘w’: Para escribir en el fichero.
* ‘x’: Para la creación, fallando si ya existe.
* ‘a’: Para añadir contenido a un fichero existente.
* ‘b’: Para abrir en modo binario.


### Lectura de la información

Imprimir todo su contenido
### Metodo read

``` python
fichero.read()
```

### Metodo readLine()

Vamos leyendo líneas hasta el final del fichero. Unva vez llegado al final del fichero ya no puede leer más.
Cada vez que utilices readLine() solo podrás leer una línea


```python
fichero.readLine()
```

### Método readLines()

Existe otro método llamado readlines(), que devuelve una lista donde cada elemento es una línea del fichero.

```python
fichero = open('ejemplo.txt')
lineas = fichero.readlines()
print(lineas)
```


#### Ejercicio1 crea un fichero txt y crea una clase que lea ficheros uno método utiliza read y otro readLine

Para leer todos las líneas de un fichero podemo utilizar while

```python
with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()
```

## CREAR UNA PANTALLA DONDE VISUALIZAR LOS DATOS DE UN FICHERO
```python

from tkinter import *
# Hold onto a global reference for the root window
root = None

def buttonPushed():
   # abrir el fichero y
   txt.insert (END, <aquí poner el contenido del fichero>)

def main():
  global root
  global txt
  root = Tk() # Create the root (base) window where all widgets go
  w = Label(root, text="Hello, world!") # Create a label with words
  w.pack() # Put the label into the window
  txt = Text(root, height = 5, width = 52)
  #txt.insert(root.END, "ejemplo")
  txt.pack()
  myButton = Button(root, text="Exit",command=buttonPushed)
  myButton.pack()
  root.mainloop() # Start the event loop

main()

```

## Escribir

### Modos
‘w’: Borra el fichero si ya existiese y crea uno nuevo con el nombre indicado.
‘a’: Añadirá el contenido al final del fichero si ya existiese (append end Inglés)
‘x’: Si ya existe el fichero se devuelve un error.


### Método write ()

```python
fichero = open("datos_guardados.txt", 'w')
fichero.write("Contenido a escribir")
fichero.close()
```

#### Guardar los elementos de una lista en python

```python
# Abrimos el fichero
fichero = open("datos_guardados.txt", 'w')

# Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

# Cerramos el fichero
fichero.close()
```
## Ejercicio crea un programa que a partir de un txt con datos personales cree un fichero html con los datos personales que sea un CV
## Ejercicio crea un

