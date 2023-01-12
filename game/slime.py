from itertools import cycle

import pygame

from config import config
from images import images


class Slime(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()
        self.walk_cycle = cycle(images[color].walk)
        self.pos = list(pos)
        self.stats = config[color]
        self.image = self.walk_cycle.__next__()
        self.size = list(self.image.get_size())
        self.bounding = self.image.get_bounding_rect()
        self.rect = pygame.Rect(*(self.pos + self.size))
        self.skip = True
        self.cell = list(config.start)
        self.colided = False

    @property
    def vx(self):
        return self.x * self.stats.speed

    @property
    def vy(self):
        return self.y * self.stats.speed

    @property
    def x(self):
        data = config.map[self.cell[1]][self.cell[0]]
        if data == "]":
            self.rect = self.rect.move(0, -2)
            return 1
        if data == "[":
            self.rect = self.rect.move(0, 2)
            return 1
        if data == ">" or data == "s":
            return 1
        if data == "<":
            return -1
        if data == "e":
            return 1
        return 0

    @property
    def y(self):
        data = config.map[self.cell[1]][self.cell[0]]
        if data == "^":
            return -1
        if data == "_":
            return 1
        return 0

    def update(self, *args, **kwargs):
        self.skip = not self.skip
        if self.skip:
            self.image = self.walk_cycle.__next__()
            if self.x == -1:
                self.image = pygame.transform.flip(self.image, 1, 0)

        self.rect = self.rect.move(self.vx, self.vy)

        if not pygame.Rect(config.cell_size[0] * self.cell[0], config.cell_size[1] * self.cell[1],
                           *config.cell_size).colliderect(self.rect):
            if self.colided:
                self.cell[0] += self.x
                self.cell[1] += self.y
                self.colided = False
        else:
            if not self.colided:
                self.colided = True
