import pygame
pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode([width, height])
def GameLoop():
    while True:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
GameLoop()