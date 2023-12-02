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

class Sprite2(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.image.set_colorkey(env_vars.COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, rect, fps):
        super().__init__()

        self.frames = []
        for img in images:
            self.frames.append(pygame.image.load(img).convert_alpha())

        self.image = self.frames[0]
        self.image.set_colorkey(env_vars.COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

        self.fps = fps
        self.last_tick = 0
        self.current_frame = 0

    def update(self):
        if(pygame.time.get_ticks() - self.last_tick > self.fps):
            self.last_tick = pygame.time.get_ticks()
            self.current_frame += 1
            self.image = self.frames[self.current_frame % len(self.frames)]
            self.image.set_colorkey(env_vars.COLOR)

# vvv tutaj 

class Path(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/sciezkaDefault.png', rect)

class Wall(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokSniegu1.png', rect)

class WallLeft(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogLewy1.png', rect)

class WallRight(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogPrawy1.png', rect)

class WallUp(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogGora1.png', rect)

class WallDown(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogDol1.png', rect)


PLAYER_ANIMATION_SPEED = 90
class PlayerDown(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/graczDefault.png',
            './Grafiki/Gotowe/graczDol1.png',
            './Grafiki/Gotowe/graczDol2.png',
        ], rect, PLAYER_ANIMATION_SPEED)

class PlayerUp(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/graczGora1.png',
            './Grafiki/Gotowe/graczGora2.png',
            './Grafiki/Gotowe/graczGora3.png',
        ], rect, PLAYER_ANIMATION_SPEED)

class PlayerLeft(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/graczLewo1.png',
            './Grafiki/Gotowe/graczLewo2.png',
        ], rect, PLAYER_ANIMATION_SPEED)

class PlayerRight(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/graczPrawo1.png',
            './Grafiki/Gotowe/graczPrawo2.png',
        ], rect, PLAYER_ANIMATION_SPEED)

class Enemy(Sprite):
    def __init__(self, rect):
        super().__init__(RED, rect)

class Water(Sprite):
    def __init__(self, rect):
        super().__init__(BLUE, rect)

class Exit(Sprite):
    def __init__(self, rect):
        super().__init__(GREEN, rect)
