import pygame
from src.world import World
from src.player import Player
class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fun Platformer!!")
    self.active =True
    self.gamestate= "menu"
    
  def mainloop(self):
    """This loop transitions between game states"""

    while self.active:
      if self.gamestate == "menu":
        self.menuloop()
      elif self.gamestate == "game":
        self.gameloop()
      elif self.gamestate == "gameover":
        self.gameoverloop()
  ### below are some sample loop states ###

  def menuloop(self):
    """ The menu """
    pygame.display.set_caption("Fun Platformer!! press enter")
    self.screen.fill((135, 206, 235)) #Light Blue
    font = pygame.font.Font(None, 36)
    text = font.render("Press Enter to play", True, (0,0,0))
    self.screen.blit(text, (300, 400))
    pygame.display.flip()  # Updat

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.active = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          print( "TO GAME")
          self.gamestate = "game"
        elif event.key == pygame.K_ESCAPE:
          self.active = False
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
   
   the_game=World(self.screen)
   self.gamestate = the_game.run()
      
  def gameoverloop(self):
   
    self.screen.fill((200,0,0))
    pygame.display.flip()  # Update display

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.active = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN: # press escape to quit
          self.gamestate = "menu"
     