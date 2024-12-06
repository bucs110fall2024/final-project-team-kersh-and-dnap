import pygame
from src.world import World
from src.player import Player
class Controller:
  """
    Manages game states and transitions between them.

    Attributes:
        screen (pygame.Surface): The display surface for the game.
        active (bool): Indicates if the game is running.
        gamestate (str): Current state of the game ('menu', 'game', or 'gameover').
  """
  def __init__(self):
    """Initializes the game window and sets the initial state."""
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fun Platformer!!")
    self.active =True
    self.gamestate= "menu"
    
  def mainloop(self):
    """
    Controls the main game flow. Continuously 
    checks the current game state and runs the
    corresponding loop until the game is exited.
    """

    while self.active:
      if self.gamestate == "menu":
        self.menuloop()
      elif self.gamestate == "game":
        self.gameloop()
      elif self.gamestate == "gameover":
        self.gameoverloop()

  def menuloop(self):
    """
    Handles the menu state.
    Displays the menu screen
    and transitions to the game state
    when the Enter key is pressed.
    """
    pygame.display.set_caption("Fun Platformer!! Press enter")
    self.screen.fill((135, 206, 235)) #Light Blue
    font = pygame.font.Font(pygame.font.match_font("verdana"), 60)
    text = font.render("Welcome to JumpQuest!!", True, (0,0,0))
    instruction_text = font.render("Press Enter to Start!!", True, (0, 0, 0)) 
    font = pygame.font.Font(pygame.font.match_font("verdana"), 40)
    more_instruction=font.render("Keep Jumping on Red Don't Die!", True, (0, 0, 0)) 
    self.screen.blit(text, (10,25))
    self.screen.blit(instruction_text, (30, 125))
    self.screen.blit(more_instruction, (50, 300))

    yellow= pygame.Surface((100,100))
    yellow.fill((255,255,0))
    red=pygame.Surface((100,100))
    red.fill((255,0,0))

    self.screen.blit(yellow,(50, 450))
    self.screen.blit(red, (650,450))
                        
    pygame.display.flip()  # Update

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.active = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          print( "TO GAME")
          self.gamestate = "game"
        elif event.key == pygame.K_ESCAPE:
          self.active = False
  
  def gameloop(self):
   """
    Handles the main gameplay loop. 
    Runs the World class's game logic
    and updates the game state
    based on the result.
    """
   the_game=World(self.screen)
   self.gamestate = the_game.run()
   
  def gameoverloop(self):
    """
    Handles the game over state. Displays
    the game over screen and transitions back to the
    menu state when Enter is pressed.
    """
    if self.gamestate == 'gameover':
      self.screen.fill((200,0,0))
      font = pygame.font.Font(pygame.font.match_font("impact"), 100)
      text = font.render("GAME OVER", True, (0,0,0))
      font = pygame.font.Font(pygame.font.match_font("impact"), 75)
      instruction_text = font.render("Press Enter to Try Again!!", True, (0, 0, 0)) 
      self.screen.blit(text, (200,200))
      self.screen.blit(instruction_text, (0, 350))
      pygame.display.flip()  # Update display

      for event in pygame.event.get():
        if event.type== pygame.QUIT:
          self.active = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN: # press escape to quit
            self.gamestate = "menu"

   