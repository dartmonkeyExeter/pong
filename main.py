import pygame
from random import uniform

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pong')

my_font = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()

fps = 60

running = True

width = 8
height = 80

ball_x = 250
ball_y = 250

x_vel = -5
y_vel = 1

player_one_x = 25
player_one_y = 250

# Fix: Initialize player_two_y properly
player_two_x = 460
player_two_y = 250

p1_points = 0
p2_points = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_one_y > 0:
        player_one_y -= 10
    if keys[pygame.K_s] and player_one_y < 500 - height:
        player_one_y += 10
    if keys[pygame.K_UP] and player_two_y > 0:
        player_two_y -= 10
    if keys[pygame.K_DOWN] and player_two_y < 500 - height:
        player_two_y += 10
    if ball_y <= 0 + 9 or ball_y >= 500 - 9:
        y_vel = -y_vel
    
    if ball_x < player_one_x - 9:
        p2_points += 1
        ball_x = 250
        ball_y = 250

        x_vel = -5
        y_vel = 1
        player_one_y = 250
        player_two_y = 250
    elif ball_x > player_two_x + 9:
        p1_points += 1
        ball_x = 250
        ball_y = 250

        x_vel = -5
        y_vel = 1
        player_one_y = 250
        player_two_y = 250
    if (
        ball_x - 9 < player_one_x
        and ball_y + 9 > player_one_y
        and ball_y - 9 < player_one_y + height
    ):
        x_vel = -x_vel
        y_vel += uniform(-0.5,0.5)
    if (
        ball_x + 9 > player_two_x
        and ball_y + 9 > player_two_y
        and ball_y - 9 < player_two_y + height
    ):
        x_vel = -x_vel
        y_vel += uniform(-1.5,1.5)
    ball_y += y_vel
    ball_x += x_vel

    win.fill((0, 0, 0))
    player_one_points_display = my_font.render(f'{str(p1_points)}', False, (255, 255, 255))
    win.blit(player_one_points_display, (2,0))
    player_one_points_display = my_font.render(f'{str(p2_points)}', False, (255, 255, 255))
    win.blit(player_one_points_display, (480,0))
    pygame.draw.rect(win, (255, 255, 255), (ball_x, ball_y, 9, 9))
    pygame.draw.rect(win, (255, 255, 255), (player_one_x, player_one_y, width, height))
    pygame.draw.rect(win, (255, 255, 255), (player_two_x, player_two_y, width, height))
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
