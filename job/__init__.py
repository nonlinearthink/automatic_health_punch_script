from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

from config import Configuration
from datetime import datetime, date
from selenium import webdriver
import time
import traceback


def daka():
    # 获取当天的配置
    config = Configuration.config
    dayOfWeek = datetime.today().weekday()
    dayOfMonth = date.today().day
    config_today = config["rules"]["default"]
    if config["rules"]["custom"] != None:
        weekday = [
            "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
            "sunday"
        ]
        if config["rules"]["custom"]["week"] != None and weekday[
                dayOfWeek] in config["rules"]["custom"]["week"]:
            config_today = config["rules"]["custom"]["week"][
                weekday[dayOfWeek]]
        if config["rules"]["custom"]["month"] != None and dayOfMonth in config[
                "rules"]["custom"]["month"]:
            config_today = config["rules"]["custom"]["month"][dayOfMonth]
    print("生成每日的配置: ", config_today)
    # 开始执行脚本
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
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
        print("登录成功")
        # 跳转
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # 自动定位
        pag = driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input')
        driver.execute_script("arguments[0].removeAttribute('readonly')", pag)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input'
        ).send_keys(config_today["location"])
        time.sleep(2)
        # 目前所在地
        pag = driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input')
        driver.execute_script("arguments[0].removeAttribute('readonly')", pag)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input'
        ).send_keys(config_today["destination"])
        time.sleep(2)
        # 近14天是否有与疫情中、高风险地区人员的接触史
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 近14天是否有与疑似、确诊人员的接触史?
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 近21天是否有中高风险地区旅居史，近14天是否有中高风险地区所在区旅居史？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 现是否处于医学观察状态？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[7]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 现是否处于居家隔离状态？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[9]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 现身体状况，是否存在发热体温、寒战、咳嗽、胸闷以及呼吸困难等症状？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 同住家属近14天是否有与疫情中、高风险地区人员的接触史？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 同住家属近14天是否有与疑似、确诊人员的接触史？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 同住家属近14天是否到过疫情中、高风险地区？
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 同住家属现是否处于医学观察状态?
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 今日申领学校所在地健康码的颜色?
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[16]/div[2]/div/div/li[1]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # 本人或家庭成员(包括其他亲密接触人员)是否有近28日入境或未来7日拟入境的情况?
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        #模拟点击提交
        driver.find_element_by_partial_link_text('提交').click()
        time.sleep(2)
        # 验证签到成功
        if(is_visible(driver,'//*[@class="modal-buttons "]/span') ):
            driver.find_element_by_xpath(
                '//*[@class="modal-buttons "]/span'
            ).click()
            print("签到成功")
        else:
            print("签到失败")
    except Exception as e:
        print("签到失败")
        traceback.print_exc()
    finally:
        driver.quit()

# 一直等待某元素可见，默认超时10秒
def is_visible(driver,locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False
