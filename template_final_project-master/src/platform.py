import pygame
pygame.init()
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.ground= pygame.Surface(width, height)
        self.ground.fill(0,255,0)
        self.rect = self.ground.get_rect(topleft=(x, y))
       

