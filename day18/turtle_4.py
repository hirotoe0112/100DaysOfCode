import turtle
import random

t = turtle.Turtle()
t.pensize(5)
t.speed("fast")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def walk():
    t.pencolor(random_color())
    t.setheading(random.choice([0, 90, 180, 270]))
    t.forward(30)


while True:
    walk()
