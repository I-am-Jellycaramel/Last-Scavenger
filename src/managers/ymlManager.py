import os

import yaml


# yml 불러오기
def load_yaml():
    current_path = os.getcwd()
    with open(current_path[:-3] + "resource\\resource.yml") as yml:
        config = yaml.load(yml, Loader=yaml.FullLoader)
    return config
