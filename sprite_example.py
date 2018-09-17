#Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 800 #width of our game window
HEIGHT = 600 # height of our game window
FPS = 30 #number of frames per second

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def  update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

#initialise game and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while  running:
    # setup clock
    clock.tick(FPS)
    # event handler
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing, flip everything
    pygame.display.flip()

pygame.quit()
