import pygame
import random

WIDTH = 460 #width of our game window
HEIGHT = 580 # height of our game window
FPS = 100 #number of frames per second

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialise game and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game")
clock = pygame.time.Clock()
class player(pygame.sprite.Sprite):
    def __init__(self):
 class playpr
        self.arg = arg
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 13

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx += -5
        if keystate[pygame.K_LEFT]:
            self.speedx += -5
        if keystate[pygame.K_d]:
            self.speedx += 5
        if keystate[pygame.K_RIGHT]:
            self.speedx += 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
             self.rect.left = 0
all_sprites = pygame.sprite.Group()

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
