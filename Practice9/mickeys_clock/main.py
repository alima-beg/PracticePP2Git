import pygame  
import sys
from clock import MickeyClock

def main():
    pygame.init()

    # create a square window (800x800) to match the clock design
    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # create the game window
    pygame.display.set_caption("Mickey Mouse Clock")  # set window title
    clock_app = MickeyClock(WIDTH, HEIGHT)  # create object of your clock class
    timer = pygame.time.Clock()  # clock object to control FPS (frame rate)
    running = True  # variable that controls the main loop

    while running:
        for event in pygame.event.get():  # check all user events
            if event.type == pygame.QUIT:  # if user clicks X button
                running = False  # stop the loop and close program

        clock_app.render(screen)  # draw/update the clock on screen
        pygame.display.flip()  # update the full display (show new frame)
        timer.tick(60)  # limit the program to 60 frames per second

    pygame.quit()  # close pygame properly (free resources)
    sys.exit()  # exit the Python program completely

# this line checks if the file is run directly (not imported)
if __name__ == "__main__":
    main()  # start the program
 