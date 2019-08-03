from beeper import Beeper
from dot import Dot
from karel import Karel
from ikarel import KarelInterface
from wall import Wall
import config
import pygame


class World:
    def __init__(self, template):
        self.template = template
        self.dimension = (0, 0)
        self.beeper = {}
        self.karel = {}
        self.beeper_bag = None
        self.wall = {}
        self.speed = 1.00
        self.real_karel = None

    def parse_template(self):
        with open(self.template, "r") as template:
            raw_commands = template.readlines()
        parsed_commands = []
        for command in raw_commands:
            bad_characters = [":", "\n", "(", ")", ","]
            command = "".join(char for char in command if char not in bad_characters)
            parsed_commands.append(command.split(" "))
        for command in parsed_commands:
            if command[0] == "Dimension":
                x = int(command[1]) * config.DIMENSION_UNIT
                y = int(command[2]) * config.DIMENSION_UNIT
                self.dimension = (x, y)
            elif command[0] == "Beeper":
                x = int(command[1]) * config.DIMENSION_UNIT
                y = int(command[2]) * config.DIMENSION_UNIT
                quantity = int(command[3])
                self.beeper[(x, y)] = self.beeper.get((x, y), 0) + quantity
            elif command[0] == "BeeperBag":
                quantity = command[1]
                if quantity == "INFINITE":
                    self.beeper_bag = float("inf")
                else:
                    self.beeper_bag = int(quantity)
            elif command[0] == "Wall":
                x = int(command[1]) * config.DIMENSION_UNIT
                y = int(command[2]) * config.DIMENSION_UNIT
                direction = config.DIRECTION_MAP[command[3]]
                self.wall[(x, y)] = self.wall.get((x, y), []) + [direction]
            elif command[0] == "Karel":
                x = int(command[1]) * config.DIMENSION_UNIT
                y = int(command[2]) * config.DIMENSION_UNIT
                direction = config.DIRECTION_MAP[command[3]]
                self.karel[(x, y)] = direction
            elif command[0] == "Speed":
                self.speed = float(command[1])

    def create(self):
        pygame.init()
        pygame.mixer.init()
        width = self.dimension[0]
        height = self.dimension[1]
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Karel Learns Python")

        beeper_sprites = pygame.sprite.Group()
        dot_sprites = pygame.sprite.Group()
        wall_sprites = pygame.sprite.Group()
        karel_sprite = pygame.sprite.Group()
        for location, quantity in self.beeper.items():
            for beeper in range(quantity):
                x = location[0] - config.DIMENSION_UNIT/2
                y = self.dimension[1] - (location[1] - config.DIMENSION_UNIT/2)
                center = x, y
                beeper_sprites.add(Beeper(center))

        x_axis = self.dimension[0] // config.DIMENSION_UNIT + 1
        y_axis = self.dimension[1] // config.DIMENSION_UNIT + 1
        for horizontal in range(x_axis):
            for vertical in range(y_axis):
                x = horizontal * config.DIMENSION_UNIT - config.DIMENSION_UNIT / 2
                y = self.dimension[1] - (vertical * config.DIMENSION_UNIT - config.DIMENSION_UNIT / 2)
                center = x, y
                dot_sprites.add(Dot(center))

        for location, direction in self.karel.items():
            x = location[0] - config.DIMENSION_UNIT/2
            y = self.dimension[1] - (location[1] - config.DIMENSION_UNIT/2)
            center = x, y
            karel_sprite.add(Karel(center, direction))

        for location, directions in self.wall.items():
            for direction in directions:
                if direction == config.DIRECTION_MAP["North"]:
                    x = location[0] - config.DIMENSION_UNIT / 2
                    y = self.dimension[1] - location[1]
                    orientation = "h"
                elif direction == config.DIRECTION_MAP["South"]:
                    x = location[0] - config.DIMENSION_UNIT / 2
                    y = self.dimension[1] - (location[1] - config.DIMENSION_UNIT)
                    orientation = "h"
                elif direction == config.DIRECTION_MAP["East"]:
                    x = location[0]
                    y = self.dimension[1] - (location[1] - config.DIMENSION_UNIT / 2)
                    orientation = "v"
                elif direction == config.DIRECTION_MAP["West"]:
                    x = location[0] - config.DIMENSION_UNIT
                    y = self.dimension[1] - (location[1] - config.DIMENSION_UNIT / 2)
                    orientation = "v"
                center = x, y
                wall_sprites.add(Wall(center, orientation))
        self.real_karel = KarelInterface(karel_sprite, beeper_sprites, wall_sprites,
                                         dot_sprites, screen, self.speed)
        # self.close()

    # def close(self):
    #     pygame.display.set_mode(flags=pygame.RESIZABLE)
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False


world = World("world/unitednations.w")
world.parse_template()
world.create()
real_karel = world.real_karel










