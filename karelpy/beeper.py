import pygame
import config


class Beeper(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/beeper.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.DIMENSION_UNIT//2, config.DIMENSION_UNIT//2))
        self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.rect.center = center
