import pygame

pygame.init()
class Controller:
  
  def __init__(self):
    self.sprites = pygame.sprite.Group()
    self.max_sprites = 20
    self.active =True
    self.gamestate= "menu"
    
  def mainloop(self):
    #select state loop

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('MARIO!')

    while self.active is True:
      if self.gamestate == "menu":
        self.menuloop(screen)
      elif self.gamestate == "game":
        self.gameloop(screen)
      elif self.gamestate == "gameover":
        self.gameoverloop(screen)
  ### below are some sample loop states ###

  def menuloop(self, screen):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self, screen):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw

