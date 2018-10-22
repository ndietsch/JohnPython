import pygame
import random
from os import path

WIDTH = 580 #width of our game window
HEIGHT = 600# height of our game window
FPS = 60 #number of frames per second

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#initialise game and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shmup!")
clock = pygame.time.Clock()
