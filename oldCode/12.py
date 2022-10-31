from re import S
import turtle
import random

turtle.speed(3)
turtle.colormode(255)
turtle.hideturtle()
def paint():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.pendown()
    turtle.pencolor((r,g,b))
    turtle.pensize(10)
    turtle.circle(80)
    turtle.penup()

paint()
turtle.goto(-180,0)
paint()
turtle.goto(180,0)
paint()
turtle.goto(-180/2,-50)
paint()
turtle.goto(180/2,-50)
paint()

turtle.goto(0,-100)
turtle.down()
turtle.pencolor("#000")
turtle.write("张俊伟 3010",align="center",font="宋体,8")
turtle.done()
