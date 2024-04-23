# from turtle import Turtle , Screen
# tom=Turtle()
# s1=Screen()
# tom.color("black","red")
# print(tom.heading())
# tom.begin_fill()
# while True:
#     tom.speed(80)
#     tom.forward(300)
#     tom.left(170+)
#     if tom.heading()==0:
#         break
# tom.end_fill()
# s1.exitonclick()

import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255) 
tom=Turtle()
s1=Screen()
while True:
    tom.pensize(3)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.speed(50)
    tom.circle(100)
    tom.left(10)
    if tom.heading()==0:
        break
s1.exitonclick()