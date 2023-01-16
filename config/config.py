import configparser
import os

import pygame.font

import constants
import data


def load_map(path):
    tower_points = []
    arr = []
    with open(path, "r") as file:
        for count_y, line in enumerate(file.readlines()):
            lst = []
            if "s" in line:
                start = (0, count_y)
            if "e" in line:
                end = (len(line.strip()) - 1, count_y)
            for count_x, symbol in enumerate(line.strip()):
                lst.append(symbol)
                if symbol == "o":
                    tower_points.append((count_x, count_y))
            arr.append(lst)
    return arr, start, end, tower_points


def create_config(path):
    config = configparser.ConfigParser()
    config.read_dict({'Grey Slime': {'hp': '100', 'speed': '1', 'magic': '0', 'physical': '0'},
                      'Blue Slime': {'hp': '75', 'speed': '1.5', 'magic': '0', 'physical': '0'},
                      'Green Slime': {'hp': '100', 'speed': '1', 'magic': '0.5', 'physical': '0'},
                      'Purple Slime': {'hp': '200', 'speed': '0.75', 'magic': '0', 'physical': '0'},
                      'Red Slime': {'hp': '100', 'speed': '1', 'magic': '0', 'physical': '0.5'},
                      'Projectile': {'speed': '30'},
                      'Physical Tower': {'damage': '10', 'speed': '1000', 'damage_by_level': '2',
                                         'speed_by_level': '0.8', 'price': '50', 'price_by_level': '100'},
                      'Magic Tower': {'damage': '10', 'speed': '1000', 'damage_by_level': '2',
                                      'speed_by_level': '0.8', 'price': '50', 'price_by_level': '100'}})
    with open(path, "w") as config_file:
        config.write(config_file)


class Slime:
    def __init__(self, hp, speed, magic, physical):
        self.hp = float(hp)
        self.speed = float(speed)
        self.magic = float(magic)
        self.physical = float(physical)


class Tower:
    def __init__(self, fps, damage, reload, price):
        self.damage = float(damage)
        self.reload = round(fps * float(reload))
        self.price = int(price)


class BaseConfig:
    def __init__(self, config_path: str, map_path: str, font_path: str):
        if not os.path.exists(config_path):
            create_config(config_path)
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        # init screen
        self.screen_width = int(self.config.get("Screen", "width"))
        self.screen_height = int(self.config.get("Screen", "height"))
        self.size = self.screen_width, self.screen_height
        self.fps = int(self.config.get("Screen", "fps"))
        self.rows_count = int(self.config.get("Screen", "rows"))
        self.columns_count = int(self.config.get("Screen", "columns"))
        self.cell_size = (round(self.screen_width / self.columns_count), round(self.screen_height / self.rows_count))
        # init slimes
        self.grey_slime = Slime(**dict(self.config.items("Grey Slime")))
        self.blue_slime = Slime(**dict(self.config.items("Blue Slime")))
        self.green_slime = Slime(**dict(self.config.items("Green Slime")))
        self.purple_slime = Slime(**dict(self.config.items("Purple Slime")))
        self.red_slime = Slime(**dict(self.config.items("Red Slime")))
        self.slime_size = (int(self.config.get("Slime", "size")),) * 2
        # init towers
        self.magic_tower = Tower(self.fps, **dict(self.config.items("Magic Tower")))
        self.physical_tower = Tower(self.fps, **dict(self.config.items("Physical Tower")))
        # init font
        self.font_size = int(self.config.get("Screen", "font_size"))
        self.font = pygame.font.Font(font_path, self.font_size)
        # init map
        self.map, self.start, self.end, self.tower_points = load_map(map_path)
        # init book
        self.book_size = (int(self.config.get("Book", "size")),) * 2
        # init bow
        self.bow_size = (int(self.config.get("Bow", "size")),) * 2

        self.start_money = int(self.config.get("Game", "start_money"))
        self.reward = int(self.config.get("Slime", "reward"))
        self.difficulty = int(self.config.get("Game", "difficulty"))



class Config(BaseConfig):
    def __init__(self, config_path: str, map_path: str, font_path: str):
        self.config_path = config_path
        self.map_path = map_path
        super().__init__(config_path, map_path, font_path)

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

    def update(self):
        super().__init__(self.config_path, self.map_path)

    def write_score(self):
        self.config.set("Game", "record", str(data.score))
        with open(self.config_path, "w") as config_file:
            self.config.write(config_file)
