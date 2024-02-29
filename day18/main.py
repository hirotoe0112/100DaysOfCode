# import colorgram

# colors = colorgram.extract("image.jpg", 26)

# colors_rgb = []
# for color in colors:
#     colors_rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(colors_rgb)

import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()

colors = [
    (198, 175, 119),
    (125, 36, 23),
    (187, 157, 50),
    (170, 104, 56),
    (5, 56, 83),
    (201, 216, 205),
    (109, 67, 85),
    (39, 35, 34),
    (223, 224, 227),
    (84, 141, 61),
    (20, 122, 175),
    (111, 161, 176),
    (75, 38, 48),
    (8, 67, 47),
    (65, 154, 134),
    (132, 41, 43),
    (184, 98, 81),
    (183, 180, 181),
    (210, 200, 108),
    (178, 201, 186),
    (150, 180, 170),
    (90, 143, 158),
    (28, 81, 59),
    (193, 190, 192),
]

first_position_x = -350
first_position_y = -350
number_of_dots = 100
dot_size = 20
distance = 50

t.hideturtle()
t.penup()
t.setpos(first_position_x, first_position_y)
t.speed("fastest")


def draw_dot():
    t.dot(dot_size, random.choice(colors))


def move_forward():
    t.forward(distance)


def move_next_line():
    t.setpos(first_position_x, t.position()[1] + distance)


for i in range(1, number_of_dots + 1):
    draw_dot()
    if i % 10 == 0:
        move_next_line()
    else:
        move_forward()

screen = turtle.Screen()
screen.exitonclick()
