import pygame
from pygame.locals import *

import enums.gamePhase as gamePhase
import main as main


def render_screen(phase: gamePhase.GamePhase):
    match phase:
        case phase.PHASE_1:
            print(main.instance.path)
            background = pygame.image.load(main.instance.path + "last-scavanger-game-main-screen.png")
            game_title = main.instance.font.render("Last Scavanger", 1, main.instance.colorWhite)

            main.instance.displaySurf.blit(background, (0, 0))
            main.instance.displaySurf.blit(game_title, (40, 300))
        case _:
            pass
