import pygame
from pygame.locals import *

import managers.situationManager as situationManager
import enums.gamePhase as gamePhase
import classes.lastscavenger as lastscavenger
import classes.situation as situation

def render_screen(phase: gamePhase.GamePhase, ls: lastscavenger.LastScavenger):
    match phase:
        case phase.PHASE_1:
            render_background(ls)

            #게임 제목 출력
            game_title = ls.font.render("Last Scavanger", 1, ls.colorWhite)
            ls.displaySurf.blit(game_title, (40, 300))

            #상황 가져오기
            main_screen_situation = situationManager.get_situation(0)
            if isinstance(main_screen_situation, situation.Situation):
                buttons = main_screen_situation.buttons
                for button in buttons:
                    button.draw(ls.displaySurf, ls.font)
        case _:
            pass

def render_background(ls: lastscavenger.LastScavenger):
    background = pygame.image.load("last-scavanger-game-main-screen.png")
    ls.displaySurf.blit(background, (0, 0))
