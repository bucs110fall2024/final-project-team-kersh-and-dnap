import pygame

#import your controller
from src.controller import Controller
def main():
    pygame.init()
    the_controller=Controller()
    the_controller.mainloop()
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
