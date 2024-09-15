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
