import pygame,random
import time
from pygame.locals import*
pygame.init()
pygame.display.set_caption("recycle")
screen = pygame.display.set_mode((1000,800))
f = pygame.font.SysFont("Sixtyfour Convergence",45)
score = 0
text = f.render("score = "+str(score),True,"Blue")
#recyclable sprites
class recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(35,50))
        self.rect = self.image.get_rect()
#non recyclable sprites
class non_recycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trash bag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(35,50))
        self.rect = self.image.get_rect()
#trash can
class trash_can(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trash can.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,150))
        self.rect = self.image.get_rect()
#list of imagesfor the recycle class
recycles = ["coffee cup.png", "crate.png", "soda can.png", "water bottle.png"]
#sprite groups
rg = pygame.sprite.Group()
nrg = pygame.sprite.Group()
all = pygame.sprite.Group()
#drawing items on screen
for i in range(30):
    item = recycle(random.choice(recycles))
    #seting random position 
    item.rect.x = random.randrange(980)
    item.rect.y = random.randrange(780)
    rg.add(item)
    all.add(item)
for i in range(22):
    item = non_recycleable()
    item.rect.x = random.randrange(980)
    item.rect.y = random.randrange(780)   
    nrg.add(item)
    all.add(item)
trashcan = trash_can()
all.add(trashcan)
clock = pygame.time.Clock()
start = time.time()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    total = time.time()-start
    if total >= 30:
        if score >= 30:
            text = f.render("Good job!",(20,50),"blue")
        else:
            text = f.render("Game over",(20,50),"blue")
    else:
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:#up
            if trashcan.rect.y>0:
                trashcan.rect.y-=7
        if keys[pygame.K_DOWN]:#down
            if trashcan.rect.y<800:
                trashcan.rect.y+=7
        if keys[pygame.K_LEFT]:#left
            if trashcan.rect.x>0:
                trashcan.rect.x-=7
        if keys[pygame.K_RIGHT]:#right
            if trashcan.rect.x<1000:
                trashcan.rect.x+=7
        #checking the collision
        item_hit = pygame.sprite.spritecollide(trashcan,rg,True)
        trash_hit = pygame.sprite.spritecollide(trashcan,nrg,True)
        for i in item_hit:
            score = score+1
            text = f.render("score = "+str(score),True,"Blue")
        screen.blit(text,(20,50))
        all.draw(screen)
    pygame.display.update()
pygame.quit()
