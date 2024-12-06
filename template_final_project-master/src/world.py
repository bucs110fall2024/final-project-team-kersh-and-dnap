import pygame
import random

from src.player import Player
from src.enemy import Enemy
from src.platform import Platform

class World:
    
    """
    Manages the game world, including sprites and the game loop.

    Args:
        screen (Surface): The display surface.
    """
     
    def __init__(self, screen):
        """Sets up the game world and initializes objects."""
        pygame.init()
        self.screen = screen
        pygame.display.set_caption("Fun Platformer!")
        self.clock = pygame.time.Clock()
        self.playing = True
        self.bg_color = (135, 206, 235) 

        self.kills=0

        #ADD SPRITE GROUPS
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player= Player(100, 500)
        self.all_sprites.add(self.player)

        ground= Platform(0,500,800,100)#x,y,width,height
        self.platforms.add(ground)
        self.all_sprites.add(ground)
        #ADD FLOATING PLATFORMS
        
        enemy = Enemy(500, 465, enemy=True, speed=1)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)
        self.enemy_spawn_timer = 0

    def spawn_enemy(self):
        """Spawns an enemy"""
        enemy = Enemy(500, 465, enemy=True, speed=1)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def run(self): 
        """Game loop"""
        while self.playing:
            self.events()
            self.update()
            self.draw()

            self.enemy_spawn_timer += 1

            if self.enemy_spawn_timer > 120:
                self.spawn_enemy()
                self.enemy_spawn_timer=0
            
            self.clock.tick(60)

        if self.player.health <= 0:
            print("Game Over")
            return "gameover"
        
        return "menu"
    
    def events(self): #for each key event
        """Key events and Inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.horizontal_move(-5)
                elif event.key == pygame.K_RIGHT:
                    self.player.horizontal_move(5)
                elif event.key == pygame.K_UP:
                    self.player.vertical_move()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.player.horizontal_move(0)

    def update(self): #update and redraw screen 
        """ Updates Sprites and checks for collisions"""
        self.all_sprites.update()

        on_ground= pygame.sprite.spritecollide(self.player, self.platforms, False)
        if on_ground:
            self.player.standing=True
            self.player.on_ground = True
            self.player.rect.y = on_ground[0].rect.top - self.player.rect.height
        else:
            self.player.on_ground =False

        #ENEMY COLLSIONS
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.player, enemy):
                if self.player.rect.bottom <= enemy.rect.top + 10 and self.player.speedY > 0:
                    self.enemies.remove(enemy)
                    self.all_sprites.remove(enemy)
                    self.player.speedY= -10
                    self.kills += 1
                else:
                    self.player.health-=1
                    if self.player.health <=0:
                        print("Game Over")
                        self.playing = False

    def draw(self): #makes background and puts sprites on the screen
        """Visualizes the background and sprites"""
        self.screen.fill((self.bg_color)) #LIGHT BLUE
        self.all_sprites.draw(self.screen)

        
        font = pygame.font.Font(None, 36)  
        message = "Keep Jumping on Red!"
        text = font.render(message, True, (0, 0, 0))  # Black text
        self.screen.blit(text, (10, 10)) 

        kill_counter = font.render(f"Kills: {self.kills}",True,(0,0,0))
        self.screen.blit(kill_counter,(10,50))

        pygame.display.flip()

    