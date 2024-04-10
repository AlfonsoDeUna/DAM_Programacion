# Creación de un juego en Pygame

## Crea InvasionAlieligena.py

```python
import sys
import pygame

class AlienInvasion:
    
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((largo, ancho))
        pygame.display.set_caption("Invasion Aliligena")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
```

### A partir del código inicial añade los siguientes cambios para dar forma a la pantalla principal del juego

* añade al método set_mode del constructor que la pantalla sea de 1200, 800 píxeles
* añade al caption para que tenga un título que ponga Invasión alieligena
* 
