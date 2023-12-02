import pygame
import env_vars

class HeatBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('./Grafiki/Gotowe/pasek_upojenia.png').convert_alpha(), (400, 33))
        self.image.set_colorkey(env_vars.COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = 56
        self.rect.y = 238

    def update(self):
        pass