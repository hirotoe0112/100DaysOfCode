from turtle import Turtle
import random

move_distance = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(
            (random.randint(0, 170), random.randint(0, 170), random.randint(0, 170))
        )
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset()
        self.move_distance = move_distance

    def reset(self):
        self.goto((0, -280))

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.move_distance)
