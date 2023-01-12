import pygame.font

from .config import Config

pygame.font.init()
config = Config("config.cfg", "map.txt", "fonts/Arbata Compact Mac.ttf")
