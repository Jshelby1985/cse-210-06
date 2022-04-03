from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(SCREEN_WIDTH, position.get_y())
        elif x > (SCREEN_WIDTH):
            position = Point(0, position.get_y())
        body.set_position(position)

        if y < 0:
            position = Point(SCREEN_HEIGHT, position.get_x())
        elif y > (SCREEN_HEIGHT):
            position = Point(0, position.get_x())
        body.set_position(position)
        
        