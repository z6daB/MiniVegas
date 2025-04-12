import pygame
from game_screens import get_current_screen, change_screen, add_screen
from settings import WIDTH, HEIGHT, PLAYLIST

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

import menu
import game


class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.playList = PLAYLIST
        pygame.display.set_caption("MiniVegas")

        add_screen('menu', menu.Menu())
        change_screen('menu')

    def run(self):
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.mixer.music.load(self.playList[0]) 
        self.playList.pop(0) 
        pygame.mixer.music.play() 
        pygame.mixer.music.queue(self.playList[0]) 
        self.playList.pop(0) 

        while True:
            get_current_screen().run()
            # for event in pygame.event.get(): 
            #     if event.type == pygame.USEREVENT + 1:
            #         if len(self.playList) > 0: 
            #             pygame.mixer.music.queue(self.playList[0]) 
            #             self.playList.pop(0) 
            #     if not pygame.mixer.music.get_busy(): 
            #         print("Playlist completed") 
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    main = Main()
    main.run()