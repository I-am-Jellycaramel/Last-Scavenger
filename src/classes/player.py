import src.classes.inventory as inventory


# 보관함, 상태 효과, 체력과 배고픔 수치를 나타내기 위한 클래스입니다.
class Player():

    # 초기값으로 설정합니다.
    # 체력: 100
    # 배고픔 수치: 100
    # 보관함: 비어있게
    # 상태 효과: 비어 있게
    def __init__(self):
        self.health = 100
        self.foodLevel = 100
        self.statusEffects = []
        self.inventory = inventory.Inventory()
