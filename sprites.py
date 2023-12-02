import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0 ,0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

SPRITE_SIZE = (32, 32)
SPRITE_RECT = pygame.Rect(0, 0, 32, 32)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color):
        self.sprite = pygame.surface.Surface(SPRITE_SIZE)
        self.sprite.fill(color)
        self.sprite.set_colorkey(color)
        pygame.draw.rect(self.sprite, BLACK, SPRITE_RECT, 1)

# vvv tutaj 

Path = Sprite(WHITE)
Wall = Sprite(BLACK)
Player = Sprite(GRAY)
Enemy = Sprite(RED)
Water = Sprite(BLUE)
