import sys
import time

import pygame
from pygame.locals import *

import enums.gamePhase as gamePhase
import classes.situation as situation

# 코드 영감: http://pygametutorials.wikidot.com/tutorials-basic
class LastScavenger():

    # 객체 초기화 될때
    def __init__(self, version: str):
        self.isRunning = True
        self.displaySurf = None
        self.gameFrameWidth = 800
        self.gameFrameHeight = 600
        self.colorWhite = (255, 255, 255)
        self.colorBlack = (0, 0, 0)
        self.fps = 30
        self.gameTitle = "Last Scavanger - " + version
        self.font = None
        self.clock = None
        self.phase = gamePhase.GamePhase.PHASE_1

    # 게임 초기화 시킬 때
    def on_init(self):
        pygame.init()

        # 폰트 설정
        self.font = pygame.font.SysFont("nanumgothic", 20)

        # 시간 설정
        self.clock = pygame.time.Clock()

        # 아이콘 설정
        logo = pygame.image.load("last-scavanger-main-gui-icon.png")
        pygame.display.set_icon(logo)

        # 창 제목 설정
        pygame.display.set_caption(self.gameTitle)
        self.displaySurf = pygame.display.set_mode((self.gameFrameWidth, self.gameFrameHeight))

        self.isRunning = True

    # 이벤트 감지할 때
    def on_event(self, event):
        if event.type == pygame.QUIT:
            #게임 종료
            self.isRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass


    # 반복 작업할 때
    def on_loop(self):
        self.clock.tick(self.fps)

        #메인 화면 일 때 버튼에 마우스 가져다가 대면 버튼 색깔 바꾸기
        if self.phase == gamePhase.GamePhase.PHASE_1:
            import managers.situationManager as situationManager
            main_screen_situation = situationManager.get_situation(0)
            if isinstance(main_screen_situation, situation.Situation):
                buttons = main_screen_situation.buttons
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        print(".", time.time())
                        button.draw_hover(self.displaySurf)

    # 그래픽 작업할 때
    def on_render(self):
        import managers.renderManager as renderManager
        renderManager.render_screen(self.phase, self)

        pygame.display.update()

    # 종료할 때
    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() is False:
            self.isRunning = False

        while self.isRunning:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()