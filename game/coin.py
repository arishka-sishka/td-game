from itertools import cycle

import pygame

from images import images


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.skip = True
        self.cycle = cycle(images.coin)
        # TODO: монетка сильно быстрая
        self.image = self.cycle.__next__()
        self.rect = pos + self.image.get_size()

    def update(self, *args, **kwargs):
        self.image = self.cycle.__next__()
