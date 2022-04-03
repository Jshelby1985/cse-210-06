from constants import *
from game.casting.point import Point
from game.scripting.action import Action
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.label import Label
from game.casting.text import Text 



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
            
            self._add_dialog(cast, WIN)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)
        
        
        
        