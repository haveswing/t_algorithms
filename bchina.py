import turtle
from turtle import *
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("bchina")

leonardo = turtle.Turtle()

leonardo.speed(-1)

for i in range(240):
    leonardo.pencolor("yellow")
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)

    leonardo.penup()
    leonardo.setposition(0, 0)
    leonardo.pendown()

    leonardo.right(0.5)

    leonardo.pencolor("purple")
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)

    leonardo.penup()
    leonardo.setposition(0, 0)
    leonardo.pendown()

    leonardo.right(0.5)

    leonardo.pencolor("orange")
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)
    leonardo.forward(250)
    leonardo.right(120)

    leonardo.penup()
    leonardo.setposition(0, 0)
    leonardo.pendown()

    leonardo.right(0.5)

leonardo.hideturtle()
turtle.done()