def findElementInDict(dict: dict, name: str):
    for (key, value) in dict.items():
        if (key != name):
            continue
        return value

