import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
WHITE = (255, 255, 255)
MyColor = (255,192,203)
done = False
clock = pygame.time.Clock()
circle_start_w = 600
circle_start_h = 350

while not done:
   keys = pygame.key.get_pressed()

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

   if keys[pygame.K_UP]:
       if circle_start_h > 38:
           circle_start_h -= 20

   if keys[pygame.K_DOWN]:
       if circle_start_h < 662:
           circle_start_h += 20

   if keys[pygame.K_LEFT]:
       if circle_start_w > 38:
           circle_start_w -= 20

   if keys[pygame.K_RIGHT]:
       if circle_start_w < 1162:
           circle_start_w += 20

   screen.fill(WHITE)
   pygame.draw.circle(screen, MyColor, (circle_start_w, circle_start_h), 25)
   pygame.display.flip()
   clock.tick(60)