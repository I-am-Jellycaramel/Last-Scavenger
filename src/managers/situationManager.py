import src.classes.situation as situation
import src.enums.area as area
import src.main as main

situationList = []


def get_situation(number):
    for s in situationList:
        if s.id == number:
            return s
        return None


def setUp():
    # print(main.prefix, "상황을 초기화합니다.")
    situation.Situation(
        0,
        "아무런 상황도 아님",
        [
            "아직 아무 일도 일어나지 않았습니다. 걱정하지 마세요."
        ],
        area.Area.ROAD_OF_HOME
    )
    situation.Situation(
        1,
        "모험의 시작",
        [
            "당신은 한낱 잡무용 로봇일 뿐이지만, 가슴이 뜨거워짐을 느꼈습니다.",
            "물론 그렇게 느끼도록 프로그래밍 되어있었겠지만, 오늘도 쓸만한 자원을 모으러 이동해야합니다."
        ],
        area.Area.ROAD_OF_HOME
    )
