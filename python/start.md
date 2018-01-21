# python 环境搭建

由于当前操作系统的差别，在安装 python 的时候，有许多不一样之处，请根据教程来做（我们只使用 python3.6 版本，因为 2.x 要亡了）

[windows](https://www.jianshu.com/p/7a0b52075f70)

[mac](https://www.python.org/downloads/mac-osx/) 选择 Latest Python 3 Release - Python 3.6.4 下载，点击安装。


# pycharm 的使用

## 下载安装

Pycharm 提供 社区版 与 专业版。专业版是要收费的，对于我们学习 Python 而言，使用免费的社区版已足够。
[点击下载](https://www.jetbrains.com/pycharm/download/)

## 新建项目

左侧导航栏选择 Pure Python ，右侧的 Location 选择项目的路径， Interpreter 通过下拉栏选择 Python版本 ，这里直接使用 Python 的安装路径即可，可能需要自己添加路径，点击小齿轮会出现 add local 字样，然后选择就行。

选择完成之后，点击 Create 按钮，进入界面。这时就可以创建文件了，步骤如下图所示

## 运行项目

在新建的 hello.py 文件中，写入 
```python
print("hello world")
```
点击 pycharm 右上角的绿色箭头，即可看到下方 黑色框(console) 中出现了 hello world 字样。