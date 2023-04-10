import os

import pygame
from pygame.locals import *


import classes.adventure as adventure
import classes.house as house
import classes.config as config
import classes.lastscavenger as lastScavenger
import managers.itemManager as itemManager
import managers.situationManager as situationManager
import managers.ymlManager as ymlManager


# 메인 게임 화면에서 선택지 제공
'''def printGameMainChoice():
    print(" 1. 모험 시작")
    print(" 2. 주거지 이동")
    print(" 3. 게임 종료")
    # 입력값 받기
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
            printGameMainChoice()'''


# 메인 로직
if __name__ == "__main__":
    # 화면 정리
    os.system("cls")

    # 인스턴스 셋업
    # print(prefix, "게임을 구성합니다.")
    itemManager.set_up()
    situationManager.setUp()

    # yml 불러옴
    configYaml = ymlManager.load_yaml()
    config = config.Config(configYaml)

    instance = lastScavenger.LastScavenager(config.version)
    instance.on_execute()
