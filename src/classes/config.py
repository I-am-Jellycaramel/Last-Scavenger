import managers.listManager as listManager

class Config():
    def __init__(self, config: dict):

        dict = listManager.findElementInDict(config, "default_Info")

        self.prefix = listManager.findElementInDict(dict, "prefix")
        self.version = listManager.findElementInDict(dict, "version")
        

    def setPrefix(self, prefix: str):
        self.prefix = prefix
    
    def setVersion(self, version: str):
        self.version = version
