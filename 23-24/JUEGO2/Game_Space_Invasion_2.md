# TUTORIAL 2 DE INVASIÓN ALIELIGENA

## 1. AÑADIR VELOCIDAD A LA NAVE

## 2. AÑADIR LÍMITES DE PANTALLA PARA QUE LA NAVE NO SE VAYA DE LA PANTALLA

## 3. AÑADIR PANTALLA COMPLETA AL JUEGO

## 4. DISPARAR MISILES 

Vamos a crear la clase Bullet que hereda de sprite

```python
class Bullet(Sprite):
```
importa Sprite de pygames al principio del código

```python
from pygame.sprite import Sprite
```

Las balas son rectángulos que tienen un width y un height más adelante podemos añadirlos a settings pero por ahora lo ponemos hardcodeado en el init de la clase bullet

```python
 def __init__(self, screen):

        super(Bullet, self).__init__()
        self.screen = screen

        # Creamos el bullet con un recuadro en la posición 0,0 pero después corregimos la posición de la mismaposition.
        self.rect = pygame.Rect(0, 0, 10, 10)
      
```
Vamos a añadirle dos parámetros a las balas color de las balas y velocidad de las mismas

```python
    self.color = (0,0,0)
    self.speed_factor = 2
```

Ahora vamos a crear los dos métodos que creamos para nuestros objetos del juego uno de ellos update () para actualizar su posición
dentro del juego con respecto al tiempo y otro para que dibuje la bala

```python
  def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

### 4.1 CREAR LOS ATRIBUTOS DE SETTINGS PARA LOS DISPAROS 

### 4.2 CREAR LA CLASE MISILES.PY

### 4.3 CONFIGURACIÓN DLE JUEGO PRINCIPAL PARA QUE FUNCIONE LOS DISPAROS

## 5. QUE LA NAVE DISPARE

## 5.1 BORRAR LOS DISPAROS ANTIGUOS

## 5.2 LIMITAR EL NÚMERO DE MISILES

## 6. REFACTORIZACIÓN DEL CÓDIGO PARA QUE QUEDE EL CÓDIGO MÁS BONITO


