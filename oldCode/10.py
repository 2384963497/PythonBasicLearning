import turtle as t
import random
#图形1
t.speed(0.5)
t.pensize(22)
t.pencolor("#f00")
t.circle(180)

t.penup()
t.left(90)
t.forward(70)
t.pendown()
t.right(90)

t.fillcolor("#1331F2")
t.begin_fill()
t.circle(110)
t.end_fill()
t.pensize(1)
t.penup()
for i in range(2):
    t.left(90)
    t.forward(140)

t.left(180)
t.forward(45)
t.pendown()
t.pencolor('#fff')
t.fillcolor('#fff')
t.begin_fill()
for i in range(5):
    t.forward(188)
    t.right(180-36)
t.end_fill()

t.penup()
t.goto(5,-100)
t.pendown()
t.pencolor("#000")
t.write("张俊伟 2022051613010",False,align="center",font="宋体,8")




t.done()