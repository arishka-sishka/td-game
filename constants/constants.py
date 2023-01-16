import pygame.event


class Color(object):
    blue = 1
    green = 2
    grey = 3
    purple = 4
    red = 5
    colors = [1, 2, 3, 4, 5]


class Tower(object):
    magic = 6
    physical = 7


end_event = pygame.USEREVENT + 1
