# Creación de un juego en Pygame

Crea una carpeta que ponga Game_space y lo abres en Visual Studio Code para crear el juego

## 1. Crea InvasionAlieligena.py copia este código en la carpeta del juego recien creada

```python
import sys
import pygame

class AlienInvasion:
    
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """CONSTRUCTOR DEL JUEGO DONDE INICIALIZAMOS LAS VARIABLES MÁS IMPORTANTES."""
        pygame.init()
        self.screen = pygame.display.set_mode((largo, ancho))
        pygame.display.set_caption("tÍTULO DE LA PANTALLA DEL JUEGO")

    def run_game(self):
        """BUCLE PRINCIPAL DEL JUEGO"""
        while True:
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
        # flip() es eñ emcargadp de dibujar los elementos del juego 
        pygame.display.flip()

if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
```

### 2. A partir del código inicial añade los siguientes cambios para dar forma a la pantalla principal del juego

* añade al método set_mode del constructor que la pantalla sea de 1200, 800 píxeles
* añade al caption para que tenga un título que ponga Invasión alieligena

### EJECUTA EL PYTHON

### 3.1 Crear el Frame Rate
 (frame rate) en un juego se refiere a la velocidad a la que se actualizan los gráficos en pantalla. Mantener una frecuencia de cuadros constante es importante para garantizar una experiencia de juego suave y consistente, independientemente del sistema en el que se ejecute el juego.

Añade al constructor de invasionalieligena.py el siguiente código
 ``` python
self.clock = pygame.time.Clock()
```

Añade en el bucle principal después del método flip() el siguiente código. Para que el juego funcione a 60 fps 
Si queremos tener mayor tasa de refresco debemos modificar este parámetro
```python
self.clock.tick(60)
```

### 3.2 Modificar el color de fondo

Añade el siguiente código en el constructor de invsasionaliegena.py
```python
self.bg_color = (230, 230, 230)
```

Modifica si quieres el color de fondo modficando los valores octales RGB, cada número representa la combinación del Rojo, Verde y Azul

Ahora añade antes del display.flip() del bucle principal para que añada ese color de fondo:

```python
self.screen.fill(self.bg_color)
```

### PRUEBA EL CÓDIGO

### 4. CREACIÓN DE LA CLASE SETTINGS

Hemos creado color y control de fps. Pero está a fuego vamos a crear una clase que sea capaz de configurar esos valores de color de fondo y tasa de refresco

#### Crea la clase settings.py

#### Crea el constructor sin parámetros y añade lo siguiente

Crea las siguietnes variables de instancia con los valores que te pongo a continuación
ancho_pantalla = 1200
largo_pantalla = 800
bg_color = (230,230,230)

Puedes modificar este último parámetro por el código de color que has elegido previamente en el paso anterior.

Ahora importa la clase settings en invasionaliligena.py 

```python
from settings import Settings
```

Añade al constructor de invasionaliligena.py la instancia a settings y modifica los valores anteriores para que los pille de settings

```python
from settings import Settings
```
Dentro del constructor

```python
self.settings = Settings()
self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
```
Ahora modifica también en el constructor el self.screen.fill() para que lo pille de self.settings.bg_color

### 5. AÑADE NUESTRA NAVE

Crea la clase ship.py y añade el siguiente código

```python
import pygame
class Ship:
    """Clase que gestiona la nave."""
    
    def __init__(self, ai_game):
    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
    
    # Cargamos la imagen de la imagen y la asociamos a un rectángulo para que sea más fácil gestionar
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
    # Posicionamos la nave en la mitad de fondo de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Dibuja la nave en la posición actual."""
        self.screen.blit(self.image, self.rect)
```

Crea una carpeta image dentro de la carpeta principal del juego y añade la nave que la dejo aquí como ship.bmp (descárgala y ponla en la carpeta)

### Vamos a añadir la clase ship.py al juego para ello importamos la clase en invasionalieligena.py

```python
from ship import ship
```






