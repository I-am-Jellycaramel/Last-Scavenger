import classes.situation as situation
import enums.area as area
import classes.button as button
import classes.lastscavenger as lastscavenger_import

situationList = []


def get_situation(number):
    for s in situationList:
        if s.id == number:
            return s
        return None


def setUp(li: lastscavenger_import.LastScavenger):
    # print(main.prefix, "상황을 초기화합니다.")
    situation.Situation(
        0,
        "아무런 상황도 아님",
        [
            "아직 아무 일도 일어나지 않았습니다. 걱정하지 마세요."
        ],
        area.Area.ROAD_OF_HOME,
        [
            button.Button(li, "아무일도 없는 버튼", (0, 0, 0), (60, 60, 60), (235, 159, 239), 100, 200, 100, 100)
        ]
    )
    situation.Situation(
        1,
        "모험의 시작",
        [
            "당신은 한낱 잡무용 로봇일 뿐이지만, 가슴이 뜨거워짐을 느꼈습니다.",
            "물론 그렇게 느끼도록 프로그래밍 되어있었겠지만, 오늘도 쓸만한 자원을 모으러 이동해야합니다."
        ],
        area.Area.ROAD_OF_HOME,
        []
    )
