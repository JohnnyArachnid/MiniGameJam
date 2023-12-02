import pygame
import sprites
import env_vars

MOVEMENT_TIME = 2000#ms - jego dupa nie rusza sie w 2sek ale chuj
MOVEMENT_TICKS = 60*MOVEMENT_TIME/1000

class Player:
    def __init__(self, level, position, actualX, actualY):
        self.level = level
        self.spriteGroup = pygame.sprite.GroupSingle()
        playerSprite = sprites.Player(position)
        self.spriteGroup.add(playerSprite)
        self.x = actualX
        self.y = actualY

        self.during_move = False
        self.endtime = -1
        self.last_move = None
        self.last_tick = 0

    def draw(self, screen):
        self.spriteGroup.draw(screen)

    def move(self, next_position):
        if(self.during_move):
            return
        
        if(self.level.level_map[self.y + next_position[1]][self.x + next_position[0]] != '1'):
            return
        
        self.during_move = True
        self.endtime = pygame.time.get_ticks() + MOVEMENT_TICKS
        self.last_move = next_position

        self.update()

    def update(self):
        t = pygame.time.get_ticks()
        deltaTime = t - self.last_tick
        
        if(deltaTime == 0):
            return
        
        self.last_tick = t
        if(self.during_move and pygame.time.get_ticks() < self.endtime):
            xInc = int(self.last_move[0] * 32 * (deltaTime/MOVEMENT_TICKS))
            yInc = int(self.last_move[1] * 32 * (deltaTime/MOVEMENT_TICKS))

            newX = self.x + self.last_move[0]
            if(newX > env_vars.XTILES / 2 - 1 and self.level.x_tiles - newX > env_vars.XTILES / 2 - 1):
                self.level.move_camera(-xInc, 0)
            else:
                self.spriteGroup.sprite.rect.x += xInc
            
            newY = self.y + self.last_move[1]
            if(newY > env_vars.YTILES / 2 and self.level.y_tiles - newY > env_vars.YTILES / 2):
                self.level.move_camera(0, -yInc)
            else:
                self.spriteGroup.sprite.rect.y += yInc

        elif(self.during_move):
            self.x += self.last_move[0]
            self.y += self.last_move[1]
            self.spriteGroup.sprite.rect.x = (self.x) * 32 + self.level.camera[0]
            self.spriteGroup.sprite.rect.y = (self.y) * 32 + self.level.camera[1]
            self.during_move = False

    def move_left(self):
        self.move((-1, 0))

    def move_right(self):
        self.move((1, 0))

    def move_up(self):
        self.move((0, -1))

    def move_down(self):
        self.move((0,1))


