import turtle
turtle.circle(50,steps=6)
turtle.penup()
turtle.home()
turtle.pendown()
turtle.color("blue","green")
turtle.begin_fill()
turtle.circle(50,steps=3)
turtle.end_fill()
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.write("张俊伟 2022051613010",False,align="center",font="宋体,8")
input()