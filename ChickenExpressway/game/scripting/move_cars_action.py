from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveCarsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        cars = cast.get_actors(BRICK_GROUP)
        for car in cars:
            body = car.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)
        