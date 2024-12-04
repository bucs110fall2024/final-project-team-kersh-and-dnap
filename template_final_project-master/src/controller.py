import pygame
from src.world import World
from src.player import Player
class Controller:
  
  def __init__(self):
    pygame.init()
    self.sprites = pygame.sprite.Group()
    self.max_sprites = 20
    self.active =True
    self.gamestate= "menu"
    
  def mainloop(self):
    """This loop transitions between game states"""

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
    """ The menu """
    background = pygame.Surface((800,600))
    background.fill((135, 206, 235))

    screen.blit(background, (0, 0))  # Draw background on screen
    pygame.display.flip()  # Updat

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.active = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          self.gamestate = "game"
        elif event.key == pygame.K_ESCAPE:
          self.active = False
      #event loop

      #update data

      #redraw
      
  def gameloop(self, screen):
   the_game=World()
   the_game.run()
   self.gamestate = "gameover"
      
  def gameoverloop(self, screen):
    background = pygame.Surface((800,600))
    background.fill((200, 0, 0))

    screen.blit(background, (0, 0))  # Draw background on screen
    pygame.display.flip()  # Update display

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.active = False
      elif event.type == pygame.KEYDOWN:
        if event.type == pygame.K_RETURN:# return to game
          self.gamestate = "game"
        elif event.type == pygame.K_ESCAPE: # press esape to quit
          self.gamestate = "menu"
     