from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveCarsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        car1 = cast.get_actors(BRICK_GROUP)
        # car2 = cast.get_actors(CAR2_GROUP)
        # car3 = cast.get_actors(CAR3_GROUP)
        # car4 = cast.get_actors(CAR4_GROUP)

        for car in car1:
            body = car.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            x = position.get_x()

            if x < -180:
                position = Point(SCREEN_WIDTH, position.get_y())
            elif x > (SCREEN_WIDTH):
                position = Point(0-180, position.get_y())
            
            body.set_position(position)
