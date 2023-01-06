from os import listdir

from pygame import image, transform

from config import config


def get_slime_images(path):
    return [image.load(path + "/walk/" + file) for file in (listdir(path + "/walk"))]


class SlimeImages:
    def __init__(self, path):
        self.walk = get_slime_images(path)


class Images(object):
    background = transform.scale(image.load("sprites/field/field.png"), (config.screen_width, config.screen_height))
    blue_slime = SlimeImages("sprites/slimes/blue")
    green_slime = SlimeImages("sprites/slimes/green")
    grey_slime = SlimeImages("sprites/slimes/grey")
    purple_slime = SlimeImages("sprites/slimes/purple")
    red_slime = SlimeImages("sprites/slimes/red")
