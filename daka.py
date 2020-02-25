# -*- coding: utf-8 -*-
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  
myusername = "xxxxxxxx"#登录账号
mypassword = "xxxxxx"#登录密码
localtion = "xxx xxx xxx"#所在地区，例："广东省 汕头市 潮南区"
  
driver = webdriver.Chrome() #模拟浏览器打开网站
driver.get("http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fyqdj.zucc.edu.cn%2Ffeiyan_api%2Fh5%2Fhtml%2Fdaka%2Fdaka.html")
#driver.maximize_window() #将窗口最大化


try:
 #找到登录框，输入账号密码
 driver.find_element_by_xpath('//*[@id="username"]').send_keys(myusername)
 driver.find_element_by_xpath('//*[@id="password"]').send_keys(mypassword)
 time.sleep(2)  
  
 #模拟点击登录
 driver.find_element_by_xpath('//*[@id="main"]/div/div/div[5]/div/input[1]').click()
 time.sleep(2)
except:
  print("签到失败")
print("*")
windows = driver.window_handles
driver.switch_to.window(windows[-1])
print("**") 
try:
 #输入地区
 pag=driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input')
 driver.execute_script("arguments[0].removeAttribute('readonly')",pag)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input').send_keys(localtion)
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[3]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[8]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[10]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label/div[2]/div').click()
 time.sleep(2)
 driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[1]/label/div[2]/div').click()
 time.sleep(2)
 #模拟点击签到
 driver.find_element_by_partial_link_text('提交').click()
 time.sleep(2)
 print("签到成功")

except Exception as e:
    traceback.print_exc()

driver.quit#退出驱动