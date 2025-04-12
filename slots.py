import pygame
from random import choice


class Slot:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.symbols = [
            'graphics/slots/apple.png', 'graphics/slots/bell.png', 'graphics/slots/cherries.png', 'graphics/slots/diamond.png',
            'graphics/slots/grape.png', 'graphics/slots/lemon.png', 'graphics/slots/plum.png', 'graphics/slots/seven.png', 'graphics/slots/watermelon.png'
        ]
        self.rows = 3
        self.cols = 5
        self.table = self.get_table()

        self.animating = False
        self.scroll_stacks = [[] for _ in range(self.cols)]
        self.offsets = [0 for _ in range(self.cols)]
        self.stopping = [False for _ in range(self.cols)]
        self.frame_counters = [0 for _ in range(self.cols)]
    
    def get_table(self):
        return [
            [choice(self.symbols) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
    def start_animation(self, final_table):
        self.animating = True
        self.final_table = final_table
        self.offsets = [0 for _ in range(self.cols)]
        self.frame_counters = [30 * (i + 1) for i in range(self.cols)]  # задержка для каждого столбца
        self.done = [False] * self.cols
        self.scroll_stacks = []

        for col in range(self.cols):
            # Прокручиваем 15 случайных символов + 3 финальных
            symbols = [choice(self.symbols) for _ in range(15)] + [
                final_table[row][col] for row in range(self.rows)
            ]
            images = [pygame.transform.scale(pygame.image.load(s), (100, 100)) for s in symbols]
            self.scroll_stacks.append(images)

    def update_animation(self):
        if not self.animating:
            return

        speed = 5
        for col in range(self.cols):
            if not self.done[col]:
                self.offsets[col] += speed
                if self.offsets[col] >= 100:
                    self.offsets[col] = 0
                    self.scroll_stacks[col].pop(0)
                    self.frame_counters[col] -= 1

                    if self.frame_counters[col] <= 0:
                        self.done[col] = True

        # Если все столбцы завершили анимацию
        if all(self.done):
            self.animating = False

    def get_animating_images(self):
        images = []
        for col in range(self.cols):
            col_images = []
            visible_stack = self.scroll_stacks[col][:self.rows + 1]
            for img in visible_stack:
                # Если img — это путь (str), загружаем и масштабируем
                if isinstance(img, str):
                    scaled_img = pygame.transform.scale(pygame.image.load(img), (100, 100))
                else:
                    # img уже Surface — просто добавляем
                    scaled_img = img
                col_images.append(scaled_img)
            images.append(col_images)
        return images

