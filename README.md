# 浙大城市学院钉钉健康打卡脚本

![](https://img.shields.io/badge/%E6%B5%99%E5%A4%A7%E5%9F%8E%E5%B8%82%E5%AD%A6%E9%99%A2%E9%92%89%E9%92%89%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1-v2.3-red)

## 历史版本

|版本号|仓库|
|-|-|
|v1.0|[jonesnow/automatic_health_punch_script](https://gitee.com/jonesnow/automatic_health_punch_script)|
|v2.3|[nonlinearthink/automatic_health_punch_script](https://github.com/nonlinearthink/automatic_health_punch_script)|

## 使用说明

目前提供两种方式，第一种是Docker镜像运行，第二种是源代码运行。

个人推荐使用Docker，更加简单和易管理，不过对于很多没接触过Docker的人来说，可能因为陌生而比较抵触，所以我也提供了直接运行Python代码的方法。

### Docker镜像运行

1. 下载镜像

    ```sh
    docker pull nonlinearthink/automatic-health-punch-script:2.3
    ```

    如果下载的镜像出现了问题，可以自己制作，脚本已经见 `dockerfile`。只需要在当前项目的根目录执行：

    ```sh
    docker build -t nonlinearthink/automatic-health-punch-script:2.3 .
    ```

    > 自制脚本可能需要科学上网，不然安装chrome的时候获取谷歌的验证服务可能会失败。


2. 创建一个目录
3. 获取 application.yml

    进入上一步创建的目录，运行：

    ```sh
    wget https://github.com/nonlinearthink/ automatic_health_punch_script/blob/master/application.yml
    ```

4. 创建容器

    Linux & MacOS

    ```sh
    docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -v $(pwd)/application.yml:/application.yml -ti -d nonlinearthink/automatic-health-punch-script:2.3
    ```

    Windows

    ```powershell
    docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -v %cd%\application.yml:/application.yml -ti -d nonlinearthink/automatic-health-punch-script:2.3
    ```

### 源代码运行

1. 安装依赖

    > 推荐使用 virtualenv 或者 conda 独立建环境，但是别忘了激活环境，当然默认的全局安装也行。

    ```sh
    pip install -r requirements.txt
    # 你也或许是 pip3 install -r requirements.txt
    ```

2. 下载 chromedriver

    可以通过 chrome://version 查看chrome版本。chromedriver 的版本必须与你的 chorme 版本一致，小版本号应该没影响。

    >chromedriver 下载地址: [https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

    下载解压后，将可执行文件 chromedriver 放到 Python 目录下的 Scripts 目录下，也可以添加环境变量到 Path 中。

    > 如果使用虚拟环境，也可以放到 `venv/bin` 目录下。

3. 修改 application.yml

    详细见 application.yml 里面的注释。

4. 后台运行

    Linux & MacOS

    ```sh
    nohup python3 main.py > daka.log 2>&1 &
    # 可使用 ps -ef | grep python3 查询 pid 后删除
    ```

    Windows

    ```powershell
    pythonw test.py > daka.log
    # 可使用 tasklist 查询进程号后删除
    ```
