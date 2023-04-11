from typing import List


import classes.button as button
import enums.area as area
import managers.situationManager as situationManager

class Situation:
    def __init__(self, id: int, name: str, description: List[str], area: area.Area, buttons: List[button.Button]):
        self.id = id
        self.name = name
        self.description = description
        self.area = area
        self.buttons = buttons

        situationManager.situationList.append(self)
