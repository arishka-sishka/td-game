from itertools import cycle
from random import choice

import pygame

import constants
import data
import utils
from config import config
from images import images
from .buttons import Bow, Book
from .pineapple import Pineapple
from .slime import Slime


class Game:
    def __init__(self):
        self.display = pygame.display.set_mode(config.size)
        self.display.set_alpha(205)
        self.clock = pygame.time.Clock()
        self.slimes = pygame.sprite.Group()
        book = pygame.sprite.GroupSingle(
            Book((config.screen_width - (50 + config.book_size[0]), config.screen_height - (50 + config.book_size[0]))))
        bow = pygame.sprite.GroupSingle(
            Bow((config.screen_width - (100 + config.bow_size[0] + config.book_size[0]),
                 config.screen_height - (50 + config.bow_size[0]))))
        self.buttons = pygame.sprite.Group(book, bow)
        self.towers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.pineapple = pygame.sprite.GroupSingle(
            Pineapple((config.end[0] * config.cell_size[0], config.end[1] * config.cell_size[1] - 20)))
        self.tick = 0

    def end_screen(self):
        img_cycle = cycle(images.pineapple_cry)
        skip = 3
        while True:
            if skip == 3:
                img = img_cycle.__next__()
                skip = 0
            rect = img.get_rect()
            self.display.fill((255, 255, 255))
            text = config.font.render(f"Score: {data.score}", False, (0, 0, 0))
            text = pygame.transform.scale(text, (text.get_width() * 2, text.get_height() * 2))
            position = [(config.screen_width - text.get_width()) // 2,
                        (config.screen_height - text.get_height()) // 5 * 3]
            self.display.blit(text, position)
            text = config.font.render("press any key", False, (0, 0, 0))
            text = pygame.transform.scale(text, (text.get_width() * 2, text.get_height() * 2))
            position[1] += text.get_height()
            position[0] = (config.screen_width - text.get_width()) // 2
            self.display.blit(text, position)
            self.display.blit(img, ((config.screen_width - rect.w) // 2, position[1] - rect.h - 50 - text.get_height()))
            skip += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    utils.terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.update()
            self.clock.tick(config.fps)

    def start_screen(self):
        img_cycle = cycle(images.pineapple_float)
        skip = 3
        while True:
            if skip == 3:
                img = img_cycle.__next__()
                skip = 0
            rect = img.get_rect()
            self.display.fill((255, 255, 255))
            text = config.font.render("Start Game", False, (0, 0, 0))
            text = pygame.transform.scale(text, (text.get_width() * 2, text.get_height() * 2))
            position = [(config.screen_width - text.get_width()) // 2,
                        (config.screen_height - text.get_height()) // 5 * 3]
            self.display.blit(text, position)
            text = config.font.render("press any key", False, (0, 0, 0))
            text = pygame.transform.scale(text, (text.get_width() * 2, text.get_height() * 2))
            position[1] += text.get_height()
            position[0] = (config.screen_width - text.get_width()) // 2
            self.display.blit(text, position)
            self.display.blit(img, ((config.screen_width - rect.w) // 2, position[1] - rect.h - 50 - text.get_height()))
            skip += 1
            self.tick = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    utils.terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.new_game()
                    config.write_score()
                    return
            pygame.display.update()
            self.clock.tick(config.fps)

    @property
    def k(self):
        return config.difficulty / (data.score + 1)

    def play(self):
        self.new_game()
        self.start_screen()
        while True:
            self.game_loop()

    def game_loop(self):
        run = True
        while run:
            if self.tick >= round(config.fps * self.k):
                self.spawn_slime()
                self.tick = 0
            self.tick += 1
            self.clock.tick(config.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    utils.terminate()

                if event.type == constants.constants.end_event:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    point_rect = pygame.Rect(event.pos + (1, 1))
                    if self.choice:
                        if (tower := point_rect.collidelist(self.points)) != -1 and self.choice.price <= data.money:
                            self.towers.add(self.choice.tower(self.points[tower].topleft))
                            data.money -= int(self.choice.price)
                            self.points.pop(tower)
                    choice = point_rect.collidelist(self.buttons.sprites())
                    if choice == 1 and self.choice != self.buttons.sprites()[1]:
                        self.choice = self.buttons.sprites()[1]
                    elif choice == 0 and self.choice != self.buttons.sprites()[0]:
                        self.choice = self.buttons.sprites()[0]
                    else:
                        self.choice = None

            self.draw_window()
        self.end_screen()
        self.new_game()

    def draw_window(self):
        self.display.blit(images.background, (0, 0))
        utils.draw_information(self.display, (config.screen_width - 450, 20),
                               (config.screen_width - 200, 20))
        self.slimes.draw(self.display)
        self.buttons.draw(self.display)
        self.towers.draw(self.display)
        self.pineapple.draw(self.display)
        self.projectiles.draw(self.display)
        self.towers.update(self.display, self.slimes, self.projectiles)
        self.slimes.update()
        self.projectiles.update()
        self.buttons.update(self.display, self.choice)
        self.pineapple.update(self.slimes)

        if self.choice:
            utils.draw_available(self.display, self.points)

        pygame.display.update()

    def spawn_slime(self):
        self.slimes.add(Slime(choice(list(constants.color.colors)),
                              ((config.start[0] - 0.5) * config.cell_size[0], config.start[1] * config.cell_size[1])))

    def new_game(self):
        self.choice = None
        self.points = list(map(lambda tuple: pygame.Rect(tuple[0] * config.cell_size[0], tuple[1] * config.cell_size[1],
                                                         *config.cell_size), config.tower_points))
        self.slimes.empty()
        self.towers.empty()
        self.projectiles.empty()
        data.score = 0
        data.money = config.start_money
