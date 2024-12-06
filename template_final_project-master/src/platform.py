import pygame

class Platform(pygame.sprite.Sprite):
    """
    Represents a platform in the game.

    Args:
        x (int): x-coordinate of the platform.
        y (int): y-coordinate of the platform.
        width (int): Width of the platform.
        height (int): Height of the platform.
    """
    def __init__(self, x, y, width, height):
        """Initializes the platform by position and size."""
        super().__init__()
        self.image= pygame.Surface((width, height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

       