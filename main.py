import yaml
from config import Configuration
import schedule
from job import daka
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# 新功能调试函数
# def license_username():
#     print(Configuration.config['username'])


def restart():
    Configuration.readConfig()
    schedule.clear()
    # 新功能调试代码
    # schedule.every(1).seconds.do(license_username)
    schedule.every().day.at(Configuration.config["schedule"]).do(daka)


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        restart()


def main():
    # 监听 application.yml，当文件内容改变的时候重新加载配置
    observer = Observer()
    file_handler = FileHandler()
    observer.schedule(file_handler, 'application.yml', recursive=True)
    observer.start()
    # 主循环
    restart()
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
