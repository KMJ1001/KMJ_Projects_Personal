'''
Avoid_it_2023.py
-----------------
Avoid it | ver 3 (2023-2)
Written by KimMinJi
----------------
=increase code-readibility
-rename variables 
-delete useless codes 
-etc

=add functions
-terminate game 
-restart game 
-add how to paly 
-add invincible state 
-reinforce score system
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
GRAY = (50, 50, 50)
LIGHTGRAY = (150, 150, 150)

#Fonts
FONT100 = pygame.font.Font(None, 100)
FONT80 = pygame.font.Font(None, 80)
FONT50 = pygame.font.Font(None, 50)
FONT30 = pygame.font.Font(None, 30)

#GamePad and FPS
DISPLAYSURF = pygame.display.set_mode((800, 700))
FPSCLOCK = pygame.time.Clock()
FPS = 60


##GameProcedure
def main():
    global scoreboard, trial
    scoreboard = [ ]
    trial = 0
    
    ##Title
    draw_title()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    trial += 1
                    ingame()
                if event.key == pygame.K_RETURN:
                    draw_how_to_play()
                    
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
    playerSpeed = 5
    
    beforeTime = time() 
    generateInterval = 3

    generalState = False
    initialTime = time()
    invincibilitySpan = 5
    
    command = [0, 0, 0, 0]

    
    #Generate Initial Bullets
    for times in range(10):
        bulletLocation_x = random.randrange(0, 801)
        bulletLocation_y = random.randrange(0, 701)
        bulletSpeed_x = random.randrange(-5, 6)
        bulletSpeed_y = random.randrange(-5, 6)

        ##Deal With Strange Bullets
        #Pre-collided Bullet
        distance = ((playerLocation_x - bulletLocation_x)**2 + (playerLocation_y - bulletLocation_y)**2)**0.5
        if distance < 50:
            bulletSpeed_x = random.randrange(-5, 6)
            bulletSpeed_y = random.randrange(-5, 6)
        #Static Bullet
        if bulletSpeed_x == bulletSpeed_y == 0:
            bulletSpeed_x = random.randrange(-5, 6)
            bulletSpeed_y = random.randrange(-5, 6)
                    
        bullet = [[bulletLocation_x, bulletLocation_y], [bulletSpeed_x, bulletSpeed_y]]
        bullets.append(bullet)
    

    while running:
        #Generate Bullets (per generateInterval)
        if time() - beforeTime >= generateInterval:
            for times in range(4):
                bulletLocation_x = random.randrange(0, 801)
                bulletLocation_y = random.randrange(0, 701)
                bulletSpeed_x = random.randrange(-5, 6)
                bulletSpeed_y = random.randrange(-5, 6)

                #Deal With Strange Bullets
                #Pre-collided Bullet
                distance = ((playerLocation_x - bulletLocation_x)**2 + (playerLocation_y - bulletLocation_y)**2)**0.5
                if distance < 50:
                    bulletSpeed_x = random.randrange(-5, 6)
                    bulletSpeed_y = random.randrange(-5, 6)
                #Static Bullet
                if bulletSpeed_x == bulletSpeed_y == 0:
                    bulletSpeed_x = random.randrange(-5, 6)
                    bulletSpeed_y = random.randrange(-5, 6)
                
                    
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

        if generalState:
            #Draw Player in General State
            if command[0] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_x += playerSpeed
                pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
            if command[1] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_x -= playerSpeed
                pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
            if command[2] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_y += playerSpeed
                pygame.draw.circle(DISPLAYSURF, WHITE, (playerLocation_x, playerLocation_y), playerRadius)
            if command[3] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_y -= playerSpeed
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

                #Measure Distance Between Player & Bullet
                distance = ((playerLocation_x - bulletLocation_x)**2 + (playerLocation_y - bulletLocation_y)**2)**0.5
                if distance < 30:
                    running = False

                            
        else: #Invincible State, Do Not Check Collision
            #Draw Player in Invincible State
            if command[0] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_x += 5
                pygame.draw.circle(DISPLAYSURF, GREEN, (playerLocation_x, playerLocation_y), playerRadius)
            if command[1] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_x -= 5
                pygame.draw.circle(DISPLAYSURF, GREEN, (playerLocation_x, playerLocation_y), playerRadius)
            if command[2] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_y += 5
                pygame.draw.circle(DISPLAYSURF, GREEN, (playerLocation_x, playerLocation_y), playerRadius)
            if command[3] == 1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (playerLocation_x, playerLocation_y), playerRadius)
                playerLocation_y -= 5
                pygame.draw.circle(DISPLAYSURF, GREEN, (playerLocation_x, playerLocation_y), playerRadius)

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

            pygame.draw.circle(DISPLAYSURF, GREEN, (playerLocation_x, playerLocation_y), playerRadius)
            
            #Break Initial Invincibility State
            if time() - initialTime >= invincibilitySpan:
                generalState = True

            pygame.display.update()

        
        FPSCLOCK.tick(FPS)


    ##Game Over
    #Calculate Score
    numBullets = len(bullets)
    playTime = time() - initialTime
    playTime_modified = int(playTime*10)
    score = numBullets + playTime_modified
    
    draw_game_over(score)
    print_scoreboard(score, scoreboard)

    
def draw_title():
    DISPLAYSURF.fill(BLACK)
    
    AVOIDIT = FONT100.render('AVOID IT', True, WHITE)
    PRESSTOSTART = FONT50.render('[PRESS SPACEBAR TO START]', True, WHITE)
    HOWTOPLAY = FONT30.render('(PRESS ENTER FOR HOW TO PLAY)', True, LIGHTGRAY)

    pygame.draw.circle(DISPLAYSURF, WHITE, (445, 540), 80)
    pygame.draw.circle(DISPLAYSURF, RED, (225, 480), 40)
    pygame.draw.circle(DISPLAYSURF, RED, (545, 610), 40)
    DISPLAYSURF.blit(AVOIDIT, (265, 150))
    DISPLAYSURF.blit(PRESSTOSTART, (150, 350))
    DISPLAYSURF.blit(HOWTOPLAY, (440, 670))

    pygame.display.update()

def draw_how_to_play():
    DISPLAYSURF.fill(BLACK)

    TITLE = FONT80.render('~How To Play~', True, WHITE)
    MOVE = FONT50.render('-Move White-cirlce Player by Arrow Keys.', True, WHITE)
    AVOID_1 = FONT50.render('-You just avoid Red-cirlce bullets', True, WHITE)
    AVOID_2 = FONT50.render('  as long as possible.', True, WHITE)
    INVINCIBLE_1 = FONT50.render('-If the game is started,', True, WHITE)
    INVINCIBLE_2 = FONT50.render(' you will be in invincibility for 5 sec.', True, WHITE)
    PLAYER = FONT50.render('-In invincible state, Player becomes green.', True, WHITE)
    PRESSTOSTART = FONT50.render('[PRESS SPACEBAR TO START]', True, WHITE)

    CREDIT = FONT30.render('MADE BY K.M.J', True, GRAY)

    pygame.draw.circle(DISPLAYSURF, WHITE, (80, 125), 20)
    pygame.draw.circle(DISPLAYSURF, RED, (245, 105), 10)
    pygame.draw.circle(DISPLAYSURF, RED, (265, 145), 10)
    pygame.draw.circle(DISPLAYSURF, GREEN, (450, 125), 20)
    DISPLAYSURF.blit(TITLE, (20, 10))
    DISPLAYSURF.blit(MOVE, (20, 200))
    DISPLAYSURF.blit(AVOID_1, (20, 250))
    DISPLAYSURF.blit(AVOID_2, (20, 300))
    DISPLAYSURF.blit(INVINCIBLE_1, (20, 350))
    DISPLAYSURF.blit(INVINCIBLE_2, (20, 400))
    DISPLAYSURF.blit(PLAYER, (20, 450))
    DISPLAYSURF.blit(PRESSTOSTART, (130, 550))

    DISPLAYSURF.blit(CREDIT, (15, 660))

    pygame.display.update()

def draw_game_over(score):
    DISPLAYSURF.fill(BLACK)

    GAMEOVER = FONT100.render('GAME OVER', True, WHITE)
    NOWSCORE = FONT50.render('YOUR SCORE: {}'.format(score), True, WHITE)
    PRESSTORESTART = FONT50.render('[PRESS SPACEBAR TO RESTART]', True, WHITE)
    HOWTOPLAY = FONT30.render('(PRESS ENTER FOR HOW TO PLAY)', True, LIGHTGRAY)
    
    DISPLAYSURF.blit(GAMEOVER, (200, 150))
    DISPLAYSURF.blit(NOWSCORE, (250, 255))
    DISPLAYSURF.blit(PRESSTORESTART, (130, 350))
    DISPLAYSURF.blit(HOWTOPLAY, (440, 670))
    
    pygame.display.update()


def print_scoreboard(score, scoreboard):
    #Update Trial & Scoreboard
    scoreboard.append(score)
    scoreboard.sort(reverse=True)

    #Deal With Overlapped Score
    setScoreboard = set(scoreboard)
    scoreboard = list(setScoreboard)
    
    print('==Scoreboard(trial: {})=='.format(trial))
    for i in range(len(scoreboard)):
            print('{}. {}'.format(i + 1, scoreboard[i]))


def terminate():
    pygame.quit()
    sys.exit()
    






if __name__=="__main__":
    main()
