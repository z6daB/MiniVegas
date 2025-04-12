import sys
import pygame

from game_screens import change_screen, dict_screens
from screen import GameScreen
from slots import Slot


class Game(GameScreen):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.slot = Slot()
        self.table = self.slot.get_table()
    
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not self.slot.animating:  # запускать только если не в процессе
                    final_table = self.slot.get_table()
                    self.slot.start_animation(final_table)
                    self.table = final_table  # обновим table после окончания анимации
    
    def update(self):
        self.slot.update_animation()

    def draw(self):
        self.display.fill((0, 0, 0))
        if self.slot.animating:
            print("animating")
            anim_imgs = self.slot.get_animating_images()
            for col in range(self.slot.cols):
                for row, img in enumerate(anim_imgs[col]):
                    y_offset = -self.slot.offsets[col]
                    x = (col + 1.5) * 100
                    y = (row + 1) * 100 + y_offset
                    self.display.blit(img, (x, y))
        else:
            
            for row in range(self.slot.rows):
                for col in range(self.slot.cols):
                    img = pygame.transform.scale(
                        pygame.image.load(self.table[row][col]), (100, 100)
                    )
                    self.display.blit(img, ((col + 1.5) * 100, (row + 1) * 100))


dict_screens['game'] = Game()