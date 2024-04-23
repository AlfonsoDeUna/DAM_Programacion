# TUTORIAL 2 DE INVASIÓN ALIELIGENA

## 1. AÑADIR VELOCIDAD A LA NAVE

### Añadir el factor de velocidad en settings

En el constructor
```python
self.ship_speed = 1.5
```

En la clase ship.py
``` python
 def __init__(self, ai_game):
      """Initialize the ship and set its starting position."""
      self.screen = ai_game.screen
      self.settings = ai_game.settings # ESTO LO AÑADIMOS

      # Start each new ship at the bottom center of the screen.
      self.rect.midbottom = self.screen_rect.midbottom

      # Store a float for the ship's exact horizontal position.
      self.x = float(self.rect.x)

      # Movement flags; start with a ship that's not moving.
      self.moving_right = False
      self.moving_left = False

def update(self):
"""Update the ship's position based on movement flags."""
      # Update the ship's x value, not the rect.
      if self.moving_right:
            self.x += self.settings.ship_speed
      if self.moving_left:
            self.x -= self.settings.ship_speed
      # Update rect object from self.x.
            self.rect.x = self.x
```

## 2. AÑADIR LÍMITES DE PANTALLA PARA QUE LA NAVE NO SE VAYA DE LA PANTALLA

Tenemos que comparar la posición de la nave del rectángulo, es decir self.rect.right que contiene el valor que tiene la nave dentro de la pantalla
se encuentra dentro es decir es menor al valor de la pantalla. self.screen_rect.right:

En ship.py...

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

Crea el constructor que luego le añadiremos el resto del código en el punto 4.2
```python
 def __init__(self, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        # Creamos el bullet con un recuadro en la posición 0,0 pero después corregimos la posición de la mismaposition.
        self.rect = pygame.Rect(0, 0, 10, 10)
```

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

En settings.py debes crear los siguientes parámetros en el constructor:

 ```python
# Bullet settings
self.bullet_speed = 2.0
self.bullet_width = 3
self.bullet_height = 15
self.bullet_color = (60, 60, 60)
```

### 4.2 COMPLEAR LA CLASE bullet.py añadiendo el settings Y DEMÁS CÓDIGO DEL CONSTRUCTOR

```python
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

  def __init__(self, ai_game):
    """ Crear la bala donde está la nave """
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    # Crear la bala en el rect (0, 0) .
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
    self.settings.bullet_height)

    self.rect.midtop = ai_game.ship.rect.midtop

    # Store the bullet's position as a float.
    self.y = float(self.rect.y)

  def update(self):
```

Ahora crea el update para que la bala se pueda mover

```python
    def update(self):
      """Move the bullet up the screen."""
      # Update the exact position of the bullet.
      self.y -= self.settings.bullet_speed

      # Update the rect position.
      self.rect.y = self.y
```

Crea el método que dibuja las balas en bullet.py debajo de update()

```python
  def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)

  def __init__(self):
    """ creamos las balas como un grupo"""
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
```


### 4.3 CONFIGURACIÓN DLE JUEGO PRINCIPAL PARA QUE FUNCIONE LOS DISPAROS

Ahora queremos que cuando pulsemos a la barra la nave dispare, para controlar todas las balas 
tenemos en pygame los grupos  Group. Donde gestionamos todas las balas activas en ese momento

En el fichero del juego principal importamos la clase bullet y creamos el grupo como una variable de instancia en el constructor

``` python
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group

```

En el bucle principal del juego:

```python
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self.ship.update()
      self.bullets.update() # aquí ponemos la nueva línea que gestionará las balas
      self._update_screen() 
      self.clock.tick(60)
```

De ese modo con Group las dibujaremos y controlamos su actualizción en pantalla desde el bucle principal del juego

## 5. QUE LA NAVE DISPARE

En el juego principal vamos a añadirle que cuando pulse la barra dispare

```python
def _check_keydown_events(self, event):
    # hay más código
      elif event.key == pygame.K_q:
        sys.exit()
      elif event.key == pygame.K_SPACE:
      self._fire_bullet()

def _check_keyup_events(self, event):
# no copies nada aquí

def _fire_bullet(self):
  """ Creamos el objeto bala y lo añadimos al grupo."""
  new_bullet = Bullet(self)
  self.bullets.add(new_bullet)
```

```python
def _update_screen(self):
"""Update images on the screen, and flip to the new screen."""
  self.screen.fill(self.settings.bg_color)
  for bullet in self.bullets.sprites():
    bullet.draw_bullet()

  self.ship.blitme()
  pygame.display.flip()
```
## 5.1 BORRAR LOS DISPAROS ANTIGUOS

El código del borrado es el siguiente: (lo pongo para explicarlo)

```python
for bullet in self.bullets.copy():
  if bullet.rect.bottom <= 0:
   self.bullets.remove(bullet)
   print(len(self.bullets))
``` 

Utilizamos el copy() para que nos haga una copia y poder modificar las balas que salen del límite que sería cuando llega a la posición 0

Este código tiene que estar en el bucle principal del juego.

Qudaría así:

```python

def run_game(self):
  """Start the main loop for the game."""
  while True:
   self._check_events()
   self.ship.update()
   self.bullets.update()

    # Borrado de las balas
   for bullet in self.bullets.copy():
    if bullet.rect.bottom <= 0:
      self.bullets.remove(bullet)
      print(len(self.bullets))

   self._update_screen()
```

## 5.2 LIMITAR EL NÚMERO DE MISILES

## 6. REFACTORIZACIÓN DEL CÓDIGO PARA QUE QUEDE EL CÓDIGO MÁS BONITO


