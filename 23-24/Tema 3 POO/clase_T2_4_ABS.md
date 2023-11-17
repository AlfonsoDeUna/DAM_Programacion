# 1. Introducción a las Clases Base Abstractas (ABCs):

Concepto de ABCs: En Python, una Clase Base Abstracta es una clase que no se puede instanciar y que define un conjunto de métodos y propiedades que deben ser implementados por sus subclases.

```python
from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def update(self):
        pass
```
# 2. ABCs en el Desarrollo de Videojuegos:

Ejemplo de ABC para Enemigos:
Supongamos que estamos creando diferentes tipos de enemigos en un juego. Todos ellos deben tener ciertas acciones comunes como atacar y recibir daño.
```python
class Enemy(GameObject):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass
```

# 3. Ejemplo Práctico: Creando una Clase Base Abstracta para Enemigos:
Implementación de Subclases:
Crearemos dos tipos de enemigos: Zombie y Robot, que implementan los métodos de la clase abstracta Enemy.
```python

class Zombie(Enemy):
    def attack(self):
        return "El zombie muerde."

    def take_damage(self, damage):
        return f"El zombie recibe {damage} puntos de daño."

class Robot(Enemy):
    def attack(self):
        return "El robot dispara un láser."

    def take_damage(self, damage):
        return f"El robot recibe {damage} puntos de daño."
```

# 4. Actividad de Codificación en Clase:
Tarea para los Alumnos:
Crear una ABC para otro componente del juego, como Item.
Implementar dos subclases que extienden Item.

```python
class Item(GameObject):
    @abstractmethod
    def use(self):
        pass

class Potion(Item):
    def use(self):
        return "Usas una poción para recuperar salud."

class Bomb(Item):
    def use(self):
        return "Lanzas una bomba causando daño."
```
# 5. Discusión y Reflexión:
Preguntas para la Reflexión:
* ¿Cómo ayudan las ABCs a garantizar que diferentes clases en un juego compartan una interfaz común?
* ¿Pueden identificar juegos donde se podrían aplicar estas prácticas?

---

# Ejemplo de clase

```python
from abc import ABC, abstractmethod

class Armas (ABC):
    
    @abstractmethod
    def disparar(self):
        pass
    
class pistola (Armas):
    
    def __init__ (self, num_balas):
        self.cargador = num_balas
    
    def disparar (self):
        if (self.cargador > 0):
            print ("disparo una bala....PUM!!!")
            self.cargador = self.cargador - 1
        else:
            print ("recarga las balas!!")
            
            
class ametralladora (Armas):
    
    def __init__ (self, num_balas):
        self.cargador = num_balas
    
    def disparar (self):
        if (self.cargador > 0):
            print ("disparo muchas ba, bal, balaaa, balaaaassss....PUM!!!")
            self.cargador = self.cargador - 5
        else:
            print ("recarga las balas!!")         
    
class Juego:        

    def __init__(self, Armas):
        self.arma = Armas
    
    def iniciar(self):
       self.arma.disparar()

       
tipoArma = pistola(5)
game = Juego(tipoArma)

game.iniciar()
```

