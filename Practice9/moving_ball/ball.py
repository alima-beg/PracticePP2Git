import pygame

class Ball:
   def __init__(self, x, y):
       self.x = x  # initial X position
       self.y = y  # initial Y position
       self.radius = 25  # circle size
       self.speed = 20  # movement speed

   def move(self, keys):
       # move up with boundary check
       if keys[pygame.K_UP] and self.y > 38:
           self.y -= self.speed
       # move down
       if keys[pygame.K_DOWN] and self.y < 662:
           self.y += self.speed
       # move left
       if keys[pygame.K_LEFT] and self.x > 38:
           self.x -= self.speed
       # move right
       if keys[pygame.K_RIGHT] and self.x < 1162:
           self.x += self.speed
           
   def draw(self, screen):
       pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)