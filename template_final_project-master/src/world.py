import pygame

from src.player import Player
from src.enemy import Enemy
from src.platform import Platform

class World:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        pygame.display.set_caption("Fun Platformer!")
        self.clock = pygame.time.Clock()
        self.playing = True

        #ADD SPRITE GROUPS
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player= Player(100, 300, img=None)
        self.all_sprites.add(self.player)

        ground= Platform(0,500,800,100)#x,y,width,height
        self.platforms.add(ground)
        self.all_sprites.add(ground)
        #ADD FLOATING PLATFORMS

        enemy = Enemy(200, 300, enemy=True, speed=1, img=None)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def run(self): 
        """Game loop"""
        while self.playing:
            self.events()
            self.update()
            self.draw()
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
        """XXXXXX"""
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
                else:
                    self.player.health-=1
                    if self.player.health <=0:
                        print("Game Over")
                        self.playing = False

    def draw(self): #makes background and puts sprites on the screen
        """Visualizes the background and sprites"""
        self.screen.fill((135, 206, 235)) #LIGHT BLUE
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

