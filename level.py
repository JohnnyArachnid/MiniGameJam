import pygame
import env_vars
import sprites
from player import Player

class Level:
    def __init__(self):
        self.x_tiles = 0
        self.y_tiles = 0
        self.level_map = None
        self.all_sprites = pygame.sprite.Group()
        self.animated_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.camera = (0, 0)
        self.spawn = (0, 0)

    def load_level(self, level_name):
        with open(level_name, 'r') as f:
            level_map = f.read().replace(' ', '').splitlines()
            self.level_map = []
            for row in level_map:
                row_split = row.split(',')
                self.level_map.append(row_split)
        
        self.x_tiles = len(self.level_map[0])
        self.y_tiles = len(self.level_map)

    def actual_width(self):
        return self.x_tiles * 32
    
    def actual_height(self):
        return self.y_tiles * 32

    def move_camera(self, x, y):
        self.camera = (self.camera[0] + x, self.camera[1] + y)
        for sprite in self.all_sprites:
            sprite.rect.x += x
            sprite.rect.y += y
        for sprite in self.animated_sprites:
            sprite.rect.x += x
            sprite.rect.y += y

    def draw(self, screen, xStart, yStart):
        xUnit = screen.get_width() / env_vars.XTILES
        yUnit = screen.get_height() / env_vars.YTILES

        for x in range(self.x_tiles):
            for y in range(self.y_tiles):
                position = (xStart + x * xUnit, yStart + y * yUnit, xUnit, yUnit)
                #print(len(self.level_map[y]))
                match self.level_map[y][x]:
                    case '15':
                        self.all_sprites.add(sprites.Wall(position))
                    case '1':
                        self.all_sprites.add(sprites.Path(position))
                    case '2':
                        self.animated_sprites.add(sprites.Ice(position))
                    case '17':
                        self.all_sprites.add(sprites.WallLeft(position))
                    case '16':
                        self.all_sprites.add(sprites.WallRight(position))
                    case '13':
                        self.all_sprites.add(sprites.WallUp(position))
                    case '12':
                        self.all_sprites.add(sprites.WallDown(position))
                    case '22':
                        self.level_map[y][x] = '1'
                        self.all_sprites.add(sprites.Path(position))
                        self.spawn = (x, y)
                        self.player = Player(self, position, x, y)
                    case '3':
                        self.animated_sprites.add(sprites.Ognisko(position))
                    case '0':
                        self.animated_sprites.add(sprites.Exit(position))
                    case '4':
                        self.all_sprites.add(sprites.Santa(position))
                    case '5':
                        self.all_sprites.add(sprites.Elf1(position))
                    case '6':
                        self.all_sprites.add(sprites.Elf2(position))
                    case '7':
                        self.all_sprites.add(sprites.Elf3(position))
                    case '8':
                        self.all_sprites.add(sprites.LDolLewo(position))
                    case '9':
                        self.all_sprites.add(sprites.LDolPrawo(position))
                    case '10':
                        self.all_sprites.add(sprites.LGoraLewo(position))
                    case '11':
                        self.all_sprites.add(sprites.LGoraPrawo(position))
                    case '12':
                        self.all_sprites.add(sprites.RogDol(position))
                    case '13':
                        self.all_sprites.add(sprites.RogGora(position))
                    case '18':
                        self.all_sprites.add(sprites.RogDolLewo(position))
                    case '19':
                        self.all_sprites.add(sprites.RogDolPrawo(position))
                    case '20':
                        self.all_sprites.add(sprites.RogGoraLewo(position))
                    case '21':
                        self.all_sprites.add(sprites.RogGoraPrawo(position))
                    case other:
                        print(other)
                        print('Nieznany znak w pliku mapy!')
                        exit(1)