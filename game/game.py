import pygame

import constants
import utils
from config import config
from images import images
from .slime import Slime


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode(config.size)
        self.display.set_alpha(205)
        self.clock = pygame.time.Clock()
        self.slimes = pygame.sprite.Group()
        self.slimes.add(Slime(constants.color.red, ((config.start[0] - 1) * config.cell_size[0], config.start[1] * config.cell_size[1])))
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
        utils.draw_information(self.display, 1000, (config.screen_width - 450, 20), 1000,
                               (config.screen_width - 200, 20))
        self.slimes.draw(self.display)
        self.slimes.update()
        obj = self.slimes.sprites()[0]
        pygame.draw.rect(self.display, (0, 0, 0), (config.cell_size[0] * obj.cell[0], config.cell_size[1] * obj.cell[1],
                           *config.cell_size), 2)
        pygame.draw.rect(self.display, (255, 0, 0), obj, 2)
        # отображение доступных мест постройки
        if 0:
            utils.draw_available(self.display)

        pygame.display.update()
