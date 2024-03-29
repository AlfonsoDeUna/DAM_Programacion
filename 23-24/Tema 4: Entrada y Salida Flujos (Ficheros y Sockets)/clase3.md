# Clase 31/01/2024

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

## Hoy veremos

Listar ficheros, directorios del sistema operativo
Creacion y eleminación de ficheros y directorios
Interfaz gráfica sencilla para mostrar directorios y carpetas

### Ejemplo de Interfaz gráfica de texto con scrollBar
```python
# Import the required library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x350")

# Add a Scrollbar(horizontal)
v=Scrollbar(win, orient='vertical')
v.pack(side=RIGHT, fill='y')

# Add a text widget
text=Text(win, font=("Georgia, 24"), yscrollcommand=v.set)

# Add some text in the text widget
for i in range(10):
   text.insert(END, "Welcome to Tutorialspoint...\n\n")

# Attach the scrollbar with the text widget
v.config(command=text.yview)
text.pack()

win.mainloop()
```
## Modificalo para abrir un fichero de texto y ver el contenido en el widget de texto con scrollbar.

## Librería OS
```python
import os
```

### Listar ficheros y directorios

```python
print(os.listdir())
```

#### Listar directorios concretos a partir de su ruta
`.` Directorio actual
`..` Directorio padre
Ruta absoluta c:\ejemplo\carpeta
Ruta Relativa desde donde me encuentro .\carpeta\

```python
print (os.listdir(path='..')
```

## Obtener la ruta actual
```python
ruta_app = os.getcwd()
```

## Preguntar si es un archivo
```python
os.path.isfile(archivo)
```
## Ejemplo de listado de ficheros

```python
ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    print (archivo)
```

## Información de los ficheros
Con la función os.path.isfile(archivo) se comprueba si el elemento es un archivo.

Por cierto, aunque hemos utilizado os.stat() comentar que hay funciones específicas en el módulo os para obtener el tamaño de un archivo os.path.getsize() y las fechas de último acceso os.path.getatime() y de última modificación os.path.getmtime().

Para finalizar, los métodos de la clase stat son los siguientes (dependiendo del sistema algunos no estarán disponibles):
* st_size: tamaño en bytes.
* st_mode: tipo de archivo y bits de permisos.
* st_ino: número de inodo.
* st_dev: identificador del dispositivo.
* st_uid: identificador del usuario propietario.
* st_gid: identificador del grupo propietario.
* st_atime: fecha-hora del último acceso (en segundos).
* st_mtime: fecha-hora de la última modificación (en segundos).
* st_ctime: fecha-hora ultimo cambio (unix) o creación (win).
* st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
* st_blocks: número de bloques de 512 bytes asignados.
* st_blksize: tamaño de bloque preferido por sistema.
* st_rdev: tipo de dispositivo si un dispositivo inode.
* st_flags: banderas definidas por usuario.
* st_gen: Número fichero generado.
* st_birthtime: tiempo de creación del archivo.
* st_rsize: tamaño real del archivo.
* st_creator: creador del archivo.
* st_type: tipo de archivo.
* st_file_attributes: atributos.

#### Ejemplo

``` python
import os
from datetime import datetime

ruta_app = os.getcwd()  # obtiene ruta del script 
print (ruta_app)
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
linea = '-' * 40
print (contenido)
for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    print (os.path.isfile(archivo))
    #if not os.access(archivo, os.R_OK) and os.path.isfile(archivo):
    archivos += 1
    estado = os.stat(archivo)  # obtiene estado del archivo
    tamaño = estado.st_size  # obtiene de estado el tamaño 
    
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime. 
    
    ult_acceso = datetime.fromtimestamp(estado.st_atime)
    modificado = datetime.fromtimestamp(estado.st_mtime)
    
    # Se aplica el formato establecido de fecha y hora
    
    ult_acceso = ult_acceso.strftime(formato)
    modificado = modificado.strftime(formato)
    
    # Se acumulan tamaños y se muestra info de cada archivo
    
    total += tamaño
    print(linea)
    print('archivo      :', elemento)
    print('modificado   :', modificado)        
    print('último acceso:', ult_acceso)
    print('tamaño (Kb)  :', round(tamaño/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))
```
## Ejemplo de TreeView en Tkinter como UI
```python
import tkinter as tk
from tkinter import ttk

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Adding a Vertical Scrollbar to a Treeview Widget")

# create a treeview
tree = ttk.Treeview(window, columns=('Name', 'Age'))

# define the columns
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# add some data to the treeview
tree.insert('', 'end', '1', text='1', values=('Ram', 25))
tree.insert('', 'end', '2', text='2', values=('Mohan', 30))
tree.insert('', 'end', '3', text='3', values=('Shayam', 35))

# pack the treeview
tree.pack()

# start the main loop
window.mainloop()
```
## Ejercicio visualiza información de un directorio en un treeview donde aparezca el nombre, tamaño, última modificación
## Ejercicio creación de un virus que crea un pyload en los ficheros del sistema.

### crear directorios desde python
https://j2logo.com/como-crear-directorios-en-python/

1. Crea una carpeta y escribe tres ficheros txt en python
3. Recorrer el directorio y buscar los ficheros que sean txt
4. Una vez encontrados tienes que poner dentro del fichero una frase Infectado!!
