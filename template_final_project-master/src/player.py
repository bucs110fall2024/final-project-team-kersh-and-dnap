import pygame

pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img="R.png"):
       super().__init__()
       self.image = pygame.image.load(img)
       self.rect =self.image.get_rect()
       self.rect.x = x #Coordinates of the character
       self.rect.y = y #^^^^
       self.health = 3
       self.lives = 3
       self.speedX=0
       self.speedY=0 #upward movement(Jumping)
       self.standing=True #If the character is on the ground

    def update(self):
        """Update player's position based on speed"""
        self.rect.x += self.speedX #adds distance based on speed to coordinate
        self.rect.y += self.speedY
        
    def apply_gravity(self):
        if not self.on_ground:
            self.speedY += self.gravity

    def horizontal_move(self, dx):
        """Movement left or right"""
        self.speedX = dx

    def vertical_move(self):
        "Movement up. Only works when the player is on the ground."
        if self.standing:
            self.speedY= -15

    
