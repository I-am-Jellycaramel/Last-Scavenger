import os
import time
import classes.situation as situation

MOVING_TIME = 5

def runAdventure():
    print("모험을 시작합니다. 모험을 준비해주세요.")

    #시작 준비
    for i in range(0, MOVING_TIME):
        print(f"{MOVING_TIME-i}초 뒤 시작합니다.")
        time.sleep(1)
    
# 하나의 탐험 자체를 기록합니다.
# 플레이어의 진행 정보, 각 모험별 점수 등을 기록해야합니다.
class Adventure():

    isRunning = True

    def __init__(
            self,
            previousSituation: situation.Situation, 
            nowSituation: situation.Situation
            ):
        self.previousSituation = previousSituation
        self.nowSituation = nowSituation
