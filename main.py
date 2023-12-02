import pygame
import env_vars
from level import Level

# pygame init
pygame.init()
screen = pygame.display.set_mode([512, 288])

clock = pygame.time.Clock()
FPS = 60

# Run until the user asks to quit
running = True

level = Level()
level.load_level('level1.txt')
level.draw(screen, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN\
           and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill(env_vars.SURFACE_COLOR)
    level.all_sprites.update()
    level.all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

# kończeie gry
pygame.quit()