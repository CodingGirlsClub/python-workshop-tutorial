# -*- coding: utf-8 -*-

"""
Created By pengguanhua on 2017/12/10
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
