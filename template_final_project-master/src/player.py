import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img="XXXXXXXXXX.png"):
       super().__init__()
       #self.image = pygame.image.load(img)
       self.image = pygame.Surface((40,40))
       self.image.fill((255,255,0))
       self.rect =self.image.get_rect()
       self.rect.x = x #Coordinates of the character
       self.rect.y = y #^^^^
       self.health = 3
       self.speedX=0
       self.speedY=0 #upward movement(Jumping)
       self.standing=False #If the character is on the ground
       self.on_ground = False

    def update(self):
        """Update player's position based on speed"""
        self.rect.x += self.speedX #adds distance based on speed to coordinate
        self.rect.y += self.speedY
    
        if not self.on_ground:
            self.speedY+= 1
        else:
            self.speedY = 0
         #make sure player stays on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.on_ground = True

    def horizontal_move(self, dx):
        """Movement left or right"""
        self.speedX = dx

    def vertical_move(self):
        "Movement up. Only works when the player is on the ground."
        if self.standing:
            self.speedY= -15
            self.on_ground = False

    
