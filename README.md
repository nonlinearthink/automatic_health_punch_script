# 自动健康打卡脚本-使用说明

#### 安装selenium包

```
pip install selenium
```
#### 下载chromedriver驱动  https://npm.taobao.org/mirrors/chromedriver

找到符合自己浏览器版本的chromedriver驱动，下载解压后，将chromedriver.exe文件放到Python目录下的Scripts目录下，也可以添加环境变量到Path中；

#### Selenium脚本源码

```
# -*- coding: utf-8 -*-
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
  
myusername = "xxxxxxxx"#登录账号,学号
mypassword = "xxxxxx"#登录密码,身份证后6位
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
```
#### 添加Windows定时任务
1. 我的电脑>右键管理>(左侧栏)任务计划程序>Microsoft>Windows>(右侧栏)创建任务(详见百度)

2. 设置任务:

命名任务
![输入图片说明](https://images.gitee.com/uploads/images/2020/0225/135138_58c31adf_4859314.png "屏幕截图.png")
设置触发器
![输入图片说明](https://images.gitee.com/uploads/images/2020/0225/135154_efdceb40_4859314.png "屏幕截图.png")
设置操作
![输入图片说明](https://images.gitee.com/uploads/images/2020/0225/135207_c6a241c3_4859314.png "屏幕截图.png")

注意：该方法的前提是py后缀的脚本文件默认打开方式是python，可以先尝试一下，本人就是默认python打开，如果不行可以用下面方法设置默认打开方式：

1.win+R打开运行；

2.输入regedit，确定；

3.在打开的注册表中找到以下目录：

HKEY_CLASSES-ROOT->Python.file->shell->open->command

4.将该项的内容修改为：

“D:\Python\Python3.6.1\pythonw.exe” “D:\Python\Python3.6.1\Lib\idlelib\idle.pyw” -e “%1”
（将其中的路径修改为自己python的安装路径即可）