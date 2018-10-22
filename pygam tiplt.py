import pygame
import random
WIDTH = 360
HEIGHT = 480
FBS = 30
clock.tick(FBS)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = display.set_mode((WIDTH, HEIGHT))


screen = display.set_caption("my game")
clock = time.Clock()

# Game loop
rcnning = True
while rcnning:
    screen.fill(BLACK)
    pygam.display.flip()
    for event pygame.event.get():
        if event.type == pygam.QUIT:
            running = False

pygame.quit()
