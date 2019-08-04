from karelpy import config
import pygame


class Dot(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        width = config.DIMENSION_UNIT / 10
        height = config.DIMENSION_UNIT / 10
        self.image = pygame.Surface((width, height))
        self.image.fill(config.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
