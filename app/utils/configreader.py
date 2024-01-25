import json

class ConfigReader:
    def __init__(self, path):
        with open(path, "r") as fp:
            self.load_config = json.load(fp)

    def get(self, key):
        return self.load_config[key]