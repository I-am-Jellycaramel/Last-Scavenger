import os
import time
import src.main as main

MOVING_TIME = 3


# 집으로 들어가기 위한 함수입니다.
def enter_house():
    print(main.config.prefix, "집으로 이동합니다.")

    # 이동 준비
    for i in range(0, MOVING_TIME):
        print(f"{MOVING_TIME - i}초 뒤 이동합니다.")
        time.sleep(1)

    # 집 설정
    house = House()
    print("  :: Last Scavanger :: 집에 입장했습니다.")


# 디스크에서 메모리로 집 진행도를 옮길 때 사용하기 위한 클래스입니다.
# 각 집의 진행 정도를 나타냅니다.
class House:

    # 디스크에서 정보를 가져옵니다.
    def __init__(self):
        pass

    # 집 진행 정도를 소개합니다
    def introduce(self):
        pass
