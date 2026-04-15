import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = r'C:\Users\Акниет\Desktop\practice_pp2\Practice9\music_player\music'  # путь к музыке

songs = [os.path.join(music_folder, f) for f in os.listdir(music_folder)
        if f.endswith(('.mp3', '.wav'))]  # список файлов музыки

if not songs:  # если нет файлов
   print("No .mp3 or .wav files found in", music_folder)
   pygame.quit()
   exit()

durations = []  # список длительности треков
for song in songs:
   durations.append(pygame.mixer.Sound(song).get_length())  # длина каждого трека
music_index = 0  # текущий трек
num = len(songs)  # количество треков

screen = pygame.display.set_mode((600, 400))  # окно
BG = (255, 255, 255)  # фон
CARD = (200, 200, 200)  # карточка
ACCENT = (0, 200, 150)  # акцент
TEXT = (240, 240, 240)  # текст
SUBTEXT = (140, 140, 140)  # вторичный текст
HIGHLIGHT = (255, 80, 80)  # выделение
BLACK = (0, 0, 0)  # черный
font = pygame.font.Font(None, 32)  # основной шрифт
small_font = pygame.font.Font(None, 22)  # маленький шрифт
done = False  # выход из программы
clock = pygame.time.Clock()  # FPS

def play_next():  # следующий трек
   global music_index
   music_index = (music_index + 1) % num  # переход по кругу
   pygame.mixer.music.load(songs[music_index])
   pygame.mixer.music.play()

def play_prev():  # предыдущий трек
   global music_index
   music_index = (music_index - 1) % num
   pygame.mixer.music.load(songs[music_index])
   pygame.mixer.music.play()

def get_start(h, m, s):  # формат времени HH:MM:SS
   if (h < 10):
       if (m < 10):
           if (s < 10):
               return font.render(f"0{h:.0f}:0{m:.0f}:0{s:.0f}", True, BLACK)
           else:
               return font.render(f"0{h:.0f}:0{m:.0f}:{s:.0f}", True, BLACK)
       elif (s < 10):
           return font.render(f"0{h:.0f}:{m:.0f}:0{s:.0f}", True, BLACK)
       else:
           return font.render(f"0{h:.0f}:{m:.0f}:{s:.0f}", True, BLACK)
   elif (m < 10):
       if (s < 10):
           return font.render(f"{h:.0f}:0{m:.0f}:0{s:.0f}", True, BLACK)
       else:
           return font.render(f"{h:.0f}:0{m:.0f}:{s:.0f}", True, BLACK)
   else:
       return font.render(f"{h:.0f}:{m:.0f}:{s:.0f}", True, BLACK)
   
current_times = 0  # текущее время трека
is_paused = False  # пауза

while not done:
   if durations[music_index] > 0:  # защита от деления на 0
       progress_ratio = current_times / durations[music_index]  # процент проигрывания
       circle_x = 200 + progress_ratio * 900  # позиция индикатора
   else:
       circle_x = 200
   if pygame.mixer.music.get_busy():  # если музыка играет
       current_times = pygame.mixer.music.get_pos() / 1000  # время в секундах
   screen.fill(BG)  # очистка экрана

   # карточка
   pygame.draw.rect(screen, CARD, (20, 20, 560, 360), border_radius=15)

   # название трека
   song_name = os.path.basename(songs[music_index])
   name_surface = font.render(song_name, True, HIGHLIGHT)
   screen.blit(name_surface, (50, 60))

   # линия прогресса
   pygame.draw.line(screen, SUBTEXT, (50, 200), (550, 200), 3)
   if durations[music_index] > 0:
       progress_ratio = current_times / durations[music_index]
       circle_x = 50 + progress_ratio * 500  # движение по линии
   else:
       circle_x = 50
   pygame.draw.line(screen, ACCENT, (50, 200), (circle_x, 200), 4)  # заполненная линия
   pygame.draw.circle(screen, ACCENT, (circle_x, 200), 6)  # кружок-индикатор

   # расчет времени
   h = current_times // 3600
   m = current_times // 60
   s = current_times % 60
   start = get_start(h, m, s)  # текущее время
   end = get_start(durations[music_index]//3600,
                   durations[music_index]//60,
                   durations[music_index]%60)  # длительность
   screen.blit(start, (50, 220))
   screen.blit(end, (470, 220))

   # список треков
   for i, s in enumerate(songs):
       s0 = os.path.basename(s)
       color = TEXT if s0 != song_name else HIGHLIGHT  # выделение текущего
       name = small_font.render(f'{i+1}. {s0}', True, color)
       screen.blit(name, (50, 260 + i*20))

   # управление
   controls = small_font.render("P Play | S Pause | N Next | B Back | Q Quit", True, SUBTEXT)
   screen.blit(controls, (50, 330))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:  # закрытие окна
           done = True
       elif event.type == pygame.KEYDOWN:  # нажатие клавиш
           if event.key == pygame.K_q:  # выход
               done = True
           elif event.key == pygame.K_p:  # play
               if is_paused:
                   pygame.mixer.music.unpause()
                   is_paused = False
               elif not pygame.mixer.music.get_busy():
                   pygame.mixer.music.load(songs[music_index])
                   pygame.mixer.music.play()
                   pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)  # событие конца
           elif event.key == pygame.K_s:  # pause
               if pygame.mixer.music.get_busy():
                   pygame.mixer.music.pause()
                   is_paused = True
           elif event.key == pygame.K_n:  # следующий
               play_next()
               is_paused = False
           elif event.key == pygame.K_b:  # предыдущий
               play_prev()
               is_paused = False
       elif event.type == pygame.USEREVENT + 1:  # когда трек закончился
           play_next()

   pygame.display.flip()  # обновление экрана
   clock.tick(15)
pygame.quit()
 