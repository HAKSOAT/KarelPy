import pygame

DIMENSION_UNIT = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (185, 185, 185)
FPS = 5
DIRECTION_MAP = {"North": 1, "East": 2, "South": 3, "West": 4}


class Dot(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        width = DIMENSION_UNIT / 10
        height = DIMENSION_UNIT / 10
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center


class Beeper(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("beezer.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (DIMENSION_UNIT//2, DIMENSION_UNIT//2))
        self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.rect.center = center


class Karel(pygame.sprite.Sprite):
    def __init__(self, center, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("karel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (DIMENSION_UNIT, DIMENSION_UNIT))
        self.direction = direction
        self.center = center
        self.beeper_bag = 0
        if self.direction == DIRECTION_MAP["South"]:
            self.image = pygame.transform.rotate(self.image, -90)
        elif self.direction == DIRECTION_MAP["North"]:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.direction == DIRECTION_MAP["West"]:
            self.image = pygame.transform.rotate(self.image, -180)
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def move(self):
        if self.direction == DIRECTION_MAP["South"]:
            self.rect.center = self.rect.center[0], self.rect.center[1] + DIMENSION_UNIT
        elif self.direction == DIRECTION_MAP["North"]:
            self.rect.center = self.rect.center[0], self.rect.center[1] - DIMENSION_UNIT
        elif self.direction == DIRECTION_MAP["West"]:
            self.rect.center = self.rect.center[0] - DIMENSION_UNIT, self.rect.center[1]
        elif self.direction == DIRECTION_MAP["East"]:
            self.rect.center = self.rect.center[0] + DIMENSION_UNIT, self.rect.center[1]

    def turn_left(self):
        self.direction = self.direction - 1 if self.direction > DIRECTION_MAP["North"] else DIRECTION_MAP["West"]
        self.image = pygame.transform.rotate(self.image, 90)

    def turn_right(self):
        self.direction = self.direction + 1 if self.direction < DIRECTION_MAP["West"] else DIRECTION_MAP["North"]
        self.image = pygame.transform.rotate(self.image, -90)

    def pick_beeper(self, beeper_sprites):
        beepers = pygame.sprite.spritecollide(self, beeper_sprites, False)
        self.beeper_bag += 1
        beepers[0].kill()

    def put_beeper(self, beeper_sprites):
        for beeper in range(0, self.beeper_bag):
            center = self.rect.center
            beeper_sprites.add(Beeper(center))
            # Should raise a no beeper in the bag error
            self.beeper_bag -= 1
            break

    def __absolute_south_clear(self, wall_sprites):
        next_center = self.rect.center[0], self.rect.center[1] + DIMENSION_UNIT
        for wall in wall_sprites.sprites():
            if next_center[1] == wall.rect.center[1]:
                return False
        return True

    def __absolute_north_clear(self, wall_sprites):
        next_center = self.rect.center[0], self.rect.center[1] - DIMENSION_UNIT
        for wall in wall_sprites.sprites():
            if next_center[1] == wall.rect.center[1]:
                return False
        return True

    def __absolute_west_clear(self, wall_sprites):
        next_center = self.rect.center[0] - DIMENSION_UNIT, self.rect.center[1]
        for wall in wall_sprites.sprites():
            if next_center[0] == wall.rect.center[0]:
                return False
        return True

    def __absolute_east_clear(self, wall_sprites):
        next_center = self.rect.center[0] + DIMENSION_UNIT, self.rect.center[1]
        for wall in wall_sprites.sprites():
            if next_center[0] == wall.rect.center[0]:
                return False
        return True

    def front_is_clear(self, wall_sprites):
        if self.direction == DIRECTION_MAP["South"]:
            return self.__absolute_south_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["North"]:
            return self.__absolute_north_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["West"]:
            return self.__absolute_west_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["East"]:
            return self.__absolute_east_clear(wall_sprites)

    def right_is_clear(self, wall_sprites):
        if self.direction == DIRECTION_MAP["East"]:
            return self.__absolute_south_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["West"]:
            return self.__absolute_north_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["South"]:
            return self.__absolute_west_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["North"]:
            return self.__absolute_east_clear(wall_sprites)

    def left_is_clear(self, wall_sprites):
        if self.direction == DIRECTION_MAP["West"]:
            return self.__absolute_south_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["East"]:
            return self.__absolute_north_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["North"]:
            return self.__absolute_west_clear(wall_sprites)
        elif self.direction == DIRECTION_MAP["South"]:
            return self.__absolute_east_clear(wall_sprites)

    def beepers_present(self, beeper_sprites):
        col = pygame.sprite.spritecollide(self, beeper_sprites, False)
        if col:
            return True
        return False

    def facing_north(self):
        return True if self.direction == DIRECTION_MAP["North"] else False

    def facing_south(self):
        return True if self.direction == DIRECTION_MAP["South"] else False

    def facing_east(self):
        return True if self.direction == DIRECTION_MAP["East"] else False

    def facing_west(self):
        return True if self.direction == DIRECTION_MAP["West"] else False


class Wall(pygame.sprite.Sprite):
    def __init__(self, center, orientation):
        pygame.sprite.Sprite.__init__(self)
        if orientation == "v":
            self.image = pygame.Surface((1, DIMENSION_UNIT))
        elif orientation == "h":
            self.image = pygame.Surface((DIMENSION_UNIT, 1))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center


class WorldMaker:
    def __init__(self, template):
        self.template = template
        self.dimension = (0, 0)
        self.beeper = {}
        self.karel = {}
        self.beeper_bag = None
        self.wall = {}
        self.speed = 1.00

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
                x = int(command[1]) * DIMENSION_UNIT
                y = int(command[2]) * DIMENSION_UNIT
                self.dimension = (x, y)
            elif command[0] == "Beeper":
                x = int(command[1]) * DIMENSION_UNIT
                y = int(command[2]) * DIMENSION_UNIT
                quantity = int(command[3])
                self.beeper[(x, y)] = self.beeper.get((x, y), 0) + quantity
            elif command[0] == "BeeperBag":
                quantity = command[1]
                if quantity == "INFINITE":
                    self.beeper_bag = float("inf")
                else:
                    self.beeper_bag = int(quantity)
            elif command[0] == "Wall":
                x = int(command[1]) * DIMENSION_UNIT
                y = int(command[2]) * DIMENSION_UNIT
                direction = DIRECTION_MAP[command[3]]
                self.wall[(x, y)] = self.wall.get((x, y), []) + [direction]
            elif command[0] == "Karel":
                x = int(command[1]) * DIMENSION_UNIT
                y = int(command[2]) * DIMENSION_UNIT
                direction = DIRECTION_MAP[command[3]]
                self.karel[(x, y)] = direction
            elif command[0] == "Speed":
                self.speed = float(command[1])

    def create_world(self):
        pygame.init()
        pygame.mixer.init()
        width = self.dimension[0]
        height = self.dimension[1]
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Karel Learns Python")
        clock = pygame.time.Clock()

        beeper_sprites = pygame.sprite.Group()
        dot_sprites = pygame.sprite.Group()
        wall_sprites = pygame.sprite.Group()
        karel_sprite = pygame.sprite.Group()
        for location, quantity in self.beeper.items():
            for beeper in range(quantity):
                x = location[0] - DIMENSION_UNIT/2
                y = self.dimension[1] - (location[1] - DIMENSION_UNIT/2)
                center = x, y
                beeper_sprites.add(Beeper(center))

        x_axis = self.dimension[0] // DIMENSION_UNIT + 1
        y_axis = self.dimension[1] // DIMENSION_UNIT + 1
        for horizontal in range(x_axis):
            for vertical in range(y_axis):
                x = horizontal * DIMENSION_UNIT - DIMENSION_UNIT / 2
                y = self.dimension[1] - (vertical * DIMENSION_UNIT - DIMENSION_UNIT / 2)
                center = x, y
                dot_sprites.add(Dot(center))

        for location, direction in self.karel.items():
            x = location[0] - DIMENSION_UNIT/2
            y = self.dimension[1] - (location[1] - DIMENSION_UNIT/2)
            center = x, y
            karel_sprite.add(Karel(center, direction))

        for location, directions in self.wall.items():
            for direction in directions:
                if direction == DIRECTION_MAP["North"]:
                    x = location[0] - DIMENSION_UNIT / 2
                    y = self.dimension[1] - location[1]
                    orientation = "h"
                elif direction == DIRECTION_MAP["South"]:
                    x = location[0] - DIMENSION_UNIT / 2
                    y = self.dimension[1] - (location[1] - DIMENSION_UNIT)
                    orientation = "h"
                elif direction == DIRECTION_MAP["East"]:
                    x = location[0]
                    y = self.dimension[1] - (location[1] - DIMENSION_UNIT / 2)
                    orientation = "v"
                elif direction == DIRECTION_MAP["West"]:
                    x = location[0] - DIMENSION_UNIT
                    y = self.dimension[1] - (location[1] - DIMENSION_UNIT / 2)
                    orientation = "v"
                center = x, y
                wall_sprites.add(Wall(center, orientation))

        #karel_sprite.sprites()[0].pick_beeper(beeper_sprites)
        #karel_sprite.sprites()[0].pick_beeper(beeper_sprites)
        # karel_sprite.sprites()[0].
        # running = True
        karels = karel_sprite.sprites()[0]
        moves = [karels.turn_left, karels.move, karels.move, karels.move, karels.pick_beeper,
                 karels.move, karels.pick_beeper, karels.turn_right,
                 karels.move, karels.move, karels.move, karels.move, karels.turn_right,
                 karels.move, karels.pick_beeper, karels.move, karels.move, karels.pick_beeper,
                 karels.move, karels.pick_beeper]
        for move in moves:
            clock.tick(FPS * self.speed)
            try:
                move()
            except:
                move(beeper_sprites)
            dot_sprites.update()
            wall_sprites.update()
            karel_sprite.update()
            beeper_sprites.update()
            # keep loop running at the right speed

            # Process input (events)
            # for event in pygame.event.get():
            #     # check for closing window
            #     if event.type == pygame.QUIT:
            #         running = False

            # Draw / render
            screen.fill(WHITE)
            wall_sprites.draw(screen)
            dot_sprites.draw(screen)
            beeper_sprites.draw(screen)
            karel_sprite.draw(screen)
            # *after* drawing everything, flip the display
            pygame.display.flip()
            pygame.display.set_mode(flags=pygame.RESIZABLE)

        pygame.quit()


world = WorldMaker("world/unitednations.w")
world.parse_template()
world.create_world()









