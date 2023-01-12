import pygame

import constants
from config import config


def draw_available(display):
    surface = pygame.Surface(config.size)
    surface.set_alpha(50)
    for i in range(config.rows_count):
        for j in range(config.columns_count):
            if config.map[i][j] == 'o':
                pygame.draw.rect(surface, (0, 255, 0, 255),
                                 (j * config.cell_size[0], i * config.cell_size[1], *config.cell_size), 0, 20)
    display.blit(surface, (0, 0))


def draw_information(display, money, money_pos, score, score_pos):
    score = config.font.render(f"Score: {score}", False, (0, 0, 0))
    money = config.font.render(f"Balance: {money}", False, (0, 0, 0))
    money_width = money.get_size()[0]
    score_width = score.get_size()[0]
    display.blit(money, money_pos)
    display.blit(config.font.render("Ⓞ", False, (255, 255, 0)), (money_pos[0] + money_width, money_pos[1]))
    display.blit(score, score_pos)
    display.blit(config.font.render("★", False, (255, 255, 0)), (score_pos[0] + score_width, score_pos[1]))

