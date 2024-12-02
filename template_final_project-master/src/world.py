import pygame

pygame.init()
from player import Player
from enemy import Enemy
from platform import Platform

class World:
    def __init__(self):
        pygame.init()
        self.screen = pygame. display.set_mode(800,600)
        pygame.display.set_caption("Fun Platformer!")

        #ADD SPRITE GROUPS
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player= Player(100, 300, img=None)
        self.all_sprites.add(Player)

        ground= Platform(0,500,800,100)#x,y,width,height
        self.platforms.add(ground)
        self.all_sprites.add(ground)
        #ADD FLOATING PLATFORMS

        enemy = Enemy(200, 300, enemy=True, speed=1, img=None)
        self.enemies.add(enemy)
        self.all_sprites.add(Enemy)

    def run(self):
        pass

    def events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

