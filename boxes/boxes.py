import pygame

class BoxesGame():
    def __init__(self):
        pygame.init()
        width, height = 389, 489
        # create the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")
        # init clock
        self.clock = pygame.time.Clock()

        self.boardh = [[False for x in range (6)] for y in range(7)]
        self.boardv = [[False for x in range (7)] for y in range(6)]
        # init the Graphics
        self.initGraphics()

    def initGraphics(self):
        self.normallinev = pygame.image.load("normalline.png")
        self.normallineh = pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev = pygame.image.load("bar_done.png")
        self.bar_doneh = pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.hoverlinev = pygame.image.load("hoverline.png")
        self.hoverlineh = pygame.transform.rotate(pygame.image.load("hoverline.png"), -90)



    def update(self):
        # sleep
        self.clock.tick(60)
        # clear the screen
        self.screen.fill(0)

        for event in pygame.event.get():
            # process quit sigcgnal
            if event.type == pygame.QUIT:
                exit()

        # update the screen
        pygame.display.flip()


bg=BoxesGame()
while 1:
    bg.update()
