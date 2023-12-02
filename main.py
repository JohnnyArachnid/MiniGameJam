import pygame
import env_vars
from heatbar import HeatBar
from level import Level
import sprites

# pygame init
pygame.init()
screen = pygame.display.set_mode([env_vars.SCREEN_WIDTH, env_vars.SCREEN_HEIGHT])

clock = pygame.time.Clock()
FPS = 60

# Run until the user asks to quit
running = True

level = Level()
level.load_level('level1.txt')
level.draw(screen, 0, 0)

heatbar = pygame.sprite.GroupSingle()
heatbar.add(HeatBar())

tutorial = True
tutorialScreen = pygame.sprite.GroupSingle()
tutorialScreen.add(sprites.TutorialScreen((0, 0, 512, 288)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            tutorial = False
            if event.key == pygame.K_ESCAPE:
                running = False

    if not tutorial:
        level.player.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            level.player.move_left()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            level.player.move_right()
            pass
        if key[pygame.K_UP] or key[pygame.K_w]:
            level.player.move_up()
            pass
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            level.player.move_down()
            pass


    if(not tutorial):
        screen.fill(env_vars.SURFACE_COLOR)
        level.all_sprites.draw(screen)
        level.player.draw(screen)
        heatbar.draw(screen)
        heatbar.update(screen)
    else:
        tutorialScreen.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# kończeie gry
pygame.quit()