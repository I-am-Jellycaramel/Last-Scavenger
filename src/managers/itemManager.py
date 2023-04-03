import main

itemList = []

def getItem(number):
    for item in itemList:
        if (item.id != number):
            continue
        return item
        

def setUp():
    #print(main.prefix, "아이템을 초기화합니다.")
    pass