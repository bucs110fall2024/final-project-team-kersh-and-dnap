import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy, speed=1, img="XXXXXX.png"):
        super().__init__()
        self.image = pygame.image.load(img)
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