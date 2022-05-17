import pygame
import math
ROW = 6
COLUMN = 7
BLUE = (50, 100, 200)
RED = (200, 0, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
SQUARESIZE = 100
RADIUS = SQUARESIZE / 2 - 5
WINDOW_SIZE = 4
EMPTY = 0
width = COLUMN * SQUARESIZE             #700 pixel
height = (ROW+1) * SQUARESIZE           #700 pixel
size =(width,height)
display = pygame.display.set_mode(size)
PLAYER = 0
AI = 1

prune = True
k = 5

PLAYER_PIECE = 1
AI_PIECE = 2

ALPHA_WORST_VALUE = -math.inf           #worst value alpha could have
BETA_WORST_VALUE = math.inf              #worst value beta could have
