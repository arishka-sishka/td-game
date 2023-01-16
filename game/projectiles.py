from itertools import cycle
from math import atan2, pi

import pygame

from images import images
from utils import update_image


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, target, damage):
        super().__init__()
        self.target = target
        self.damage = damage
        target_x, target_y = self.target.rect.center
        x, y = pos
        angle = 180 + int((180 / pi) * atan2(target_x - x, target_y - y))
        images = list(map(lambda x: pygame.transform.rotate(x, angle), self.images))
        self.cycle = cycle(images)
        self.image = self.cycle.__next__()
        self.rect = pygame.Rect(pos + self.image.get_size())
        self.skip = 0

    def move_to_target(self):
        target_x, target_y = self.target.rect.center
        x, y = self.rect.center
        coords = [target_x - x, target_y - y]
        coords = list(map(lambda x: (x / abs(max(coords, key=lambda x: abs(x)))) * 10, coords))
        self.rect = self.rect.move(*coords)

    def hit_target(self):
        if pygame.sprite.collide_mask(self, self.target):
            self.target.hit(self.damage, self.type)
            self.kill()

    def update(self, *args, **kwargs):
        update_image(self, 2)
        self.move_to_target()
        self.hit_target()


class PhysicalProjectile(Projectile):
    def __init__(self, pos, target, damage):
        self.type = "physical"
        self.images = images.physical_projectile
        super().__init__(pos, target, damage)


class MagicProjectile(Projectile):
    def __init__(self, pos, target, damage):
        self.type = "magic"
        self.images = images.magic_projectile
        super().__init__(pos, target, damage)
