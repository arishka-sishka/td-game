from os import listdir

from pygame import image, transform

import constants
from config import config


def load_image(path):
    sprite = image.load(path)
    return sprite.subsurface((24, 30, 23, 18))


def get_images(path, size=None, crop=False):
    func = load_image if crop else image.load
    if not size:
        return [func(path + "/" + file) for file in listdir(path)]
    return [transform.scale(func(path + "/" + file), size) for file in listdir(path)]


class SlimeImages:
    def __init__(self, path):
        self.walk = get_images(path + "/walk", size=config.slime_size, crop=True)


class Images:
    def __init__(self):
        self.background = transform.scale(image.load("sprites/field/field.png"),
                                          (config.screen_width, config.screen_height))
        self.blue_slime = SlimeImages("sprites/slimes/blue")
        self.green_slime = SlimeImages("sprites/slimes/green")
        self.grey_slime = SlimeImages("sprites/slimes/grey")
        self.purple_slime = SlimeImages("sprites/slimes/purple")
        self.red_slime = SlimeImages("sprites/slimes/red")

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
