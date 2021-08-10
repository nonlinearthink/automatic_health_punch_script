# 浙大城市学院钉钉健康打卡脚本

![](https://img.shields.io/badge/%E6%B5%99%E5%A4%A7%E5%9F%8E%E5%B8%82%E5%AD%A6%E9%99%A2%E9%92%89%E9%92%89%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1-v2.0-red)

## 历史版本

|版本号|仓库|
|-|-|
|v1.0|[jonesnow/automatic_health_punch_script](https://gitee.com/jonesnow/automatic_health_punch_script)|
|v2.0|[nonlinearthink/automatic_health_punch_script](https://gitee.com/nonlinearthink/automatic_health_punch_script)|

## 使用说明

目前提供两种方式，第一种是手动安装的方式，第二种是Docker安装。

### 手动安装
#### 安装依赖

> 推荐使用 virtualenv 或者 conda 独立建环境，但是别忘了激活环境，当然默认的全局安装也行。

```sh
pip install -r requirements.txt
# 或者 pip3 install -r requirements.txt
```

#### 下载 chromedriver

可以通过 chrome://version 查看chrome版本。chromedriver 的版本必须与你的 chorme 版本一致，小版本号应该没影响。

chromedriver 下载地址: [https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

下载解压后，将可执行文件 chromedriver 放到Python目录下的Scripts目录下，也可以添加环境变量到Path中。

> 推荐使用虚拟环境，然后把可执行文件放到 `venv/bin` 目录下。

#### 后台运行

##### Linux & MacOS

```sh
nohup python3 test.py > daka.log 2>&1 &
# 可使用 ps -ef | grep python3 查询 pid 后删除
```

##### Windows

```powershell
pythonw test.py > daka.log
# 可使用 tasklist 查询进程号后删除
```

### Docker自动安装

Docker 为推荐安装方式，因为它更好管理和维护，且操作更简单。
