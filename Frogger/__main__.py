import os
import random

from game.casting.actor import Actor
from game.casting.npc import Npc
from game.casting.cars import Cars
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 8
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Frogger"
WHITE = Color(255, 255, 255)
DEFAULT_CHICKEN = 20
DEFAULT_CARS = 20
ROAD_IMAGE = "Frogger/assets/images/road-bg.png"


def main():
    
    # create the cast
    cast = Cast()
    # background = LoadImage("Frogger/assets/images/road-bg.png")
    # background = Image(ROAD_IMAGE)
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the chicken
    x = int(MAX_X / 2)
    y = MAX_Y - CELL_SIZE
    position = Point(x, y)

    chicken = Actor()
    chicken.set_text("_")
    chicken.set_font_size(FONT_SIZE)
    chicken.set_color(WHITE)
    chicken.set_position(position)
    cast.add_actor("chicken", chicken)
    
    # create the artifacts

    for n in range(DEFAULT_CARS): 
        cars = Cars(COLS, CELL_SIZE, FONT_SIZE, 1)
        cast.add_actor("cars", cars)

   


    for n in range(DEFAULT_CHICKEN): 
        npc = Npc(COLS, CELL_SIZE, FONT_SIZE, 1)
        cast.add_actor("npc", npc)

    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()