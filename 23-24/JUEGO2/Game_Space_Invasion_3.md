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

Añade al settings.py la propiedad velocidad de los aliens en el constructor

```python
# Alien settings
self.alien_speed = 1.0
```

En aliens.py en su constructor añade los settings de la clase settings

```python
def __init__(self, ai_game):
super().__init__()
self.screen = ai_game.screen
self.settings = ai_game.settings
##### hay más código después
```

```python
def update(self):
  # mueve a la derecha el alien
  self.x += self.settings.alien_speed
  self.rect.x = self.x

```
y ya por último añadir el update en la clase principal del juego dentro del bucle del juego

```python
while True:
  self._check_events()
  self.ship.update()
  self._update_bullets()
  self._update_aliens()
  self._update_screen()
  self.clock.tick(60)
```

y crea el método _update_aliens(self): en la clase principal del juego ya que en el código anterior hemos hecho la llamada

```python
def _update_aliens(self):
  """Update the positions of all aliens in the fleet."""
  self.aliens.update()
```

En settings por útlimo añade los siguiente parámetros para la dirección de los aliens

```python
# Alien settings
self.alien_speed = 1.0
self.fleet_drop_speed = 10
# fleet_direction of 1 represents right; -1 represents left.
self.fleet_direction = 1
```

### 3.2 DETECTAR LOS LÍMITES DE PANTALLA PARA LOS MOVIMIENTOS DE LA FLOTA DE ALIENS Y CAMBIO DE SENTIDO

En el alien.py tienes que crear este método check_edges(self): Está mirando los límites

```python

def check_edges(self):
  screen_rect = self.screen.get_rect()
  eturn (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

```

En el update de alien.py tienes que poner este código

```python
def update(self):
  # Mueve el alien a la derecha o a la izquierda dependiendo del valor del fleet_direction
  self.x += self.settings.alien_speed * self.settings.fleet_direction
  self.rect.x = self.x
 ```

En el programa principal crea los métodos check_fleet_edges(self) y change_fleet_direction(self):

```python
def _check_fleet_edges(self):
"""Si detecta un borde los alines cambia la dirección"""
  for alien in self.aliens.sprites():
    if alien.check_edges():
      self._change_fleet_direction()
      break

def _change_fleet_direction(self):
  """Cambio de la dirección"""
  for alien in self.aliens.sprites():
    alien.rect.y += self.settings.fleet_drop_speed
  self.settings.fleet_direction *= -1
```

Y por último en el programa principal también hay que modificar el método _upadte_aliens(self) que hemos creado anteriormente
para que tenga en cuenta los cambios de dirección de los alines

```python
def _update_aliens(self):
  self._check_fleet_edges()
  self.aliens.update()
```

## 4. DISPARANDO A LOS ALIENS !!

En primer lugar modifica la velocidad de las balas. En settings.py modifica este párametro al valor 2.5

```python
# Bullet settings
self.bullet_speed = 2.5
self.bullet_width = 3
```

Podemos refactorizar el código un poco para mejorarlo. La parte de la actualización de las balas para añadir nuevo código
Quedaría así el método _update_bullets() del programa principal le añadimos un método _check_bullet_alien_collisions()

La idea es que cuando detectemos que los grupos colisionan nos lo da sprites cuando se detectan los recuadros de los alines y las balas
es que están juntos o superpuestos y es como que le ha tocado la bala al alien

```python

def _update_bullets(self):

  for bullet in self.bullets.copy():
  if bullet.rect.bottom <= 0:
  self.bullets.remove(bullet)
  ######################## este código anterior ya existe no toques nada añde el método este:
  self._check_bullet_alien_collisions()

def _check_bullet_alien_collisions(self):

  # Remove any bullets and aliens that have collided.
  collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
  if not self.aliens:
    # Destroy existing bullets and create new fleet.
    self.bullets.empty()
    self._create_fleet()
```
### 4.1 TRUCO PARA TESTEAR EL JUEGO. MODIFICANDO LOS MISÍLES DE DESTRUCCIÓN MASIVA DE ALIENS

## 5. OH SHIT!! LOS ALIENS SE MULTIPLICAN !!!

## 6. OTRAS MODIFICACIONES

### 6.1 LA VELOCIDAD DE LOS MISILES

## 7. ¡¡ NOS ATACAN LOS ALIENS !! FIN DEL JUEGO. GAME OVER!

