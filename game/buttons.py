from itertools import cycle

import pygame

from config import config
from game.tower import MagicTower, PhysicalTower
from images import images
from utils import update_image


class TowerButton(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.cycle = cycle(self.images)
        self.image = self.cycle.__next__()
        self.rect = pygame.Rect(pos + self.image.get_size())
        self.skip = 0

    def update(self, display, choice, *args, **kwargs):
        update_image(self, 3)
        self.draw_text(display)
        self.draw_frame(display, choice)

    def draw_frame(self, display, choice):
        if choice == self:
            pygame.draw.rect(display, (0, 255, 0), self.rect, 5, 10)

    def draw_text(self, surface):
        coin = config.font.render("Ⓞ", False, (255, 255, 0))
        text = config.font.render(str(round(self.price)), False, (0, 0, 0))
        position = self.rect.move((self.rect.w - text.get_width() - coin.get_width()) // 2, self.rect.h)
        surface.blit(text, position[:2])
        surface.blit(coin, position.move(text.get_width(), 0)[:2])


class Book(TowerButton):
    def __init__(self, pos):
        self.images = images.book
        self.price = config.magic_tower.price
        self.tower = MagicTower
        super().__init__(pos)


class Bow(TowerButton):
    def __init__(self, pos):
        self.images = images.bow
        self.price = config.physical_tower.price
        self.tower = PhysicalTower
        super().__init__(pos)
