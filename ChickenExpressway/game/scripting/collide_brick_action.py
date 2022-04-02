from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body



class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            racket_body = racket.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(racket_body, brick_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)

                stats.lose_life()
                position = Point(CENTER_X - RACKET_WIDTH , SCREEN_HEIGHT - RACKET_HEIGHT)
                racket_body.set_position(position)
                
                # if stats.get_lives() > 0:
                #     callback.on_next(TRY_AGAIN) 
                # else:
                #     callback.on_next(GAME_OVER)
                #     self._audio_service.play_sound(OVER_SOUND)



