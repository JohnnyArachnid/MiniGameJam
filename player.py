import pygame
import sprites

MOVEMENT_TIME = 2000#ms
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
        
        if(self.level[self.y + next_position[1]][self.x + next_position[0]] != '1'):
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
            self.spriteGroup.sprite.rect.x += int(self.last_move[0] * 32 * (deltaTime/MOVEMENT_TICKS))
            self.spriteGroup.sprite.rect.y += int(self.last_move[1] * 32 * (deltaTime/MOVEMENT_TICKS))

        elif(self.during_move):
            self.x += self.last_move[0]
            self.y += self.last_move[1]
            self.spriteGroup.sprite.rect.x = self.x * 32
            self.spriteGroup.sprite.rect.y = self.y * 32
            self.during_move = False

    def move_left(self):
        self.move((-1, 0))

    def move_right(self):
        self.move((1, 0))

    def move_up(self):
        self.move((0, -1))

    def move_down(self):
        self.move((0,1))


