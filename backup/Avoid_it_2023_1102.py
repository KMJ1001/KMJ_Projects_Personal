'''
Avoid_it_2023.py
-----------------
Avoid it | ver 3 (2023-2)
Written by KimMinJi
----------------
to do list
=increase readibility: rename variables, etc.
=fundamental code
=additional code 
'''
import random
import sys

import time
from time import time

import pygame
pygame.init()


#Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

#Fonts
FONT100 = pygame.font.Font(None, 100)
FONT50 = pygame.font.Font(None, 50)

#GamePad and FPS
DISPLAYSURF = pygame.display.set_mode((800, 700))
FPSCLOCK = pygame.time.Clock()
FPS = 60

##GameProcedure
def main():
    ##Title
    draw_title()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ingame()

            #Check Terminate
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.QUIT:
                terminate()
                

##Ingame
def ingame():
    DISPLAYSURF.fill(BLACK)


    #Game Data
    running = True

    bullets = [  ]
    bulletRadius = 10
    
    playerLocation_x = 400
    playerLocation_y = 350
    playerRadius = 20

    beforeTime= time()
    generateInterval = 3
    
    command = [0, 0, 0, 0]

    
    #Generate Initial Bullets
    for times in range(4):
        bulletLocation_x = random.randrange(200, 601)
        bulletLocation_y = random.randrange(200, 601)
        bulletSpeed_x = random.randrange(-5, 6)
        bulletSpeed_y = random.randrange(-5, 6)
                
        if bulletSpeed_x == bulletSpeed_y == 0:
            bulletSpeed_x = random.randrange(1, 3)
            bulletSpeed_y = random.randrange(-7, -2)
                    
        bullet = [[bulletLocation_x, bulletLocation_y], [bulletSpeed_x, bulletSpeed_y]]
        bullets.append(bullet)

    while running:
        #Generate Bullets (per generateInterval)
        if time() - beforeTime >= generateInterval:
            for times in range(16):
                bulletLocation_x = random.randrange(200, 601)
                bulletLocation_y = random.randrange(200, 601)
                bulletSpeed_x = random.randrange(-5, 6)
                bulletSpeed_y = random.randrange(-5, 6)
                
                if bulletSpeed_x == bulletSpeed_y == 0:
                    bulletSpeed_x = random.randrange(1, 3)
                    bulletSpeed_y = random.randrange(-7, -2)
                    
                bullet = [[bulletLocation_x, bulletLocation_y], [bulletSpeed_x, bulletSpeed_y]]
                bullets.append(bullet)
                
                beforeTime = time()


        #Draw Bullets
        for bullet in bullets:
            '''
            bullet = [[bulletLocation_x, bulletLocation_y], [bulletSpeed_x, bulletSpeed_y]]
            
            bullet[0][0] == bulletLocation_x
            bullet[0][1] == bulletLocation_y
            bullet[1][0] == bulletSpeed_x
            bullet[1][1] == bulletSpeed_y
            '''
            pygame.draw.circle(DISPLAYSURF, BLACK, (bullet[0][0], bullet[0][1]), bulletRadius)
        
            bullet[0][0] += bullet[1][0]
            bullet[0][1] += bullet[1][1]
        
            if bullet[0][0] >= 800 or bullet[0][0] <= 0:
                bullet[0][0] = random.randrange(100, 701)
            if bullet[0][1] >= 700 or bullet[0][1] <= 0:
                bullet[0][1] = random.randrange(100, 601)
            
            pygame.draw.circle(DISPLAYSURF, RED, (bullet[0][0], bullet[0][1]), bulletRadius)


        #Check Command
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    command[0] = 0
                if event.key == pygame.K_LEFT:
                    command[1]=0
                if event.key == pygame.K_DOWN:
                    command[2] = 0
                if event.key == pygame.K_UP:
                    command[3] = 0
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    command[0] = 1
                if event.key == pygame.K_LEFT:
                    command[1] = 1
                if event.key == pygame.K_DOWN:
                    command[2] = 1
                if event.key == pygame.K_UP:
                    command[3] = 1

            #Check Terminate 
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.QUIT:
                terminate()


        #Draw Player
        if command[0] == 1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_x += 5
            pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
        if command[1] == 1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_x -= 5
            pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
        if command[2] == 1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_y += 5
            pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
        if command[3] == 1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_y -= 5
            pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)

        if playerLocation_x > 780:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_x = 780
        if playerLocation_x < 20:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_x = 20
        if playerLocation_y > 680:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_y = 680
        if playerLocation_y < 20:
            pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
            playerLocation_y = 20

        pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)


        pygame.display.update()

        #Check Collision
        for bullet in bullets:
            bulletLocation_x = bullet[0][0]
            bulletLocation_y = bullet[0][1]
            for n in range(-10, 11):
                for m in range(-20, 21):
                    if bulletLocation_x + n == playerLocation_x + m and bulletLocation_y + n == playerLocation_y + m:    
                        running = False

        
        FPSCLOCK.tick(FPS)


    ##Game Over
    draw_game_over(bullets)
    
    #Check Terminate
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                terminate()
             if event.type == pygame.QUIT:
                terminate()
    
def draw_title():
    AVOIDIT = FONT100.render('AVOID IT', True, WHITE)
    PRESSTOSTART = FONT50.render('[PRESS SPACEBAR TO START]', True, WHITE)

    DISPLAYSURF.fill(BLACK)
    pygame.draw.circle(DISPLAYSURF, WHITE, (445, 540), 80)
    pygame.draw.circle(DISPLAYSURF, RED, (225, 480), 40)
    pygame.draw.circle(DISPLAYSURF, RED, (545, 610), 40)
    DISPLAYSURF.blit(AVOIDIT, (275, 150))
    DISPLAYSURF.blit(PRESSTOSTART, (150, 350))

    pygame.display.update()

def draw_game_over(bullets):
    DISPLAYSURF.fill(BLACK)

    GAMEOVER = FONT100.render('GAME OVER', True, WHITE)
    SCORE = FONT50.render('YOUR SCORE: {} BULLETS'.format(len(bullets)), True, WHITE)
    DISPLAYSURF.blit(GAMEOVER, (200, 250))
    DISPLAYSURF.blit(SCORE, (200, 150))

    pygame.display.update()



def terminate():
    pygame.quit()
    sys.exit()
    






if __name__=="__main__":
    main()
