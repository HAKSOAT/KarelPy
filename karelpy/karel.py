from karelpy.beeper import Beeper
from karelpy import config
import os
import pygame


class Karel(pygame.sprite.Sprite):
    def __init__(self, center, direction):
        pygame.sprite.Sprite.__init__(self)
        base_dir = os.path.abspath(os.path.dirname(__file__))
        karel_path = os.path.join(base_dir, "world", "karel.png")
        self.image = pygame.image.load(karel_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.DIMENSION_UNIT, config.DIMENSION_UNIT))
        self.direction = direction
        self.center = center
        self.amt_beepers_in_bag = 0
        if self.direction == config.DIRECTION_MAP["South"]:
            self.image = pygame.transform.rotate(self.image, -90)
        elif self.direction == config.DIRECTION_MAP["North"]:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.direction == config.DIRECTION_MAP["West"]:
            self.image = pygame.transform.rotate(self.image, -180)
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def move(self, wall_sprites):
        if self.direction == config.DIRECTION_MAP["South"]:
            if self.front_is_clear(wall_sprites):
                self.rect.center = self.rect.center[0], self.rect.center[1] + config.DIMENSION_UNIT
            else:
                raise Exception("There is a wall")
        elif self.direction == config.DIRECTION_MAP["North"]:
            if self.front_is_clear(wall_sprites):
                self.rect.center = self.rect.center[0], self.rect.center[1] - config.DIMENSION_UNIT
            else:
                raise Exception("There is a wall")
        elif self.direction == config.DIRECTION_MAP["West"]:
            if self.front_is_clear(wall_sprites):
                self.rect.center = self.rect.center[0] - config.DIMENSION_UNIT, self.rect.center[1]
            else:
                raise Exception("There is a wall")
        elif self.direction == config.DIRECTION_MAP["East"]:
            if self.front_is_clear(wall_sprites):
                self.rect.center = self.rect.center[0] + config.DIMENSION_UNIT, self.rect.center[1]
            else:
                raise Exception("There is a wall")

    def turn_left(self):
        self.direction = config.DIRECTION_MAP["West"] if self.direction == config.DIRECTION_MAP["North"] else self.direction - 1
        self.image = pygame.transform.rotate(self.image, 90)

    def pick_beeper(self, beeper_sprites):
        beepers = pygame.sprite.spritecollide(self, beeper_sprites, False)
        if len(beepers) == 0:
            raise Exception("Beeper doesn't exist here")
        beepers[0].kill()
        self.amt_beepers_in_bag += 1

    def put_beeper(self, beeper_sprites):
        if self.beepers_in_bag == 0:
            raise Exception("No Beeper in the bag")
        for beeper in range(0, self.amt_beepers_in_bag):
            center = self.rect.center
            beeper_sprites.add(Beeper(center))
            self.beepers_in_bag -= 1
            break

    def __absolute_south_clear(self, wall_sprites):
        next_wall_center = self.rect.center[0], self.rect.center[1] + config.DIMENSION_UNIT // 2
        for wall in wall_sprites.sprites():
            if next_wall_center[0] == wall.rect.center[0] and next_wall_center[1] == wall.rect.center[1]:
                return False
        return True

    def __absolute_north_clear(self, wall_sprites):
        next_wall_center = self.rect.center[0], self.rect.center[1] - config.DIMENSION_UNIT // 2
        for wall in wall_sprites.sprites():
            if next_wall_center[0] == wall.rect.center[0] and next_wall_center[1] == wall.rect.center[1]:
                return False
        return True

    def __absolute_west_clear(self, wall_sprites):
        next_wall_center = self.rect.center[0] - config.DIMENSION_UNIT // 2, self.rect.center[1]
        for wall in wall_sprites.sprites():
            if next_wall_center[0] == wall.rect.center[0] and next_wall_center[1] == wall.rect.center[1]:
                return False
        return True

    def __absolute_east_clear(self, wall_sprites):
        next_wall_center = self.rect.center[0] + config.DIMENSION_UNIT // 2, self.rect.center[1]
        for wall in wall_sprites.sprites():
            if next_wall_center[0] == wall.rect.center[0] and next_wall_center[1] == wall.rect.center[1]:
                return False
        return True

    def front_is_clear(self, wall_sprites):
        if self.direction == config.DIRECTION_MAP["South"]:
            return self.__absolute_south_clear(wall_sprites)
        elif self.direction == config.DIRECTION_MAP["North"]:
            return self.__absolute_north_clear(wall_sprites)
        elif self.direction == config.DIRECTION_MAP["West"]:
            return self.__absolute_west_clear(wall_sprites)
        elif self.direction == config.DIRECTION_MAP["East"]:
            return self.__absolute_east_clear(wall_sprites)

    def beepers_present(self, beeper_sprites):
        col = pygame.sprite.spritecollide(self, beeper_sprites, False)
        if col:
            return True
        return False

    def beepers_in_bag(self):
        return True if self.amt_beepers_in_bag > 0 else False

    def facing_north(self):
        return True if self.direction == config.DIRECTION_MAP["North"] else False

    def facing_south(self):
        return True if self.direction == config.DIRECTION_MAP["South"] else False

    def facing_east(self):
        return True if self.direction == config.DIRECTION_MAP["East"] else False

    def facing_west(self):
        return True if self.direction == config.DIRECTION_MAP["West"] else False
