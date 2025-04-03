import pygame
from screen import GameScreen
from game_screens import change_screen, dict_screens
import sys

class Menu(GameScreen):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.display.fill((200, 0, 0))


dict_screens['menu'] = Menu()
print(dict_screens)