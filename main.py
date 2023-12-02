import pygame
import env_vars
from heatbar import HeatBar
from level import Level
import sprites
import player

# pygame init
pygame.init()
screen = pygame.display.set_mode([env_vars.SCREEN_WIDTH, env_vars.SCREEN_HEIGHT])

clock = pygame.time.Clock()
FPS = 60


def run(tutorial):
    # Run until the user asks to quit
    running = True

    level = Level()
    level.load_level('level1.txt')
    level.draw(screen, 0, 0)

    heatbar = pygame.sprite.GroupSingle()
    heatbar.add(HeatBar())

    #tutorial = True
    tutorialScreen = pygame.sprite.GroupSingle()
    tutorialScreen.add(sprites.TutorialScreen((0, 0, 512, 288)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                tutorial = False
                if event.key == pygame.K_ESCAPE:
                    return False

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

            screen.fill(env_vars.SURFACE_COLOR)

            level.all_sprites.draw(screen)
            level.player.draw(screen)
            heatbar.draw(screen)
            heatbar.update(screen)

            if heatbar.sprite.internal_heat <= 0 or heatbar.sprite.internal_heat >= 400:
                return True
                """
                heatbar.sprite.internal_heat = 200
                level.camera = (0,0)
                level.player = player.Player(level, (level.spawn[0]*32, level.spawn[1]*32, 32, 32), level.spawn[0], level.spawn[1])
                level.all_sprites.draw(screen)
                """
        else:
            tutorialScreen.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

tutorial = True
while run(tutorial):
    tutorial = False

# kończeie gry
pygame.quit()