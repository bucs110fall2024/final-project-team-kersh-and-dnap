import pygame
pygame.init()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy, speed=1, img="pngkey.com-gaming-characters-png-1790042.png"):
        super().__init__()
        self.image = pygame.image.load(img) if img else pygame.Surface(40,40)
        self.image.fill(255, 0, 0)
        self.rect =self.image.get_rect()
        self.rect.x = x #Coordinates of the character
        self.rect.y = y #^^^^
        self.enemy=enemy
        self.speed = speed
        self.alive = True
       
    def update(self):
        """Moves the enemy left"""
        if self.alive is True:
            self.rect.x -= self.speed

    def die(self):
        """Kills and removes the enemy from screen"""
        self.alive = False
        self.kill() # removes enemy from screen