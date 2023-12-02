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

class TutorialScreen(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/PoczatekGryCalosc.png', rect)


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



class Ognisko(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/ogniskoDefault.png',
            './Grafiki/Gotowe/ognisko3.png',
            './Grafiki/Gotowe/ognisko1.png',
            './Grafiki/Gotowe/ognisko4.png',
        ], rect, 240)

class Ice(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/Lod.png',
            './Grafiki/Gotowe/Lod1.png',
            './Grafiki/Gotowe/Lod2.png',
            './Grafiki/Gotowe/Lod3.png',
        ], rect, 240)

class Exit(AnimatedSprite):
    def __init__(self, rect):
        super().__init__([
            './Grafiki/Gotowe/Meta1.png',
            './Grafiki/Gotowe/Meta2.png',
            './Grafiki/Gotowe/Meta3.png',
            './Grafiki/Gotowe/Meta4.png',
        ], rect, 240)

class Santa(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/MikolajNaSniegu.png', rect)

class Elf1(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/ElfnaSniegu1.png', rect)

class Elf2(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/ElfnaSniegu2.png', rect)

class Elf3(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/ElfnaSniegu3.png', rect)

class LDolLewo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/LDolLewo.png', rect)

class LDolPrawo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/LDolPrawo1.png', rect)

class LGoraLewo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/LGoraLewo1.png', rect)

class LGoraPrawo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/LGoraPrawo1.png', rect)

class RogDolLewo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogDolLewo1.png', rect)

class RogDolPrawo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogDolPrawo1.png', rect)

class RogGoraLewo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogGoraLewo.png', rect)

class RogGoraPrawo(Sprite2):
    def __init__(self, rect):
        super().__init__('./Grafiki/Gotowe/blokRogGoraPrawo.png', rect)

