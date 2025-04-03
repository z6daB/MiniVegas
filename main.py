import pygame
from game_screens import get_current_screen, change_screen, add_screen
from settings import WIDTH, HEIGHT

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

import menu

class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("MiniVegas")

        add_screen('menu', menu.Menu())
        change_screen('menu')

    def run(self):
        while True:
            get_current_screen().run()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    main = Main()
    main.run()