from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(
            (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        )
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto((self.xcor(), self.ycor() + 20))

    def go_down(self):
        self.goto((self.xcor(), self.ycor() - 20))
