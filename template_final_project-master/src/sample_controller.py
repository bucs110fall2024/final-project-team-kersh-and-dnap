import pygame

pygame.init()
class Controller:
  
  def __init__(self):
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
    background = pygame.Surface((800,600))
    background.fill((135, 206, 235))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.active = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.gamestate = "game"
          elif event.key == pygame.K_ESCAPE:
            self.active = False
            
      #event loop

      #update data

      #redraw
      
  def gameloop(self, screen):
    background = pygame.Surface((800,600))
    background.fill((135, 206, 235))
    player= pygame.Rect
    while self.state == "game":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.active = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.gamestate = "gameover"
        
        
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self, screen):
    backgroud = pygame.Surface((800,600))
    backgroud.fill("red")
    #event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.active = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          self.gamestate = "game"
        
    
     

      #update data

      #redraw