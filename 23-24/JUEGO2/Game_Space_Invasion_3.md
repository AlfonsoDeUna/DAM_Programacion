# ¡¡QUÉ VIENEN LOS ALIENS!! NOS INVADEN

## 1. CREAR LA CLASE ALIENS

Crea Alien.py

```python

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  
  def __init__(self, ai_game):
 
    super().__init__()
    self.screen = ai_game.screen

    # Cargamos la imagen de los alien.
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()
    # Lo vamos a situar arriba del todo de la pantalla
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    # La posición de los alines es muy exacta por tanto la vamos a crear como un número con decimales para ser más precisos
    self.x = float(self.rect.x)
```

### 1.1 INSTANCIAR EN EL JUEGO LOS ALIENS

En el python principal vamos a instanciar e importar la clave alien

```python
from alien import Alien

```
En el init del progrmaa principal tenemos que crear grupo. Añádelo al final

``` python

def __init__(self):
##### hay más código pro aquí#####
  self.ship = Ship(self)
  self.bullets = pygame.sprite.Group()
  self.aliens = pygame.sprite.Group()
  self._create_fleet()
```

Crea el método _create_fleet()
```python
def _create_fleet(self):
  
  # Make an alien.
  alien = Alien(self)
  self.aliens.add(alien)
```

En el update_screen() crea el draw de alien

``` python
def _update_screen(self):
  #### tendrás más código ####
  self.ship.blitme()
  self.aliens.draw(self.screen)
  pygame.display.flip()
```

PRUEBA A VER SI VES LAS NAVES ALIENS

## 2. CONSTRUIR UNA FLOTA DE ALIENS

Vamos a crear tantos alines como quepan en pantalla. Modificamos el _create_fleet(self):

```python
def _create_fleet(self):
  """Create the fleet of aliens."""
  # Create an alien and keep adding aliens until there's no room left.
  # Spacing between aliens is one alien width.
  alien = Alien(self)
  alien_width = alien.rect.width
  current_x = alien_width
  while current_x < (self.settings.screen_width - 2 * alien_width):
    new_alien = Alien(self)
    new_alien.x = current_x
    new_alien.rect.x = current_x
    self.aliens.add(new_alien)
    current_x += 2 * alien_width
```

PRUÉBALO AHORA. TIENES QUE VER UNA LÍNEA DE ALIENS

### 2.1 CREAR FILAS DE ALIENS

copia de nuevo y sustituye el código de antes ahora intenta añadir una línea 

```python
def _create_fleet(self):
  
  # 
  alien = Alien(self)
  alien_width, alien_height = alien.rect.size
  current_x, current_y = alien_width, alien_height
  while current_y < (self.settings.screen_height - 3 * alien_height):
    while current_x < (self.settings.screen_width - 2 * alien_width):
      self._create_alien(current_x, current_y)
      current_x += 2 * alien_width

  # finzaliza la línea
  current_x = alien_width
  current_y += 2 * alien_height

```

tienes que añadir este método que es el que crea el alien

```python
def _create_alien(self, x_position, y_position):

  new_alien = Alien(self)
  new_alien.x = x_position
  new_alien.rect.x = x_position
  new_alien.rect.y = y_position
  self.aliens.add(new_alien)
```

PRUEBA AHORA

## 3. AÑADIR MOVIMIENTO A LOS ALIENS

### 3.1 MOVER A LA DERECHA LOS ALIENS

### 3.2 DETECTAR LOS LÍMITES DE PANTALLA PARA LOS MOVIMIENTOS DE LA FLOTA DE ALIENS Y CAMBIO DE SENTIDO

## 4. DISPARANDO A LOS ALIENS !!

### 4.1 TRUCO PARA TESTEAR EL JUEGO. MODIFICANDO LOS MISÍLES DE DESTRUCCIÓN MASIVA DE ALIENS

## 5. OH SHIT!! LOS ALIENS SE MULTIPLICAN !!!

## 6. OTRAS MODIFICACIONES

### 6.1 LA VELOCIDAD DE LOS MISILES

## 7. ¡¡ NOS ATACAN LOS ALIENS !! FIN DEL JUEGO. GAME OVER!

