from os import listdir

from pygame import image, transform

from config import config


def get_images(path):
    return [image.load(path + "/" + file) for file in listdir(path)]


class SlimeImages:
    def __init__(self, path):
        self.walk = get_images(path + "/walk")


class Images(object):
    background = transform.scale(image.load("sprites/field/field.png"), (config.screen_width, config.screen_height))
    blue_slime = SlimeImages("sprites/slimes/blue")
    green_slime = SlimeImages("sprites/slimes/green")
    grey_slime = SlimeImages("sprites/slimes/grey")
    purple_slime = SlimeImages("sprites/slimes/purple")
    red_slime = SlimeImages("sprites/slimes/red")
    coin = get_images("sprites/coin")
