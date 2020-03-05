import pygame
import random
import sys
import math
import numpy as np
import shelve



ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(0,150,0)
green=(0,240,0)
WHITE=(255,255,255)
blue=(0,0,160)
PLAYER_BALL=1
COMP_BALL=2

WINDOW_LENGTH=4
EMPTY=0

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Connect Four')

clock=pygame.time.Clock()
pygame.init()

win_font=pygame.font.SysFont("monospace",75)


x = int(SQUARE_SIZE / 2)
y = int(SQUARE_SIZE / 2)
initial_position = (x, y)


PLAYER=0
AI=1



