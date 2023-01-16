from os import listdir

from pygame import image, transform

import constants
from config import config


def load_slime(path):
    sprite = image.load(path)
    return sprite.subsurface((24, 30, 23, 18))


def load_bow(path):
    sprite = image.load(path)
    return sprite.subsurface((100, 100, 300, 280))


def get_images(path, size=None, load=image.load):
    if not size:
        return [load(path + "/" + file) for file in listdir(path)]
    return [transform.scale(load(path + "/" + file), size) for file in listdir(path)]


class SlimeImages:
    def __init__(self, path):
        self.walk = get_images(path + "/walk", size=config.slime_size, load=load_slime)


class Images:
    def __init__(self):
        self.background = transform.scale(image.load("sprites/field/field.png"),
                                          (config.screen_width, config.screen_height))
        self.blue_slime = SlimeImages("sprites/slimes/blue")
        self.green_slime = SlimeImages("sprites/slimes/green")
        self.grey_slime = SlimeImages("sprites/slimes/grey")
        self.purple_slime = SlimeImages("sprites/slimes/purple")
        self.red_slime = SlimeImages("sprites/slimes/red")
        self.book = get_images("sprites/book", size=config.book_size)
        self.bow = get_images("sprites/bow", size=config.bow_size, load=load_bow)
        self.magic_tower = get_images("sprites/tower/magic")
        self.physical_tower = get_images("sprites/tower/physical")
        self.physical_projectile = get_images("sprites/projectile/physical", size=(9, 39))
        self.magic_projectile = get_images("sprites/projectile/magic")
        self.pineapple_heli = get_images("sprites/pineapple/heli", size=(52, 82))
        self.pineapple_float = get_images("sprites/pineapple/float")
        self.pineapple_cry = get_images("sprites/pineapple/cry")
        self.magic_weapon = get_images("sprites/weapon/magic")
        self.physical_weapon = get_images("sprites/weapon/physical", size=(42, 48))

    def __getitem__(self, item):
        match item:
            case constants.color.blue:
                return self.blue_slime
            case constants.color.green:
                return self.green_slime
            case constants.color.grey:
                return self.grey_slime
            case constants.color.purple:
                return self.purple_slime
            case constants.color.red:
                return self.red_slime
            case constants.tower.magic:
                return self.magic_tower
            case constants.tower.physical:
                return self.physical_tower
