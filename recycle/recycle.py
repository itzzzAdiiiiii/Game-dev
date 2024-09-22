import pygame,random,time
from pygames.locals import*
pygame.init()
pygame.set_caption("recycle")
screen = pygame.display.set_mode(1000,800)
#recyclable sprites
class recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(18,30))
        self.rect = self.image.get_rect()
#non recyclable sprites
class non_recycleable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load("trash bag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(18,30))
        self.rect = self.image.get_rect()
#trash can
class trash_can(pygame.sprite.Sprite):
    def __init__(self,img):
        self.image = pygame.image.load("trash can.png").convert_alpha()
        selflimage = pygame.transform.scale(self.image,(25,40))
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
    item.rect.X = random.randrange(1000)
    item.rect.y = random.randrange(800)
    rg.add(item)
    all.add(item)
