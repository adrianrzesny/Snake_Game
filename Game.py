from Bonus import Bonus 
from Direction import Direction 
from Snake import Snake
import pygame
import time 
import random 

#Window dimensions
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 608

points = 0

#Create background
background = pygame.Surface((800, 608))

# Board 25 x 19
for i in range(25):
    for j in range(19):
        image = pygame.image.load("images/background.png")
        mask = (random.randrange(0,20), random.randrange(0, 20), random.randrange(0,20))

        image.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(image, (i*32, j*32))  

#Settings pygame 
pygame.init()
screen = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])
clock = pygame.time.Clock()
font_result = pygame.font.SysFont('Comic Sans MS', 24)
font_game_over = pygame.font.SysFont('Comic Sans MS', 72)

#Snake
snake = Snake()
MOVE_SNAKE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE_EVENT, 200)

#Bonuses
bonus = Bonus()
bonuses = pygame.sprite.Group()
bonuses.add(bonus)

game_works = True
while game_works:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_works = False
                
            if event.key == pygame.K_w:
                snake.change_direction(Direction.UP)
                
            if event.key == pygame.K_s:
                snake.change_direction(Direction.DOWN)
                
            if event.key == pygame.K_a:
                snake.change_direction(Direction.LEFT)
                
            if event.key == pygame.K_d:
                snake.change_direction(Direction.RIGHT)

        elif event.type == MOVE_SNAKE_EVENT:
            snake.update()

        elif event.type == pygame.QUIT:
            game_works = False

    #Checking if the snake's head is on the bonus
    collision_with_bonus = pygame.sprite.spritecollideany(snake, bonuses)
    if collision_with_bonus != None:
        points+=1
        collision_with_bonus.kill()
        snake.collect_bonus()
        bonus = Bonus()
        bonuses.add(bonus)
        
    #Draw background
    screen.blit(background, (0,0))

    #Check if the game is over
    if snake.check_collision():
        text_game_over = font_game_over.render('GAME OVER', False, (200,0,0))
        screen.blit(text_game_over, (WIDTH_SCREEN/2-200, HEIGHT_SCREEN/2-60))
        game_works = False

    #Draw segments
    snake.draw_segments(screen)

    #Draw head snake
    screen.blit(snake.image, snake.rect)

    #Draw bonus
    for bonus in bonuses:
        screen.blit(bonus.image, bonus.rect)

    #Display result
    text_result = font_result.render(f'Result: {points}', False, (0, 0, 0))
    screen.blit(text_result, (16, 16))

    #Clear screen 
    pygame.display.flip()

    #Ustaw stałe 30 FPS
    clock.tick(30)

#Delay
time.sleep(3)

#Close application
pygame.quit()
