import pygame
import random

pygame.init()
game_size_x = 25
game_size_y = 25
screen = pygame.display.set_mode((game_size_x*10,game_size_y*10))
screen.fill((255,255,255))
pygame.display.update()

snake = [(game_size_x//2, game_size_y//2)]
head_x = snake[0][0]
head_y = snake[0][1]
direction = 'R'
length = 2
pick_up_active = False
game_over = False
pickup_x = -1
pickup_y = -1

while not game_over:
    keys = pygame.key.get_pressed()
    print(keys[pygame.K_UP])
    if keys[pygame.K_UP] == 1:
        if direction != 'D':
            direction = 'U'
    elif keys[pygame.K_DOWN] == 1:
        if direction != 'U':
            direction = 'D'
    elif keys[pygame.K_LEFT] == 1:
        if direction != 'R':
            direction = 'L'
    elif keys[pygame.K_RIGHT] == 1:
        if direction != 'L':
            direction = 'R'

    if direction == 'R':
        head_x += 1
    elif direction == 'U':
        head_y -= 1
    elif direction == 'L':
        head_x -= 1
    elif direction == 'D':
        head_y += 1

    if head_x == pickup_x and head_y == pickup_y:
        pick_up_active = False
        length += 1

    snake.append((head_x, head_y))

    if len(snake) > length:
        snake = snake[1:len(snake)]

    screen.fill((255,255,255))

    valid_pickup = False
    if not pick_up_active:
        while not valid_pickup:
            pickup_x = random.randint(2, game_size_x - 2)
            pickup_y = random.randint(2, game_size_y - 2)
            if (pickup_x, pickup_y) not in snake:
                valid_pickup = True
                pick_up_active = True
    print(pickup_x, pickup_y)
    pygame.draw.rect(screen, (255, 0, 0), (pickup_x*10, pickup_y*10, 10, 10))

    for (x, y) in snake:
        pygame.draw.rect(screen, (0, 0, 0), (x*10, y*10, 10, 10))
    pygame.display.update()

    if head_x == game_size_x or head_y == game_size_y or head_x == 0 or head_y == 0 or (head_x, head_y) in snake[0:len(snake)-2]:
        game_over = True

    pygame.time.delay(50)
    pygame.event.pump()

print('game over')
pygame.quit()
exit()