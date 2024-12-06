import pygame

#import your controller
from src.controller import Controller
def main():
    pygame.init()
    the_controller=Controller()
    the_controller.mainloop()
if __name__ == '__main__':
    main()
