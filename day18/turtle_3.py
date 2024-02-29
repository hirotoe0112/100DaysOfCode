import turtle
import random

t = turtle.Turtle()


def draw_shape(sides, is_down):
    degree = 360 / sides
    if is_down:
        degree *= -1
    for _ in range(sides):
        t.right(degree)
        t.forward(100)


for sides in range(3, 11):
    color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
    t.pencolor(color)
    draw_shape(sides, False)
    draw_shape(sides, True)
