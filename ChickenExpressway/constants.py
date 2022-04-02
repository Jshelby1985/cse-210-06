import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "ChickenExpressway"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "ChickenExpressway/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "ChickenExpressway/assets/sounds/boing.wav"
WELCOME_SOUND = "ChickenExpressway/assets/sounds/start.wav"
OVER_SOUND = "ChickenExpressway/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "ChickenExpressway/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"ChickenExpressway/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 28
RACKET_HEIGHT = 60
RACKET_RATE = 3
RACKET_VELOCITY = 1

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"ChickenExpressway/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"ChickenExpressway/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"ChickenExpressway/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"ChickenExpressway/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 160
BRICK_HEIGHT = 60
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# car1
CAR1_GROUP = "car1"
CAR1_IMAGE = {"b":["ChickenExpressway/assets/images/010.png"]}
CAR1_WIDTH = 80
CAR1_HEIGHT = 28
CAR1_DELAY = 0.5
CAR1_RATE = 4
CAR1_POINTS = 50

# car2
CAR2_GROUP = "car2"
CAR2_IMAGE = {"g":["ChickenExpressway\assets\images\car2.png"]}
CAR2_WIDTH = 80
CAR2_HEIGHT = 28
CAR2_DELAY = 0.5
CAR2_RATE = 4
CAR2_POINTS = 50

# car3
CAR3_GROUP = "car3"
CAR3_IMAGE = {"p":["ChickenExpressway\assets\images\car3.png"]}
CAR3_WIDTH = 80
CAR3_HEIGHT = 28
CAR3_DELAY = 0.5
CAR3_RATE = 4
CAR3_POINTS = 50

# car4
CAR4_GROUP = "car4"
CAR4_IMAGE = {"y":["ChickenExpressway\assets\images\car4.png"]}
CAR4_WIDTH = 80
CAR4_HEIGHT = 28
CAR4_DELAY = 0.5
CAR4_RATE = 4
CAR4_POINTS = 50


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "Winner Winner Chicken Dinner"
WAS_GOOD_GAME = "GAME OVER"