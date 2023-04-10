import sys

import pygame
from pygame.locals import *

import enums.gamePhase as gamePhase
import main 

# 코드 영감: http://pygametutorials.wikidot.com/tutorials-basic
class LastScavenager():

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
        self.font = pygame.font.SysFont("nanumgothic", 35)

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
            self.isRunning = False

    # 반복 작업할 때
    def on_loop(self):
        self.clock.tick(self.fps)

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