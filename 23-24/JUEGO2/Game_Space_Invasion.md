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
