import pygame

class BoxesGame():
    def __init__(self):
        pygame.init()
        width, height = 389, 489
        # create the screen
        self.screen = pygame.display.set_mode(width, height)
        pygame.display.set_caption("Boxes")
        # init clock
        self.clock = pygame.time.Clock()

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
