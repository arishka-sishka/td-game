from itertools import cycle

import pygame

import constants
from images import images
from utils import update_image


class Pineapple(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.cycle = cycle(images.pineapple_heli)
        self.image = self.cycle.__next__()
        self.rect = pygame.Rect(pos + self.image.get_size())
        self.skip = 0

    def update(self, slimes):
        if pygame.sprite.spritecollideany(self, slimes):
            pygame.event.post(pygame.event.Event(constants.constants.end_event))
        update_image(self, 2)