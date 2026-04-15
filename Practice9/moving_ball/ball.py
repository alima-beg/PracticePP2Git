import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))  # создаем окно
WHITE = (255, 255, 255)  # белый цвет
RED = (255, 0, 0)  # красный цвет
done = False  # флаг выхода
clock = pygame.time.Clock()  # контроль FPS
circle_start_w = 600  # начальная позиция X
circle_start_h = 350  # начальная позиция Y

while not done:  # главный цикл
   keys = pygame.key.get_pressed()  # проверка удержания клавиш

   for event in pygame.event.get():  # обработка событий
       if event.type == pygame.QUIT:  # если закрыли окно
           done = True  # выходим

   if keys[pygame.K_UP]:  # стрелка вверх
       if circle_start_h > 38:  # граница сверху
           circle_start_h -= 20  # движение вверх

   if keys[pygame.K_DOWN]:  # стрелка вниз
       if circle_start_h < 662:  # граница снизу
           circle_start_h += 20  # движение вниз

   if keys[pygame.K_LEFT]:  # стрелка влево
       if circle_start_w > 38:  # граница слева
           circle_start_w -= 20  # движение влево

   if keys[pygame.K_RIGHT]:  # стрелка вправо
       if circle_start_w < 1162:  # граница справа
           circle_start_w += 20  # движение вправо

   screen.fill(WHITE)  # очищаем экран
   pygame.draw.circle(screen, RED, (circle_start_w, circle_start_h), 25)  # рисуем круг
   pygame.display.flip()  # обновляем экран
   clock.tick(60)  # 60 FPS