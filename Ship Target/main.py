import random, pgzrun, itertools

TITLE = 'Practicing Animation'
WIDTH = 500
HEIGHT = 500

blockpos = [(450,50), (450,450), (50,450), (50,50)]
bpos = itertools.cycle(blockpos)
spiky_block = Actor('spiky_block', center = (50,50))

ship = Actor('ship', center = (200,200))






def draw():
    screen.clear()
    spiky_block.draw()
    ship.draw()

def moveblock():
    animate(
        spiky_block,'bounce_end', duration = 1, pos= next(bpos)
    )

moveblock()
clock.schedule_interval(moveblock,2)

def ship_target():
    x = random.randint(100,300)
    y = random.randint(100,300)
    ship.target = (x,y)
    targetangle = ship.angle_to(ship.target)
    targetangle += 360*((ship.angle-targetangle+180)//360)
    def moveship():
        anim = animate(
            ship, tween = 'accel_decel', pos = ship.target, duration = ship.distance_to(ship.target)/200,
            on_finished = ship_target, 
        )

    
    animate(
        ship, angle = targetangle, duration = 0.3, on_finished = moveship
    )

ship_target()


pgzrun.go()