# COMO PROGRAMAR APLICACIONES GRÁFICAS DE ESCRITORIO EN PYTHON

Tkinter es una interfaz de Python para la biblioteca gráfica Tk.

## Agregar a la librería 
```python
from Tkinter import *

```

## Características principales

Tkinter te permite crear ventanas con widgets en ellas

Un widget es un componente gráfico en la pantalla (botón, etiqueta de texto, menú desplegable,
barra de desplazamiento, imagen, etc...)

Las interfaces gráficas de usuario (GUIs) se construyen organizando y combinando
diferentes widgets en la pantalla

## Crea tu primera ventana

```Python
from Tkinter import *

root = Tk() # Create the root (base) window where all widgets go
w = Label(root, text="Hello, world!") # Create a label with words
w.pack() # Put the label into the window
root.mainloop() # Start the event loop
```

Label es una clase, w es un objeto
w = Label(root, text="¡Hola, mundo!") y Llama a la operación "pack":


## Añade botones a las pantallas

``` python

from Tkinter import *
root = Tk() # Create the root (base) window where all widgets go
w = Label(root, text="Hello, world!") # Create a label with words
w.pack() # Put the label into the window
myButton = Button(root, text="Exit")
myButton.pack()
root.mainloop() # Start the event loop
```
Si queremos añadir funcionalidad al botón tenemos que añadirle código

```python
myButton = Button(root, text="Exit",command=buttonPushed)
```
Le estamos diciendo que ese botón tiene que llamar a un método llamad buttonPushed

```python
from Tkinter import *
# Hold onto a global reference for the root window
root = None

def buttonPushed():
  global root
  root.destroy() # Kill the root window!

def main():
  global root
  root = Tk() # Create the root (base) window where all widgets go
  w = Label(root, text="Hello, world!") # Create a label with words
  w.pack() # Put the label into the window
  myButton = Button(root, text="Exit",command=buttonPushed)
  myButton.pack()
  root.mainloop() # Start the event loop

main()
```
## Crea una caja de texto

Forma general para todos los widgets:
1. # Crear el widget
widget = <nombreDelWidget>(padre, atributos...)

2. widget.pack()
empaqueta el widget para hacer que se muestre

```python
def createTextBox(parent):
  tBox = Entry(parent)
  tBox.pack()

#From main call:
createTextBox(root)
```

### ejemplo: 

```python
#Textentrybox1.py
from Tkinter import *

# Hold onto a global reference for the root window
root = None

# Hold onto the Text Entry Box also
entryBox = None

def buttonPushed():
  global entryBox
  txt = entryBox.get()
  print "The text is:",txt

def createTextBox(parent):
  global entryBox
  entryBox = Entry(parent)
  entryBox.pack()

def main():
  global root
  root = Tk() # Create the root (base) window where all widgets go
  myButton = Button(root, text="Show Text",command=buttonPushed)
  myButton.pack()
  createTextBox(root)
  root.mainloop() # Start the event loop

main()
```
### Ejemplo crear un Label que pudes manipular

```python
#changeable_label.py
# Use a StringVar to create a changeable label
from Tkinter import *

# Hold onto a global reference for the root window
root = None

# Changeable text that will go inside the Label
myText = None
count = 0 # Click counter

def buttonPushed():
  global myText
  global count
  count += 1
  myText.set("Stop your clicking, it's already been %d times!" %(count))

def addTextLabel(root):
  global myText
  myText = StringVar()
  myText.set("")
  myLabel = Label(root, textvariable=myText)
  myLabel.pack()

def main():
  global root
  root = Tk() # Create the root (base) window where all widgets go
  myButton = Button(root, text="Show Text",command=buttonPushed)
  myButton.pack()
  addTextLabel(root)
  root.mainloop() # Start the event loop
```

# Layout

El layout como distribuimos los elementos gráficos o widgets en pantalla como se distribuyen

Con el método pack, podemos disitrubir los elementos en la pantalla

myWidget.pack(side=LEFT)

```python
#pack_sample.py
from Tkinter import *

# Hold onto a global reference for the root window
root = None
count = 0 # Click counter

def addButton(root, sideToPack):
  global count
  name = "Button "+ str(count) +" "+sideToPack
  button = Button(root, text=name)
  button.pack(side=sideToPack)
  count +=1

def main():
  global root
  root = Tk() # Create the root (base) window where all widgets go
  for i in range(5):
    addButton(root, TOP)
  root.mainloop() # Start the event loop

main()
```

### EJERCICIO: Crea varios botones para que se puedan distruibir en la pantalla LEFT, BOTTOM, RIGHT, TOP

# FRAMES
Son  estructuras para almacenar otros widgets dentro de ellos, son como padres de otros elementos

# CAPTURAR LOS EVENTOS DE RATÓN

# CREAR UN MESAGEBOX 

# DIÁLOGOS DE ENTRADA DE DATOS
