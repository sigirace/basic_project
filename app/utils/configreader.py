import json

PATH_LOAD_CONFIG = "config/load_config.json"

class ConfigReader:
    def __init__(self):
        with open(PATH_LOAD_CONFIG, "r") as fp:
            self.load_config = json.load(fp)

    def get(self, key):
        return self.load_config[key]