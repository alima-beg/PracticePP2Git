import pygame
import sys
from player import Player

pygame.init()
# create game window
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Moving Circle Game")
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

# create player object
player = Player(600, 350)
running = True  # game loop control

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # exit loop

    keys = pygame.key.get_pressed()  # get keyboard input
    player.move(keys)  # update player position

    screen.fill(WHITE)  # clear screen
    player.draw(screen)  # draw player

    pygame.display.flip()  # update screen
    clock.tick(60)  # 60 FPS limit
pygame.quit()  # close pygame
sys.exit()  # close program
 