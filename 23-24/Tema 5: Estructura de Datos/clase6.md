# Numpy

NumPy es una biblioteca para el lenguaje de programación Python que da soporte para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas.

```python

import numpy as np
import matplotlib.pyplot as plt

# ejemplo de como utilizar 
vector = np.arange(5)
print (vector)

matriz = np.arange(9).reshape(3,3)
print (matriz)

tensor = np.arange(12).reshape(3,2,2)
print (tensor)

# arrays

a = np.array([1,2,3,4,5,6])
print (a)

m = np.array([[1,2],[1,2]])
print (m)

# como crear arrays con secuencias
print (np.arange(start=2, stop=10, step=1))
print (np.arange(start=2, stop=10, step=2))
print (np.arange(start=20, stop=10, step=-2))

# otra manera linspace pero aquí le decimos el tamaño del array
print (np.linspace(start=1,stop=11,num=20))

# lista o matriz de ceros
print (np.zeros(9))
print (np.zeros((2,2)))

#unos
print (np.ones(10))

#full
print (np.full (shape=(2,2), fill_value=5))

# ------------------------------------------------------------------

x = np.linspace(-3,0,20)
y = -np.e**x

plt.plot(x,y)
plt.show()

# -------------------------------------------------------------------

### vector de números aletarios

print (np.random.rand(2,2))

### gráfico de calor

x = np.random.rand(30,30)
plt.imshow(x,cmap=plt.cm.hot)
plt.colorbar()
plt.show()

### gráfico 3D
#from mayavi import mlab
#mlab.surf(x)
#mlab.axes()

### crea un vector de ceros de tamaño 10 y que el quinto valor sea un 1
vector = np.zeros(10)
print (vector)
vector[5] = 1

```
