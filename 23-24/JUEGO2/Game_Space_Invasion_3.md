# ¡¡QUÉ VIENEN LOS ALIENS!! NOS INVADEN

## 1. CREAR LA CLASE ALIENS


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
# Start each new alien near the top left of the screen.
1 self.rect.x = self.rect.width
self.rect.y = self.rect.height
# Store the alien's exact horizontal position.
2 self.x = float(self.rect.x)
```

### 1.1 INSTANCIAR EN EL JUEGO LOS ALIENS

## 2. CONSTRUIR UNA FLOTA DE ALIENS

### 2.1 CREAR UNA FILA DE ALIENS

### 2.2 AÑADIR MÁS LÍNEAS

## 3. AÑADIR MOVIMIENTO A LOS ALIENS

### 3.1 MOVER A LA DERECHA LOS ALIENS

### 3.2 DETECTAR LOS LÍMITES DE PANTALLA PARA LOS MOVIMIENTOS DE LA FLOTA DE ALIENS Y CAMBIO DE SENTIDO

## 4. DISPARANDO A LOS ALIENS !!

### 4.1 TRUCO PARA TESTEAR EL JUEGO. MODIFICANDO LOS MISÍLES DE DESTRUCCIÓN MASIVA DE ALIENS

## 5. OH SHIT!! LOS ALIENS SE MULTIPLICAN !!!

## 6. OTRAS MODIFICACIONES

### 6.1 LA VELOCIDAD DE LOS MISILES

## 7. ¡¡ NOS ATACAN LOS ALIENS !! FIN DEL JUEGO. GAME OVER!

