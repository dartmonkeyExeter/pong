import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pong') 

running = True

width = 12.5
height = 80

ball_x = 250
ball_y = 250

x_vel = -0.05
y_vel = -0.01

player_one_x = 25
player_one_y = 250

player_two_x = 460
player_two_y = 250

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w] and player_one_y>0: 
        player_one_y -= 0.5
    if keys[pygame.K_s] and player_one_y<500-height: 
        player_one_y += 0.5
    if keys[pygame.K_UP] and player_two_y>0: 
        player_two_y -= 0.5
    if keys[pygame.K_DOWN] and player_two_y<500-height: 
        player_two_y += 0.5
    if ball_y <= 0+9 or ball_y >= 500-9:
        y_vel = -y_vel
    if (ball_x-9 < player_one_x) and (ball_y < player_one_y + 40) and (ball_y > player_one_y - 40):
        x_vel = -x_vel
    if (ball_x-9 > player_two_x) and (ball_y < player_two_y + 40) and (ball_y > player_two_y - 40):
        x_vel = -x_vel
    ball_y += y_vel
    ball_x += x_vel


    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255), (ball_x, ball_y, 9, 9))
    pygame.draw.rect(win, (255, 255, 255), (player_one_x, player_one_y, width, height))
    pygame.draw.rect(win, (255, 255, 255), (player_two_x, player_two_y, width, height))
    pygame.display.update()

pygame.quit()
