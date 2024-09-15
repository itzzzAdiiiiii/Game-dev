import pygame
from pygame.locals import*
from time import*

pygame.init()
screen=pygame.display.set_mode((1000,800))
varX = 255
varY= 370
keys=[False,False,False,False]
rocket= pygame.image.load("rocket.png")
background=pygame.image.load("background.jpg")
while varY < 800:
    screen.blit(background,(0,0))
    screen.blit(rocket,(varX,varY))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False

    if keys[0]:
        if varY>0:
            varY-=7
    elif keys[1]:
        if varY<800:
            varY+=4
    elif keys[2]:
        if varX>0:
            varX-=4
    elif keys[3]:
        if varX<1000:
            varX+=4

    varY+=2
    sleep(0.05)