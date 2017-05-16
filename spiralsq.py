import turtle
from turtle import *
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("michelangelo")

michelangelo = turtle.Turtle()

michelangelo.speed(-1)

def pick_color():
    # colors = ["blue","brown","red","yellow","green","orange","beige","turquoise","pink"] # *-black
    colors = ["red", "yellow", "green"]
    color = random.shuffle(colors)
    return colors[0]

randCol = pick_color()

# life = True

for i in range(360):
    random_color = pick_color()
    michelangelo.pencolor(random_color)
    michelangelo.forward(200)
    michelangelo.right(90)
    michelangelo.forward(200)
    michelangelo.right(90)
    michelangelo.forward(200)
    michelangelo.right(90)
    michelangelo.forward(200)
    michelangelo.right(90)

    michelangelo.penup()
    michelangelo.setposition(0,0)
    michelangelo.pendown()
    michelangelo._rotate(1)


michelangelo.hideturtle()
turtle.done()