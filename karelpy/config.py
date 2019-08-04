import os

DIMENSION_UNIT = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (185, 185, 185)
FPS = 5
DIRECTION_MAP = {"North": 1, "East": 2, "South": 3, "West": 4}
WORLD_MAP = {1: os.path.join("world", "one.w"),
             2: os.path.join("world", "two.w")}
