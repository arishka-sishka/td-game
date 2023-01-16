import sys

import pygame

import data
from config import config


def draw_available(display, points):
    surface = pygame.Surface(config.size)
    surface.set_alpha(50)
    for point in points:
        pygame.draw.rect(surface, (0, 255, 0, 255), point, 0, 20)
    display.blit(surface, (0, 0))


def draw_information(display, money_pos, score_pos):
    score = config.font.render(f"Score: {data.score}", False, (0, 0, 0))
    money = config.font.render(f"Balance: {data.money}", False, (0, 0, 0))
    money_width = money.get_size()[0]
    score_width = score.get_size()[0]
    star = config.font.render("★", False, (255, 255, 0))
    coin = config.font.render("Ⓞ", False, (255, 255, 0))
    display.blit(money, money_pos)
    display.blit(coin, (money_pos[0] + money_width, money_pos[1]))
    display.blit(score, score_pos)
    display.blit(star, (score_pos[0] + score_width, score_pos[1]))


def update_image(obj, speed):
    if obj.skip == speed:
        obj.image = obj.cycle.__next__()
        obj.skip = 0
    obj.skip += 1

def terminate():
    pygame.quit()
    sys.exit()
