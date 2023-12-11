#game
import pygame
import time
import random

# Работа с пользователем
print("Выберите сложность игры: 1 - простой, 2 - средний, 3 - сложный")
x=int(input())
if x==1:
    snake_speed = 10
elif x==2:
    snake_speed = 15
elif x==3:
    snake_speed = 20

# Поле игры
window_x = 720
window_y = 480

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Начало игры
pygame.init()

# Экран
pygame.display.set_caption('Snake Game')
game_display = pygame.display.set_mode((window_x, window_y))

# Расположение змейки и яблока
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10] 
fruit_spawn = True

# Изначальное положение
direction = 'RIGHT'
change_to = direction

# Изначальный счёт
score = 0

# Инициализация объекта Clock
clock = pygame.time.Clock()

# Завершение игры
def game_over():
   my_font = pygame.font.SysFont('times new roman', 60) #создание объекта шрифта
   game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
   game_over_rect = game_over_surface.get_rect() #место отображения текста
   game_over_rect.midtop = (window_x/2, window_y/4)
   game_display.fill(black) #заполнение экрана черным цветом
   game_display.blit(game_over_surface, game_over_rect) #рисует текст на экране
   pygame.display.flip() #обновление экрана
   time.sleep(2) #задержка на 2 секунды
   pygame.quit() #завершение игры
   quit()

# Основа движений
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: #досрочное завершение игры
           pygame.quit()
           quit()
       elif event.type == pygame.KEYDOWN: #перемещение
           if event.key == pygame.K_UP:
               change_to = 'UP'
           if event.key == pygame.K_DOWN:
               change_to = 'DOWN'
           if event.key == pygame.K_LEFT:
               change_to = 'LEFT'
           if event.key == pygame.K_RIGHT:
               change_to = 'RIGHT'

   if change_to == 'UP' and direction != 'DOWN':
       direction = 'UP'
   if change_to == 'DOWN' and direction != 'UP':
       direction = 'DOWN'
   if change_to == 'LEFT' and direction != 'RIGHT':
       direction = 'LEFT'
   if change_to == 'RIGHT' and direction != 'LEFT':
       direction = 'RIGHT'

   if direction == 'UP':
       snake_position[1] -= 10
   if direction == 'DOWN':
       snake_position[1] += 10
   if direction == 'LEFT':
       snake_position[0] -= 10
   if direction == 'RIGHT':
       snake_position[0] += 10

   snake_body.insert(0, list(snake_position)) #вставка новой позиции змейки в начало списка
   if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
       score += 10
       fruit_spawn = False
   else:
       snake_body.pop() #изображение движения змейки (удаление блока)

   if not fruit_spawn: #для нового яблока
       fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
   fruit_spawn = True
   game_display.fill(black)

   for pos in snake_body: #визуализация тела змейки
       pygame.draw.rect(game_display, green, pygame.Rect(pos[0], pos[1], 10, 10))

   pygame.draw.rect(game_display, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)) #создание прямоугольника-тела змейки

   if snake_position[0] < 0 or snake_position[0] > window_x-10: #проверка на выход за рамки поля игры
       game_over()
   if snake_position[1] < 0 or snake_position[1] > window_y-10:
       game_over()

   for block in snake_body[1:]: #проверка на столкновение с собственным телом
       if snake_position[0] == block[0] and snake_position[1] == block[1]:
           game_over()

   clock.tick(snake_speed) #частота кадров
   pygame.display.update() #фулл обновление экрана
