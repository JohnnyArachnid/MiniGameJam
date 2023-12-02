import pygame
import env_vars

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0 ,0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

SPRITE_SIZE = (32, 32)
SPRITE_RECT = pygame.Rect(0, 0, 32, 32)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, rect):
        super().__init__()

        self.image = pygame.surface.Surface(SPRITE_SIZE)
        self.image.fill(env_vars.SURFACE_COLOR)
        self.image.set_colorkey(env_vars.COLOR)
        pygame.draw.rect(self.image, color, SPRITE_RECT)

        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

# vvv tutaj 

class Path(Sprite):
    def __init__(self, rect):
        super().__init__(WHITE, rect)

class Wall(Sprite):
    def __init__(self, rect):
        super().__init__(BLACK, rect)

class Player(Sprite):
    def __init__(self, rect):
        super().__init__(GRAY, rect)

class Enemy(Sprite):
    def __init__(self, rect):
        super().__init__(RED, rect)

class Water(Sprite):
    def __init__(self, rect):
        super().__init__(BLUE, rect)
