import yaml

class Configuration:

    @classmethod
    def getConfig(self):
        with open('application.yml', 'r', encoding='utf-8') as f:
            config = yaml.load(f.read(), Loader=yaml.Loader)
            print("加载配置", config)
            return config
