import math
import pygame
import sys

from screen import GameScreen
from game_screens import change_screen, dict_screens

from settings import WIDTH, HEIGHT, TOP_COLOR, BOTTOM_COLOR

class Menu(GameScreen):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.start_time = pygame.time.get_ticks()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def interpolate(self, c1, c2, t):
        return tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))

    def draw_vertical_gradient(self, surface, top_color, bottom_color):
        for y in range(HEIGHT):
            ratio = y / HEIGHT
            color = self.interpolate(top_color, bottom_color, ratio)
            pygame.draw.line(surface, color, (0, y), (surface.get_width(), y))

    def draw_glowing_stripe(self, surface, base_color, x1, y1, x2, y2):
        for i in range(8, 0, -2):
            glow_color = tuple(min(255, int(c * 0.5)) for c in base_color)
            pygame.draw.line(surface, glow_color, (x1, y1), (x2, y2), i)
        pygame.draw.line(surface, base_color, (x1, y1), (x2, y2), 2)

    def draw_moving_stripes(self, surface, base_color, offset):
        spacing = 50
        for x in range(-WIDTH, WIDTH, spacing):
            x1 = x + offset
            x2 = x1 + HEIGHT
            self.draw_glowing_stripe(surface, base_color, x1, 0, x2, HEIGHT)

    def draw(self):
        self.draw_vertical_gradient(self.display, TOP_COLOR, BOTTOM_COLOR)

        now = pygame.time.get_ticks()
        flicker_intensity = (math.sin(now / 300) + 1) / 2  # значение от 0 до 1
        stripe_color = self.interpolate((255, 255, 102), (255, 255, 255), flicker_intensity)

        offset = (now // 30) % 100
        self.draw_moving_stripes(self.display, stripe_color, offset)


dict_screens['menu'] = Menu()
