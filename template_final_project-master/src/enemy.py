import pygame
pygame.init()
class Enemy(pygame.sprite.Sprite):

    """
    Represents an enemy in the game.

    Args:
        x (int): Starting x-coordinate.
        y (int): Starting y-coordinate.
        enemy (bool): Flag indicating it's an enemy (default True).
        speed (int): Movement speed (default 1).
    """

    def __init__(self, x, y, enemy=True, speed=1):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((255, 0, 0))
        self.rect =self.image.get_rect()
        self.rect.topleft= (x, y) #Coordinates of the character
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
        