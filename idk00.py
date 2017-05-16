import turtle
from turtle import *
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("michelangelo")

michelangelo = turtle.Turtle()

michelangelo.speed(99)

michelangelo.pencolor("green")

for i in range(60):
    michelangelo.forward(random.randint(9,500))
    michelangelo.right(30)
    michelangelo.forward(20)
    michelangelo.left(60)
    michelangelo.forward(50)
    michelangelo.right(30)

    michelangelo.penup()
    michelangelo.setposition(0, 0)
    michelangelo.pendown()

    michelangelo.right(2)

michelangelo.pencolor("yellow")

for i in range(60):
    michelangelo.forward(random.randint(9,500))
    michelangelo.right(30)
    michelangelo.forward(20)
    michelangelo.left(60)
    michelangelo.forward(50)
    michelangelo.right(30)

    michelangelo.penup()
    michelangelo.setposition(0, 0)
    michelangelo.pendown()

    michelangelo.right(2)

michelangelo.pencolor("red")

for i in range(60):
    michelangelo.forward(random.randint(9,500))
    michelangelo.right(30)
    michelangelo.forward(20)
    michelangelo.left(60)
    michelangelo.forward(50)
    michelangelo.right(30)

    michelangelo.penup()
    michelangelo.setposition(0, 0)
    michelangelo.pendown()

    michelangelo.right(2)

michelangelo.pencolor("black")

for i in range(360):
    michelangelo.forward(random.randint(9,500))
    michelangelo.right(random.randint(9,500))
    michelangelo.forward(random.randint(9,500))
    michelangelo.left(random.randint(9,500))
    michelangelo.forward(random.randint(9,500))
    michelangelo.right(random.randint(9,500))

    michelangelo.penup()
    michelangelo.setposition(0, 0)
    michelangelo.pendown()

    michelangelo.right(2)

turtle.done()