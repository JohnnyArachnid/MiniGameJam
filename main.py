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

def run(tutorial):
    level = Level()
    level.load_level('level.txt')
    level.draw(screen, 0, 0)

    heatbar = pygame.sprite.GroupSingle()
    heatbar.add(HeatBar())

    tutorialScreen = pygame.sprite.GroupSingle()
    tutorialScreen.add(sprites.TutorialScreen((0, 0, 512, 288)))

    while True:
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

            for sprite in level.animated_sprites:
                sprite.update()
            
            level.animated_sprites.draw(screen)
            level.all_sprites.draw(screen)
            level.player.draw(screen)
            heatbar.draw(screen)

            if(level.player.finished):
                return False
            elif(level.player.inside_fire):
                heatbar.sprite.add_heat(1)
            elif(level.player.inside_ice):
                heatbar.sprite.remove_heat(1.5)
            else:
                heatbar.sprite.remove_heat(0.5)

            heatbar.update(screen)

            if heatbar.sprite.internal_heat <= 0:
                return True # powtarzamy nie kończymy
        else:
            tutorialScreen.draw(screen)

        pygame.display.flip()
        clock.tick(env_vars.FPS)

tutorial = True
while run(tutorial):
    #tutorial = False
    pass

# kończeie gry
pygame.quit()