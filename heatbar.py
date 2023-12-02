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

        self.internal_heat = 200

        self.pointer = pygame.sprite.GroupSingle()
        self.pointer.add(Pointer((256, 236)))

    def update(self, screen):
        self.pointer.draw(screen)

    def add_heat(self, heat):
        self.internal_heat = min(self.internal_heat + heat, 390)
        self.pointer.sprite.rect.x = 56 + self.internal_heat
    
    def remove_heat(self, heat):
        self.internal_heat -= heat

        if(self.internal_heat < 0):
            return

        self.pointer.sprite.rect.x = 56 + self.internal_heat

class Pointer(pygame.sprite.Sprite):
    WIDTH = 5
    HEIGHT = 37
    def __init__(self, position):
        super().__init__()
        # surface
        self.image = pygame.image.load('./Grafiki/Gotowe/Wskaznik.png').convert_alpha()
        self.image.set_colorkey(env_vars.COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]