import pygame
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000,800))
#colors
teal = (0,128,128)
navy_blue = (11,11,69)
green = (57,255,20)
red = (255,0,0)

border = pygame.Rect(500,0,20,800)
lives_font = pygame.font.SysFont("Pixelify Sans",40)
win_font = pygame.font.SysFont("Pixelify Sans",70)
#variables
FPS=75
bspeed=6.5
sspeed=4
max_bullets=3
AS=pygame.image.load("alienship.png")
HS=pygame.image.load("humanship.png")
BG=pygame.transform.scale(pygame.image.load("sunset.jpg"),(1000,800))
BD=pygame.Rect(500,0,10,800)
ASH=13
HSH=7
class SS(pygame.sprite.Sprite):
    def __init__(self,image,angle,x,y):
        super().__init__()
        self.image=pygame.transform.rotate(pygame.transform.scale(image,(60,50)),angle)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def hx(self,s,pl):
        self.rect.x+=s
        if pl==1:
            if self.rect.left<=0 or self.rect.right>=BD.left:
                self.rect.move_ip(-s,0)
        if pl==2:
            if self.rect.right>=1000 or self.rect.left<=BD.right:
                self.rect.move_ip(-s,0)
    def vy(self,s):
        self.rect.move_ip(0,s)
        if self.rect.top<=0 or self.rect.bottom>=800:
            self.rect.move_ip(0,-s)
ALS=SS(AS,0,250,400)
HMS=SS(HS,90,750,400)
sprites=pygame.sprite.Group()
sprites.add(ALS)
sprites.add(HMS)
def sketch():
    screen.blit(BG,(0,0))
    pygame.draw.rect(screen,navy_blue,BD)
    AT= lives_font.render("health:"+str(ASH),1,green)
    HT= lives_font.render("health:"+str(HSH),1,green)
    screen.blit(AT,(20,20))
    screen.blit(HT,(875,20))
ALB = []
HMB = []
def bullet():
    for B in ALB:
        pygame.draw.rect(screen,teal,B)
        B.x+=bspeed
    for B in HMB:
        pygame.draw.rect(screen,red,B)
        B.x-=bspeed
ALH = pygame.USEREVENT+1
HMH = pygame.USEREVENT+2
def col():
    global ASH,HSH
    for B in ALB:
       if HMS.rect.colliderect(B):
           HSH-=1
           ALB.remove(B)
    for B in HMB:
       if ALS.rect.colliderect(B):
           ASH-=1
           HMB.remove(B)
    for B1 in ALB:
        for B2 in HMB:
            if B1.colliderect(B2):
                ALB.remove(B1)
                HMB.remove(B2)
clock=pygame.time.Clock()

def W(t):
    draw_text = win_font.render(t,1,navy_blue)
    screen.blit(draw_text,(400,500))
    pygame.display.update()
    pygame.time.delay(5000)
engine=True
while engine:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==QUIT:
            engine=False
        if event.type==KEYDOWN:
            if event.key==K_LCTRL:
                B=pygame.Rect(ALS.rect.x + ALS.rect.width, ALS.rect.y + ALS.rect.height//2 - 2,10,5)
                ALB.append(B)
            if event.key==K_RCTRL:
                B=pygame.Rect(HMS.rect.x + HMS.rect.width, HMS.rect.y + HMS.rect.height//2 - 2,10,5)
                HMB.append(B)

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        ALS.hx(-sspeed,1)
    if keys[K_d]:
        ALS.hx(sspeed,1)
    if keys[K_w]:
        ALS.vy(-sspeed)
    if keys[K_s]:
        ALS.vy(sspeed)
    if keys[K_LEFT]:
        HMS.hx(-sspeed,2)
    if keys[K_RIGHT]:
        HMS.hx(sspeed,2)
    if keys[K_UP]:
        HMS.vy(-sspeed)
    if keys[K_DOWN]:
        HMS.vy(sspeed)

    sketch()
    sprites.draw(screen)
    bullet()
    col()
    if ASH<=0:
        winner_text = "HUMANS WIN!!!"
        W(winner_text)
        engine = False
    if HSH<=0:
        winner_text = "aLiEnS WiN!!!"
        W(winner_text)
        engine = False
   
    pygame.display.update()
pygame.quit()

