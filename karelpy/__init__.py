from karelpy.world import World

world = World()
world.parse_template()
world.build()
real_karel = world.real_karel
display = world.display
wait = world.wait
load = world.load
close = world.close