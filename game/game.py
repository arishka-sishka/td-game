import pygame

from config import config
from images import images


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((config.screen_width, config.screen_height))
        self.clock = pygame.time.Clock()
        self.run = True
        self.score = 0

    def play(self):
        while self.run:
            self.clock.tick(config.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.draw_window()

    def draw_window(self):
        self.display.blit(images.background, (0, 0))
        for i in range(config.rows_count):
            for j in range(config.columns_count):
                pygame.draw.rect(self.display, "#000000", (j * config.cell_size[0], i * config.cell_size[1], config.cell_size[0], config.cell_size[1]), 1)
        pygame.display.update()
