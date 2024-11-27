import pygame
pygame.init()
class Platform():
    def __init__(self, x, y, width, height):
        self.image= pygame.Surface(width, height)
        self.image.fill(0,255,0)
        while True: 
            self.image.get_rect().x +=1


