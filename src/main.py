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

#
# 상수
#
FPS = 30
GAME_FRAME_WIDTH = 800
GAME_FRAME_HEIGHT = 600
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

isRunning = True


#게임 시작
def runDefaultSetting():
    #화면 정리
    os.system("cls")

    #인스턴스 셋업
    #print(prefix, "게임을 구성합니다.")
    itemManager.setUp()
    situationManager.setUp()

    #yml 불러옴
    global config
    configYaml = ymlManager.loadYaml()
    config = config.Config(configYaml)

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
    runDefaultSetting()

    #pygame 초기화
    pygame.init()

    #창 제목 설정
    pygame.display.set_caption("Last Scavanger - ", config.version)
    #메인 디스플레이 설정
    displaySurf = pygame.display.set_mode((GAME_FRAME_WIDTH, GAME_FRAME_HEIGHT), 0, 32)
    #시간 설정
    clock = pygame.time.Clock()
    #폰트 설정
    font = pygame.font.SysFont("nanumgothic", 70)

    testImage = font.render("테스트 내용입니다. test", 1, COLOR_BLACK)
    testImageRect = testImage.get_rect()
    testImageRect.center = (GAME_FRAME_WIDTH/2, GAME_FRAME_HEIGHT/2)

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
                sys.exit()
        displaySurf.fill(COLOR_WHITE)
        displaySurf.blit(testImage, testImageRect)

        pygame.display.update()
        clock.tick(FPS)