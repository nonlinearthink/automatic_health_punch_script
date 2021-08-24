import yaml


class Configuration:

    config = {}

    @classmethod
    def readConfig(self):
        with open('application.yml', 'r', encoding='utf-8') as f:
            config = yaml.load(f.read(), Loader=yaml.Loader)
            # 处理 schedule 的格式问题
            schedule_type = type(config["schedule"])
            schedule_pattern = '%02d:%02d'
            if schedule_type == int:
                minutes = int(config["schedule"])
                config["schedule"] = schedule_pattern % (minutes / 60,
                                                         minutes % 60)
            elif schedule_type == str:
                (hh, mm) = config["schedule"].split(':')
                config["schedule"] = schedule_pattern % (int(hh), int(mm))
            else:
                raise Exception("非法配置")
            # 更新配置信息
            print("加载配置", config)
            Configuration.config = config
