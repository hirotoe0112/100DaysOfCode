from turtle import Turtle
import random

ball_speed = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(
            (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        )
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = ball_speed

    def move(self):
        next_xcor = self.xcor() + self.x_move
        next_ycor = self.ycor() + self.y_move
        self.goto((next_xcor, next_ycor))

    def bounce(self, x_bounce):
        if not x_bounce:
            self.y_move *= -1
        else:
            self.x_move *= -1

    def reset(self):
        self.goto((0, 0))
        self.bounce(x_bounce=True)
        self.ball_speed = ball_speed

    def speed_up(self):
        self.ball_speed *= 0.9
