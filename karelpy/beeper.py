from karelpy import config
import os
import pygame


class Beeper(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        base_dir = os.path.abspath(os.path.dirname(__file__))
        beeper_path = os.path.join(base_dir, "world", "beeper.png")
        self.image = pygame.image.load(beeper_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.DIMENSION_UNIT//2, config.DIMENSION_UNIT//2))
        self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.rect.center = center
