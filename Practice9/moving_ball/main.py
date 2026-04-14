import pygame
import sys
from ball import Ball

pygame.init()
# create window
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Moving Circle")
WHITE = (255, 255, 255)
clock = pygame.time.Clock()  # FPS controller

# create ball object
ball = Ball(600, 350)
done = False  # game loop flag

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # close game

    keys = pygame.key.get_pressed()  # keyboard input
    ball.move(keys)  # update position

    screen.fill(WHITE)  # clear screen
    ball.draw(screen)  # draw ball
    pygame.display.flip()  # update display
    clock.tick(60)  # limit FPS

pygame.quit()  # close pygame
sys.exit()  # exit program
 