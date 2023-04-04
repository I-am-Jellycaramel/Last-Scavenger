import main

itemList = []


def get_item(number):
    for item in itemList:
        if item.id != number:
            continue
        return item


def set_up():
    # print(main.prefix, "아이템을 초기화합니다.")
    pass
