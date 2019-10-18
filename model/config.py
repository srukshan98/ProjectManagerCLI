import json
import setting

class Config:
    path = ""
    vcs = {}
    def __init__(self, obj):
        self.path = obj['path']
        self.vcs = obj['vcs']
    def save(self):
        with open(setting.CONFIG_FILE, 'w') as config:
            json.dump({
                "path":self.path,
                "vcs":self.vcs
            }, config)
    @staticmethod
    def load():
        with open(setting.CONFIG_FILE) as f:
            conf = json.load(f)
        return Config(conf)