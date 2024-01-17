import random

import pygame
from pygame import*
pygame.init()
import time


FPS=40

#COLORS
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
MAGENTA=(255,0,255)
CYAN=(0,255,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
ORANGE=(255,127,39)

def init():
    global DISPLAYSURF, FPSCLOCK, font100, font50
    
    DISPLAYSURF=pygame.display.set_mode((800,700))
    FPSCLOCK=pygame.time.Clock()

    
    font100=pygame.font.Font(None,100)
    font50=pygame.font.Font(None,50)
    avoidit=font100.render('AVOID IT', True, WHITE)
    presstostart=font50.render('[PRESS SPACEBAR TO START]', True, WHITE)

    
    DISPLAYSURF.fill(BLACK)
    pygame.draw.circle(DISPLAYSURF, WHITE, (445,540), 80)
    pygame.draw.circle(DISPLAYSURF, RED, (225,480), 40)
    pygame.draw.circle(DISPLAYSURF, RED, (545,610), 40)
    DISPLAYSURF.blit(avoidit, (275,150))
    DISPLAYSURF.blit(presstostart, (150,350))
    
    
    while True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    ingame()
                
        pygame.display.update()



def ingame():
    DISPLAYSURF.fill(BLACK)
    run=True

    BULLETS=[]
    for n in range(4):
        bulx=random.randrange(200,601)
        buly=random.randrange(200,601)
        dx=random.randrange(-5,6)
        dy=random.randrange(-5,6)
        if dx==dy==0:
            dx=random.randrange(1,3)
            dy=random.randrange(-7,-2)
        commonbullet=[[bulx,buly], [dx,dy]]
        BULLETS.append(commonbullet)

    plaX=400
    plaY=350

    distance=((plaX-bulx)**2+(plaY-buly)**2)**0.5

    beforetime=time.time()
    command=[0,0,0,0]
    while run:
        if time.time()-beforetime>=1:
            for n in range(16):
                bulx=random.randrange(200,601)
                buly=random.randrange(200,601)
                dx=random.randrange(-5,6)
                dy=random.randrange(-5,6)
                if dx==dy==0:
                    dx=random.randrange(1,3)
                    dy=random.randrange(-7,-2)
                commonbullet=[[bulx,buly], [dx,dy]]
                BULLETS.append(commonbullet)
                beforetime=time.time()
        for bullet in BULLETS:
            pygame.draw.circle(DISPLAYSURF, BLACK, (bullet[0][0],bullet[0][1]), 10)
            bullet[0][0] +=bullet[1][0]
            bullet[0][1] +=bullet[1][1]
            if bulx>=800 or bulx<=0:
                bulx=random.randrange(100,701)
            if buly>=700 or buly<=0:
                buly=random.randrange(100,601)
            pygame.draw.circle(DISPLAYSURF, RED, (bullet[0][0],bullet[0][1]), 10)
            


        for event in pygame.event.get():
             if event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    command[0]=1
                    
                if event.key==K_LEFT:
                    command[1]=1
                    
                if event.key==K_DOWN:
                    command[2]=1
                    
                if event.key==K_UP:
                    command[3]=1

             if event.type==KEYUP:
                if event.key==K_RIGHT:
                    command[0]=0
                    
                if event.key==K_LEFT:
                    command[1]=0
                    
                if event.key==K_DOWN:
                    command[2]=0
                    
                if event.key==K_UP:
                    command[3]=0

        if command[0]==1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaX +=5
            pygame.draw.circle(DISPLAYSURF, WHITE, (plaX,plaY), 20)
            
        if command[1]==1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaX -=5
            pygame.draw.circle(DISPLAYSURF, WHITE, (plaX,plaY), 20)
            
        if command[2]==1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaY +=5
            pygame.draw.circle(DISPLAYSURF, WHITE, (plaX,plaY), 20)

        if command[3]==1:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaY -=5
            pygame.draw.circle(DISPLAYSURF, WHITE, (plaX,plaY), 20)


        if plaX>780:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaX=780
            
        if plaX<20:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaX=20
            
        if plaY>680:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaY=680
            
        if plaY<20:
            pygame.draw.circle(DISPLAYSURF, BLACK, (plaX,plaY), 20)
            plaY=20

        pygame.draw.circle(DISPLAYSURF, WHITE, (plaX,plaY), 20)

        pygame.display.update()
        
        for bullet in BULLETS:
            for n in range(-10,11):
                for m in range(-20,21):
                    if bullet[0][0]+n==plaX+m and bullet[0][1]+n==plaY+m:
                        run=False

        FPSCLOCK.tick(FPS)
            
    DISPLAYSURF.fill(BLACK)

    gameover=font100.render('GAME OVER', True, WHITE)
    score=font50.render('YOUR SCORE: %d BALLS'%len(BULLETS), True,WHITE)
    DISPLAYSURF.blit(gameover,(200,250))
    DISPLAYSURF.blit(score,(200,150))

    pygame.display.update()








if __name__=="__main__":
    init()
