import pygame
import env_vars
import sprites

class Level:
    def __init__(self):
        self.level_path = None
        self.level_map = None
        self.all_sprites = pygame.sprite.Group()

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
                        self.all_sprites.add(sprites.Enemy(position))
                    
                    case _:
                        print('Nieznany znak w pliku mapy!')
                        exit(1)