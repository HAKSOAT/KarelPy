from karelpy import config
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, center, orientation):
        pygame.sprite.Sprite.__init__(self)
        if orientation == "v":
            self.image = pygame.Surface((1, config.DIMENSION_UNIT))
        elif orientation == "h":
            self.image = pygame.Surface((config.DIMENSION_UNIT, 1))
        self.image.fill(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
