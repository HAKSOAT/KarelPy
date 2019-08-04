from karelpy.world import World
from karelpy.ikarel import KarelInterface
from karelpy import config

world = World()


def load(number):
    global world
    world.load(number)
    karel = KarelInterface(world.karel_sprites,
                   world.beeper_sprites,
                   world.wall_sprites,
                   world.dot_sprites,
                   world.screen, world.speed)
    return karel

# Code user has to load world before displaying it
display = world.display
wait = world.wait
close = world.close