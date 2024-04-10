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
La imagen de la nave te la he dejado en github dentro de la carpeta images con el nombre ship.bmp descárgala de aquí y ponla en la carpeta images en visual Studio Code

### Vamos a añadir la clase ship.py al juego para ello importamos la clase en invasionalieligena.py

```python
from ship import ship
```

Añade en el constructor de invasionalieligena.py una instancia de la nave con la variable de instancia ship, te dejo el código

```python
self.ship = Ship(self)
```
Ahora en el bucle principald el juego en invasionalieligena.py después del método screen.fill() que rellena de color la pantalla principal vamos a pintar la nave
copia el siguiente código que llama al método blitme que dibuja la nave gracias al método blit que pusimos dentro de este métoodo en ship

```python
self.ship.blitme()
```

### PRUEBA ESTE CÓDIGO, DALE A EJECUTAR, SE TIENE QUE VER LA NAVE PERO CLARO, NO SE MUEVE ,JEJEJE, AHORA TENEMOS QUE AÑADIR LOS EVENTOS PARA QUE CUANDO
PULSEMOS UNA TECLA LA TENGMAOS IDENTIFICADA Y PODAMOS MOVER LA NAVE PRINCIPAL...

### 6. EVENTOS

Crea este método después del método de clase run_game () de la clase invasionalieligena.py

```python
 def _check_events(self):
        """método que responde a los eventos que se producen en la pantalla del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
```

Claro, este método copia el código que tienes que quitar de run_game() de los eventos y en vez de ese código ahora debes llamar a ese método dentro
del run_game(), pon esto, justo debajo del while (true) que es bucle principal y quitas las líneas repetidas en este método que por tanto llamará:

``` python
self._check_events()
```

Ahora pasa lo mismo con el código que tiene run_time para pintar en pantalla todos los métodos blint() vamos a crear un método debajo del método check_events()
y añadimos este:

```python
    def _update_screen(self):
        """Actualiza las imágenes de pantalla y pinta la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
```

Ahroa tienes que quitar estas líneas de run_game() y sustituirlo por el método _update_screen(), por tanto run_game() quedará así

```python
def run_game(self):

    while True:
        self._check_events()
        self._update_screen()
        self.clock.tick(60)
```

### 6. Añadir movimiento a la nave derecha e izquierda

Añade al método check events el siguiente código, movemos a la nave un pixel a la derecha por eso sumamos uno

```python
elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        self.ship.rect.x += 1
```

El método quedará así:

```python
    def _check_events(self):
        """método que responde a los eventos que se producen en la pantalla del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
```

### Ahora, a ver si eres capaz, de añadir hacia la izquierda, ten en cuenta que restaremos un pixel ;)

### PRUEBA EL CÓDIGO, EJECÚTALO Y MIRA SI ERES CAPAZ DE MOVER LA NAVE

### 7. Movimiento contínuo, simplemente dejando el cursor derecha pulsado seguirá la nave moviéndose y no hace falta estar pulsando muchas veces la tecla

Crea en el constructor de la clase ship.py el atributo de instancia moving_right = False

Y crea el siguiente método en ship.py

```python
def update(self):
    # actualiza el movimiento de la nave dependiendo si la variable right es true
    if self.moving_right:
        self.rect.x += 1
```

En la clase invasionalieligena.py deberás modificar el metodo check_events() por este código que modfiica el valor el valor
de la variable de instancia de la nave moving_right

```python
    def _check_events(self):
        """método que responde a los eventos que se producen en la pantalla del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
```

Y en el método run_game de invasionalieligena.py añade self.ship.update() para que llame al método update de ship para que se pueda mover la nave.
El método run_game quedará así:

```python
def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
```
