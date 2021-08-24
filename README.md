# 浙大城市学院钉钉健康打卡脚本

![](https://img.shields.io/badge/%E6%B5%99%E5%A4%A7%E5%9F%8E%E5%B8%82%E5%AD%A6%E9%99%A2%E9%92%89%E9%92%89%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1-v2.5-red)

## 历史版本

这个项目最早是我在 gitee 上偶然发现的一个项目，对他进行了一定程度上的魔改，也非常感谢原仓库作者。

|版本号|仓库|
|-|-|
|v1.0|[jonesnow/automatic_health_punch_script](https://gitee.com/jonesnow/automatic_health_punch_script)|
|v2.5|[nonlinearthink/automatic_health_punch_script](https://github.com/nonlinearthink/automatic_health_punch_script)|

## 使用说明

目前提供两种方式，第一种是Docker镜像运行，第二种是源代码运行。

个人推荐使用Docker，更加简单和易管理，不过对于很多没接触过Docker的人来说，可能因为陌生而比较抵触，所以我也提供了直接运行Python代码的方法。

### Docker镜像运行

1. 下载镜像

    ```sh
    docker pull nonlinearthink/automatic-health-punch-script:2.5
    ```

    如果下载的镜像出现了问题，可以自己制作：

    ```sh
    # 下载源代码仓库
    git clone https://github.com/nonlinearthink/automatic_health_punch_script

    # 打包镜像
    docker build -t nonlinearthink/automatic-health-punch-script:2.5 .
    ```

    > 自制脚本可能需要科学上网，不然安装chrome的时候获取谷歌的验证服务可能会失败。

2. 创建一个目录
3. 获取 application.yml

    进入上一步创建的目录，运行：

    ```sh
    wget https://raw.githubusercontent.com/nonlinearthink/automatic_health_punch_script/master/application.yml
    ```

    然后根据自己的情况，对 application.yml 做适当的修改，每一个配置项都写了注释，详细见 application.yml 。

    >`raw.githubusercontent.com` 这个地址并没有被墙，但因为很多电脑的默认DNS服务器都不会存域名，所以你可能访问不了，请 '修改hosts文件' 或者 '更换DNS服务器'。

4. 创建容器

    Linux & MacOS

    ```sh
    docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -v $(pwd)/application.yml:/application.yml -ti -d nonlinearthink/automatic-health-punch-script:2.5
    ```

    Windows

    ```powershell
    docker run --name automatic-health-punch-script -e TZ=Asia/Shanghai -v %cd%\application.yml:/application.yml -ti -d nonlinearthink/automatic-health-punch-script:2.5
    ```

5. 动态修改配置
   
   之后你只需要找到 第3步 创建的 `application.yml` 文件，修改里面的内容就可以了。
   
   因为我们在 第4步 的命令里面已经把这个配置文件挂载到了容器内部，所以你可以在外面修改配置，而不需要进入容器内部。

   修改配置可能需要几秒钟才能生效，请注意 `schdule` 不要设置得离当前时间太近，保持至少1-2分钟。

### 源代码运行

1. 安装依赖

    > 推荐使用 virtualenv 或者 conda 独立建环境，但是别忘了激活环境，当然默认的全局安装也行。

    ```sh
    pip install -r requirements.txt
    # 你也或许是 pip3 install -r requirements.txt
    ```

2. 下载 chromedriver

    可以通过 chrome://version 查看chrome版本。chromedriver 的版本必须与你的 chorme 版本一致，小版本号应该没影响。

    > chromedriver 下载地址: [https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

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
