import os
import sys

import pygame
from pygame.locals import *

import classes.adventure as adventure
import classes.house as house
import classes.config as config
import managers.itemManager as itemManager
import managers.situationManager as situationManager
import managers.ymlManager as ymlManager
import managers.listManager as listManager

#코드 영감: http://pygametutorials.wikidot.com/tutorials-basic
class LastScavanager():
    
    #객체 초기화 될때
    def __init__(self):
        self.isRunning = True
        self.displaySurf = None
        self.gameFrameWidth = 800
        self.gameFrameHeight = 600
        self.colorWhite = (255, 255, 255)
        self.colorBlack = (0, 0, 0)
        self.fps = 30
        self.gameTitle = "Last Scavanger - " + config.version
        self.font = None
        self.clock = None
    
    #게임 초기화 시킬 때
    def onInit(self):
        pygame.init()

        #폰트 설정
        self.font = pygame.font.SysFont("nanumgothic", 35)

        #시간 설정
        self.clock = pygame.time.Clock()

        #아이콘 설정
        logo = pygame.image.load("last-scavanger-main-gui-icon.png")
        pygame.display.set_icon(logo)

        #창 제목 설정
        pygame.display.set_caption(self.gameTitle)
        self.displaySurf = pygame.display.set_mode((self.gameFrameWidth, self.gameFrameHeight))
        
        self.isRunning = True

    #이벤트 감지할 때
    def onEvent(self, event):
        if (event.type == pygame.QUIT):
            self.isRunning = False
    
    #반복 작업할 때
    def onLoop(self):
        self.clock.tick(self.fps)

    #그래픽 작업할 때
    def onRender(self):
        testImage = self.font.render("테스트 내용입니다. test", 1, self.colorWhite)
        testImageRect = testImage.get_rect()
        testImageRect.center = (self.gameFrameWidth/2, self.gameFrameHeight/2)

        background = pygame.image.load("last-scavanger-game-main-screen.png")

        self.displaySurf.blit(background, (0, 0))
        self.displaySurf.blit(testImage, testImageRect)

        pygame.display.update()

    #종료할 때
    def onCleanup(self):
        pygame.quit()
        sys.exit()

    def onExecute(self):
        if self.onInit() is False:
            self.isRunning = False

        while self.isRunning:
            for event in pygame.event.get():
                self.onEvent(event)

            self.onLoop()
            self.onRender()

        self.onCleanup()


    #메인 화면 문구
    #print("="*40)
    #print("  Last Scavanger")
    #print("="*40)

    #printGameMainChoice()
    
#메인 게임 화면에서 선택지 제공
def printGameMainChoice():
    print(" 1. 모험 시작")
    print(" 2. 주거지 이동")
    print(" 3. 게임 종료")
    #입력값 받기
    choice = input("선택해주세요: ")
    match choice:
        case "1":
            os.system("cls")
            print("모험 시작을 선택했습니다!")
            adventure.runAdventure()
        case "2":
            os.system("cls")
            print("주거지 이동을 선택했습니다.")
            house.enterHouse()
        case "3":
            os.system("cls")
            print("게임 종료를 선택했습니다.")
        case _:
            os.system("cls")
            print("올바르지 않은 값을 입력했습니다: ", choice)
            print("제대로 된 값을 입력해주세요. ")
            printGameMainChoice()

#메인 로직
if __name__ == "__main__":
    #화면 정리
    os.system("cls")

    #인스턴스 셋업
    #print(prefix, "게임을 구성합니다.")
    itemManager.setUp()
    situationManager.setUp()

    #yml 불러옴
    configYaml = ymlManager.loadYaml()
    config = config.Config(configYaml)

    #게임 실행
    lastScavanger = LastScavanager()
    lastScavanger.onExecute()