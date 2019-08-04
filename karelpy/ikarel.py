from karelpy import config
import pygame


class KarelInterface:
    def __init__(self, karel_sprite, beeper_sprites, wall_sprites, dot_sprites, screen, speed):
        self.karel = karel_sprite.sprites()[0]
        self.karel_sprite = karel_sprite
        self.beeper_sprites = beeper_sprites
        self.wall_sprites = wall_sprites
        self.dot_sprites = dot_sprites
        self.screen = screen
        self.speed = speed
        self.clock = pygame.time.Clock()

    def refresh(self):
        for i in range(3):
            self.clock.tick(config.FPS * self.speed)
            self.dot_sprites.update()
            self.beeper_sprites.update()
            self.wall_sprites.update()
            self.karel_sprite.update()
            self.screen.fill(config.WHITE)
            self.dot_sprites.draw(self.screen)
            self.beeper_sprites.draw(self.screen)
            self.wall_sprites.draw(self.screen)
            self.karel_sprite.draw(self.screen)
            pygame.display.flip()

    def move(self):
        self.karel.move(self.wall_sprites)
        self.refresh()

    def turn_left(self):
        self.karel.turn_left()
        self.refresh()

    def pick_beeper(self):
        self.karel.pick_beeper(self.beeper_sprites)
        self.refresh()

    def put_beeper(self):
        self.karel.put_beeper(self.beeper_sprites)
        self.refresh()

    def beepers_present(self):
        return self.karel.beepers_present(self.beeper_sprites)

    def beepers_in_bag(self):
        return self.karel.beepers_in_bag()

    def front_is_clear(self):
        return self.karel.front_is_clear(self.wall_sprites)

    def facing_north(self):
        return self.karel.facing_north()

    def facing_south(self):
        return self.karel.facing_south()

    def facing_east(self):
        return self.karel.facing_east()

    def facing_west(self):
        return self.karel.facing_west()
