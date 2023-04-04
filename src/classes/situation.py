import src.enums.area as area
import src.managers.situationManager as situationManager


class Situation:
    def __init__(self, id: int, name: str, description: list, area: area.Area):
        self.id = id
        self.name = name
        self.description = description
        self.area = area
        situationManager.situationList.append(self)
