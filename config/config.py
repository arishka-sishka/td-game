import configparser
import os


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
    def __init__(self, damage, speed, price, damage_by_level, speed_by_level, price_by_level):
        self.damage = float(damage)
        self.speed = float(speed)
        self.price = float(price)
        self.damage_by_level = float(damage_by_level)
        self.speed_by_level = float(speed_by_level)
        self.price_by_level = float(price_by_level)


class Config:
    def __init__(self, path: str):
        if not os.path.exists(path):
            create_config(path)
        config = configparser.ConfigParser()
        config.read(path)
        self.grey_slime = Slime(**dict(config.items("Grey Slime")))
        self.blue_slime = Slime(**dict(config.items("Blue Slime")))
        self.green_slime = Slime(**dict(config.items("Green Slime")))
        self.purple_slime = Slime(**dict(config.items("Purple Slime")))
        self.red_slime = Slime(**dict(config.items("Red Slime")))
        self.magic_tower = Tower(**dict(config.items("Magic Tower")))
        self.physical_tower = Tower(**dict(config.items("Physical Tower")))
        self.screen_width = int(config.get("Screen", "width"))
        self.screen_height = int(config.get("Screen", "height"))
        self.fps = int(config.get("Screen", "fps"))
        self.rows_count = int(config.get("Screen", "rows"))
        self.columns_count = int(config.get("Screen", "columns"))
        self.cell_size = (round(self.screen_width / self.columns_count), round(self.screen_height / self.rows_count))
