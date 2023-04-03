import yaml

#yml 불러오기
def loadYaml():
    with open("resource/resource.yml") as yml:
        config = yaml.load(yml, Loader=yaml.FullLoader)
    return config
