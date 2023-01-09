import pygame

import utils
from config import config
from game.coin import Coin
from images import images


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode(config.size)
        self.display.set_alpha(205)
        self.clock = pygame.time.Clock()
        self.run = True
        self.score = 0
        self.coin = pygame.sprite.GroupSingle(Coin((20, 20)))

    def play(self):
        while self.run:
            self.clock.tick(config.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.draw_window()

    def draw_window(self):
        self.display.blit(images.background, (0, 0))
        self.coin.draw(self.display)
        self.coin.update()
        # отображение доступных мест постройки
        if 1:
            utils.draw_available(self.display)

        pygame.display.update()
