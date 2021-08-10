class Configuration:
    instance: dict = None

    @classmethod
    def createConfig(self, config_info):
        if Configuration.instance == None:
            print("加载配置: ", config_info)
            Configuration.instance = config_info
        else:
            print("请重新运行程序")

    @classmethod
    def getConfig(self):
        return Configuration.instance
