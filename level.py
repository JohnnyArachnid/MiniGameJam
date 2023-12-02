import pygame
import env_vars
import sprites
from player import Player

SCIANA = '0'
SCIEZKA = '1'
WODA = '2'
SCIANA_LEWO = '3'
SCIANA_PRAWO = '4'
SCIANA_GORA = '5'
SCIANA_DOL = '6'

GRACZ = '7'
PRZECIWNIK = '8'
WYJSCIE = '9'

class Level:
    def __init__(self):
        self.level_path = None
        self.level_map = None
        self.all_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

    def load_level(self, level_name):
        levle_path = level_name
        with open(level_name, 'r') as f:
            level_map = f.read().replace(' ', '').splitlines()
            self.level_map = []
            for row in level_map:
                row_split = row.split(',')
                self.level_map.append(row_split)

    def draw(self, screen, xStart, yStart):
        xUnit = screen.get_width() / env_vars.XTILES
        yUnit = screen.get_height() / env_vars.YTILES

        for x in range(env_vars.XTILES):
            for y in range(env_vars.YTILES):
                position = (xStart + x * xUnit, yStart + y * yUnit, xUnit, yUnit)
                match self.level_map[y][x]:
                    case '0':
                        self.all_sprites.add(sprites.Wall(position))
                    case '1':
                        self.all_sprites.add(sprites.Path(position))
                    case '2':
                        self.all_sprites.add(sprites.Water(position))
                    case '3':
                        self.all_sprites.add(sprites.WallLeft(position))
                    case '4':
                        self.all_sprites.add(sprites.WallRight(position))
                    case '5':
                        self.all_sprites.add(sprites.WallUp(position))
                    case '6':
                        self.all_sprites.add(sprites.WallDown(position))
                    case '7':
                        self.level_map[y][x] = '1'
                        self.all_sprites.add(sprites.Path(position))
                        self.player = Player(self.level_map, position, x, y)
                    case '8':
                        self.all_sprites.add(sprites.Enemy(position))
                    case '9':
                        self.all_sprites.add(sprites.Exit(position))
                    case _:
                        print('Nieznany znak w pliku mapy!')
                        exit(1)