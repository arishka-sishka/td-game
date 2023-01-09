import pygame

from config import config


def draw_available(display):
    surface = pygame.Surface(config.size)
    surface.set_alpha(50)
    for i in range(config.rows_count):
        for j in range(config.columns_count):
            if config.map[i][j] == 'o':
                pygame.draw.rect(surface, (0, 255, 0, 255), (j * config.cell_size[0], i * config.cell_size[1], *config.cell_size), 0, 20)
    display.blit(surface, (0, 0))
