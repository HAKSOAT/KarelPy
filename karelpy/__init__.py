from karelpy.world import World

world = World()
world.parse_template()
world.build()
karel = world.karel_interface
display = world.display
wait = world.wait
load = world.load
close = world.close