# 浙大城市学院钉钉健康打卡脚本

![](https://img.shields.io/badge/%E6%B5%99%E5%A4%A7%E5%9F%8E%E5%B8%82%E5%AD%A6%E9%99%A2%E9%92%89%E9%92%89%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1-v2.3-red)

## 历史版本

|版本号|仓库|
|-|-|
|v1.0|[jonesnow/automatic_health_punch_script](https://gitee.com/jonesnow/automatic_health_punch_script)|
|v2.3|[nonlinearthink/automatic_health_punch_script](https://github.com/nonlinearthink/automatic_health_punch_script)|

## 使用说明

目前提供两种方式，第一种是手动安装的方式，第二种是Docker安装。

Docker是我个人推荐安装方式，不过对于很多编程新手来说，手动安装虽然麻烦，但是可能更加亲切一些，所以我也保留了下来。

对于2.3之前的版本，在安装开始之前，请先编辑 `application.yml` 文件，根据自己的情况更改配置。2.3之后支持动态配置，可在之后修改 `application.yml` 文件。

### 手动安装
#### 1. 安装依赖

> 推荐使用 virtualenv 或者 conda 独立建环境，但是别忘了激活环境，当然默认的全局安装也行。

```sh
pip install -r requirements.txt
# 或者 pip3 install -r requirements.txt
```

#### 2. 下载 chromedriver

可以通过 chrome://version 查看chrome版本。chromedriver 的版本必须与你的 chorme 版本一致，小版本号应该没影响。

chromedriver 下载地址: [https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

下载解压后，将可执行文件 chromedriver 放到 Python 目录下的 Scripts 目录下，也可以添加环境变量到 Path 中。

> 推荐使用虚拟环境，然后把可执行文件放到 `venv/bin` 目录下。

#### 3. 后台运行

##### Linux & MacOS

```sh
nohup python3 main.py > daka.log 2>&1 &
# 可使用 ps -ef | grep python3 查询 pid 后删除
```

##### Windows

```powershell
pythonw test.py > daka.log
# 可使用 tasklist 查询进程号后删除
```

### Docker自动安装

Docker 为推荐安装方式，因为它更好管理和维护，且操作更简单。

#### 1. 制作 Docker 镜像

```
docker build -t nonlinearthink/automatic-health-punch-script:2.3 .
```

这一步可能需要科学上网，不然安装chrome的时候获取谷歌的验证服务可能会失败。

> 从2.3开始支持动态配置，所以不需要在更改配置后重新制作镜像，当然你也可以选择自己制作镜像。
>
> ```sh
> docker pull nonlinearthink/automatic-health-punch-script:2.3
> ```

#### 2. 运行容器

```sh
# 2.3之前
docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -ti -d nonlinearthink/automatic-health-punch-script:2.3

# 2.3之后
docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -v $(pwd)/application.yml:/application.yml -ti -d nonlinearthink/automatic-health-punch-script:2.3
```

#### 3. 修改application.yml（2.3以上）

详细内容见 application.yml 里面的说明
