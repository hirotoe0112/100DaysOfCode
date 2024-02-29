import turtle
import random

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_circle(heading):
    t.pencolor(random_color())
    t.setheading(heading)
    t.circle(100)


heading = 0
while heading < 360:
    draw_circle(heading)
    heading += 6


screen = turtle.Screen()
screen.exitonclick()
