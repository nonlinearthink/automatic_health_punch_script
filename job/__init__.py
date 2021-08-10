from config import Configuration
from datetime import datetime, date
from selenium import webdriver
import time
import traceback


def daka():
    # 获取当天的配置
    config = Configuration.getConfig()
    dayOfWeek = datetime.today().weekday()
    dayOfMonth = date.today().day
    config_today = config["rules"]["default"]
    if config["rules"]["custom"] != None:
        weekday = [
            "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
            "sunday"
        ]
        if config["rules"]["custom"]["week"] != None:
            config_today = config["rules"]["custom"]["week"][
                weekday[dayOfWeek]]
        if config["rules"]["custom"]["month"] != None:
            config_today = config["rules"]["custom"]["month"][dayOfMonth]
    print("生成每日的配置: ", config_today)
    # 开始执行脚本
    driver = webdriver.Chrome()
    driver.get(
        "http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fyqdj.zucc.edu.cn%2Ffeiyan_api%2Fh5%2Fhtml%2Fdaka%2Fdaka.html"
    )
    try:
        #找到登录框，输入账号密码
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(
            config["username"])
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            config["password"])
        time.sleep(2)
        #模拟点击登录
        driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[5]/div/input[1]').click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        #输入地区
        pag = driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input')
        driver.execute_script("arguments[0].removeAttribute('readonly')", pag)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input'
        ).send_keys(config_today["location"])
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[7]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[9]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[16]/div[2]/div/div/li[1]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        #模拟点击签到
        driver.find_element_by_partial_link_text('提交').click()
        time.sleep(2)
        print("签到成功")
    except Exception as e:
        print("签到失败")
        traceback.print_exc()
    finally:
        driver.quit()
