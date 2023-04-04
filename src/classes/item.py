import managers.itemManager as itemManager
import enums.itemType as itemType


class Item():

    # name == 아이템 이름
    # description == 아이템 설명
    # type == 아이템 유형
    def __init__(self, id: int, name: str, description: list, type: itemType.ItemType):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        itemManager.itemList.append(self)
