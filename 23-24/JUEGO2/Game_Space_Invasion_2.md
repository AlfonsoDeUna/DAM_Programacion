# TUTORIAL 2 DE INVASIÓN ALIELIGENA

## 1. AÑADIR VELOCIDAD A LA NAVE

### Añadir el factor de velocidad en settings

```python

```

``` python
  self.center += self.ai_settings.ship_speed_factor
```
Para la izquierda le resto el factor de velocidad 
```python
self.center -= self.ai_settings.ship_speed_factor
```
## 2. AÑADIR LÍMITES DE PANTALLA PARA QUE LA NAVE NO SE VAYA DE LA PANTALLA

Tenemos que comparar la posición de la nave del rectángulo, es decir self.rect.right que contiene el valor que tiene la nave dentro de la pantalla
se encuentra dentro es decir es menor al valor de la pantalla. self.screen_rect.right:

```python
 def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center
```

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
 def __init__(self, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        # Creamos el bullet con un recuadro en la posición 0,0 pero después corregimos la posición de la mismaposition.
        self.rect = pygame.Rect(0, 0, 10, 10)
      
```
Ahora vamos a situar la bala en la posición donde se encuentra la nave, para ello dentro del constructor añade las siguientes líneas justo después donde creamos el rectángulo que será la bala del python anterior.

Además vamos a añadir después la información en decimal de la posición de la bala en el eje y que es por donde se mueve. self.y = float(self.rect.y)

```python
   self.rect.centerx = ship.rect.centerx
   self.rect.top = ship.rect.top
   self.y = float(self.rect.y)
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


