import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 700))
WHITE = (255, 255, 255)

base = r'C:\Users\Huawei\OneDrive\Desktop\PracticePP2\Practice9\mickeys_clock\images'

# загружаем изображения и сразу оптимизируем их с прозрачностью
image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()   # фон часов
mickey        = pygame.image.load(os.path.join(base, 'mikkey.png')).convert_alpha()   # Микки
hand_l        = pygame.image.load(os.path.join(base, 'hand_left_centerd.png')).convert_alpha()  # минутная стрелка
hand_r        = pygame.image.load(os.path.join(base, 'hand_right_centered.png')).convert_alpha() # часовая стрелка

# изменяем размеры изображений
resized_image = pygame.transform.scale(image_surface, (800, 600))  # фон
res_mickey    = pygame.transform.scale(mickey, (350, 350))         # Микки
hand_l_base   = pygame.transform.scale(hand_l, (100, 100))         # минутная стрелка
hand_r_base   = pygame.transform.scale(hand_r, (100, 100))         # часовая стрелка

clockc = (300, 170)   # (не используется — можно удалить)
CLOCK_CENTER = (600, 320)   # центр часов (где будет Микки)
clock = pygame.time.Clock()   # объект для контроля FPS (кадров в секунду)
done = False                  # флаг выхода из игры

while not done:

    # обработка событий (нажатия клавиш, закрытие окна и т.д.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # если нажали "крестик"
            done = True                # завершаем цикл

    # получаем текущее время
    now = datetime.datetime.now()
    h = now.hour % 12   # часы (в 12-часовом формате)
    m = now.minute      # минуты
    s = now.second      # секунды

    # вычисляем угол поворота минутной стрелки
    # 1 минута = 6 градусов (360/60)
    # добавляем секунды для плавного движения
    minutes_angle = -(m * 6 + s * 0.1)

    # вычисляем угол поворота часовой стрелки
    # 1 час = 30 градусов (360/12)
    # добавляем минуты для плавного движения
    hours_angle = -(h * 30 + m * 0.5)

    # поворачиваем изображения стрелок
    rotated_minutes = pygame.transform.rotate(hand_l_base, minutes_angle)
    rotated_hours   = pygame.transform.rotate(hand_r_base, hours_angle)

    # создаём прямоугольники (Rect) для позиционирования стрелок
    # центр задаёт точку вращения
    minutes_rect = rotated_minutes.get_rect(center=(650, 320))
    hours_rect   = rotated_hours.get_rect(center=(620, 346))

    # очищаем экран (заливаем белым цветом)
    screen.fill(WHITE)

    # рисуем фон часов
    image_rect = resized_image.get_rect()
    image_rect.center = (600, 340)
    screen.blit(resized_image, image_rect)

    # рисуем Микки в центре часов
    mic_rect = res_mickey.get_rect(center=CLOCK_CENTER)
    screen.blit(res_mickey, mic_rect)

    # рисуем стрелки
    screen.blit(rotated_hours, hours_rect)     # часовая
    screen.blit(rotated_minutes, minutes_rect) # минутная

    # обновляем экран (показываем всё нарисованное)
    pygame.display.flip()
    # ограничиваем FPS до 60 кадров в секунду
    clock.tick(60)

pygame.quit()