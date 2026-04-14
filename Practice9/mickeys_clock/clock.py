import pygame  # library for creating games and graphics
import datetime  # module for getting current date and time
import os  # module for working with file paths
pygame.init()  # initialize all pygame modules

screen = pygame.display.set_mode((1200, 700))  # create a window (width=1200, height=700)
WHITE = (255, 255, 255)  # RGB color for white

# path to the folder with images
base = r'C:\Users\Huawei\OneDrive\Desktop\PracticePP2\Practice9\mickeys_clock\images'

# load images with alpha channel (transparency support)
image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey      = pygame.image.load(os.path.join(base, 'mUmrP.png')).convert_alpha()
hand_l      = pygame.image.load(os.path.join(base, 'hand_left_centered.png')).convert_alpha()
hand_r      = pygame.image.load(os.path.join(base, 'hand_right_centered.png')).convert_alpha()

# resize images to fit the screen design
resized_image = pygame.transform.scale(image_surface, (800, 600))  # clock background
res_mickey    = pygame.transform.scale(mickey, (350, 350))        # character image
hand_l_base   = pygame.transform.scale(hand_l, (80, 80))          # minute hand base image
hand_r_base   = pygame.transform.scale(hand_r, (100, 100))        # hour hand base image

clockc = (300, 170)  # unused variable (possible old center position)
CLOCK_CENTER = (600, 320)  # center of the clock
clock = pygame.time.Clock()  # object to control FPS (frame rate)
done = False  # game loop control variable

while not done:
   for event in pygame.event.get():  # handle all events (keyboard, mouse, window)
       if event.type == pygame.QUIT:  # if user closes the window
           done = True  # exit the loop

   # get current time
   now = datetime.datetime.now()
   h = now.hour % 12   # convert to 12-hour format
   m = now.minute      # current minutes
   s = now.second      # current seconds

   # calculate rotation angles for clock hands
   minutes_angle = -(m * 6 + s * 0.1)   # 6° per minute + smooth movement from seconds
   hours_angle   = -(h * 30 + m * 0.5)  # 30° per hour + smooth movement from minutes

   # rotate clock hands
   rotated_minutes = pygame.transform.rotate(hand_l_base, minutes_angle)
   rotated_hours   = pygame.transform.rotate(hand_r_base, hours_angle)
   # set the center position for rotated images
   minutes_rect = rotated_minutes.get_rect(center=(600, 340))
   hours_rect   = rotated_hours.get_rect(center=(600, 340))

   # clear screen with white background
   screen.fill(WHITE)

   # draw clock background
   image_rect = resized_image.get_rect()
   image_rect.center = (600, 340)
   screen.blit(resized_image, image_rect)
   # draw Mickey image
   mic_rect = res_mickey.get_rect(center=CLOCK_CENTER)
   screen.blit(res_mickey, mic_rect)
   # draw clock hands
   screen.blit(rotated_hours, hours_rect)
   screen.blit(rotated_minutes, minutes_rect)

   # update display
   pygame.display.flip()
   # limit FPS to 60 frames per second
   clock.tick(60)
   
# quit pygame properly
pygame.quit()