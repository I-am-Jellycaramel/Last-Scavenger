import src.managers.listManager as listManager


class Config:
    def __init__(self, config: dict):
        dict = listManager.find_element_in_dict(config, "default_Info")

        self.prefix = listManager.find_element_in_dict(dict, "prefix")
        self.version = listManager.find_element_in_dict(dict, "version")

    def set_prefix(self, prefix: str):
        self.prefix = prefix

    def set_version(self, version: str):
        self.version = version
