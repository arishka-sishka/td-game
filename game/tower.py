from copy import copy

import pygame

from config import config
from game.projectiles import PhysicalProjectile, MagicProjectile
from images import images


class Tower(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.base = pos
        self.level = 0
        self.radius = 300
        self.rect = pygame.Rect((self.base[0], self.base[1] - self.image.get_height() + 64) + self.image.get_size())
        self.reload = 0

    @property
    def image(self):
        return self.images[self.level]

    def update(self, display, slimes, projectile, *args, **kwargs):
        target = pygame.sprite.spritecollideany(self, slimes, collided=pygame.sprite.collide_circle)
        if target and self.reload == 0 and target.alive():
            projectile.add(self.projectile(self.rect.midtop, target, self.stats.damage))
            self.reload = self.stats.reload

        if self.reload > 0:
            self.reload -= 1


class MagicTower(Tower):
    def __init__(self, pos):
        self.images = images.magic_tower
        self.stats = copy(config.magic_tower)
        self.projectile = MagicProjectile
        super().__init__(pos)

    @property
    def image(self):
        img = self.images[self.level]
        img.blit(images.magic_weapon[0], (20, 10))
        return img

class PhysicalTower(Tower):
    def __init__(self, pos):
        self.images = images.physical_tower
        self.stats = copy(config.magic_tower)
        self.projectile = PhysicalProjectile
        super().__init__(pos)

    @property
    def image(self):
        img = self.images[self.level]
        img.blit(images.physical_weapon[0], (10, 0))
        return img


