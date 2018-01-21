# -*- coding: utf-8 -*-

"""
turtle 是一个可以画图的 python 扩展，运行下段代码，观察结果
更多的操作，查看 http://www.cnblogs.com/nowgood/p/turtle.html

需要自行画出的图形：
正方形
三角形
N边形
杨辉三角
蜂巢
"""


# 画一个五角星
import turtle

t = turtle.Turtle()

t.pencolor("yellow")
t.fillcolor("red")

t.begin_fill()
t.forward(20)
side = 1
side_length = 100
while side < 10:
    if side % 2 == 1:
        t.left(72)
        t.forward(side_length)
    else:
        t.right(144)
        t.forward(side_length)
    side += 1
t.end_fill()
turtle.done()
