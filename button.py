import pygame
from settings import WIDTH, HEIGHT

class Button:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font_audiowide = pygame.font.Font("fonts/Audiowide-Regular.ttf", 36)
        self.font_monoton = pygame.font.Font("fonts/Monoton-Regular.ttf", 36)
        self.font_orbitron = pygame.font.Font("fonts/Orbitron-VariableFont_wght.ttf", 36)

        self.font_bungee = pygame.font.Font("fonts/Bungee-Regular.ttf", 36)
        self.font_kumar = pygame.font.Font("fonts/KumarOne-Regular.ttf", 36)
        self.font_sonsie = pygame.font.Font("fonts/SonsieOne-Regular.ttf", 36)
    
    def button_start(self):
        button_start = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 160, 50)
        return button_start
    
    def button_start_draw(self):
        self.surf_start = self.font_sonsie.render("Start", True, (255, 255, 255))
        pygame.draw.rect(self.display, (255, 0, 204),  self.button_start())
        self.display.blit(self.surf_start, (self.button_start().x + 10, self.button_start().y))
    
    def button_exit(self):
        button_exit = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 160, 50)
        return button_exit
    
    def button_exit_draw(self):
        self.surf_exit = self.font_sonsie.render("Exit", True, (255, 255, 255))
        pygame.draw.rect(self.display, (255, 0, 204), self.button_exit())
        self.display.blit(self.surf_exit, (self.button_exit().x + 25, self.button_exit().y))