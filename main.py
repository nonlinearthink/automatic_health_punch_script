import yaml
from config import Configuration
import schedule
from job import daka


def main():
    config = Configuration.getConfig()
    total = int(config["schedule"])
    try:
        schedule.every().day.at(config["schedule"]).do(daka)
    except Exception as e:
        hh = total / 60
        mm = total % 60
        pattern = r'%02d:%02d'
        config["schedule"] = pattern % (hh, mm)
        schedule.every().day.at(config["schedule"]).do(daka)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
