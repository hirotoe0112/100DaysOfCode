import random
import turtle


class RacingTurtle:
    def __init__(self, color, postition_y):
        self.t = turtle.Turtle(shape="turtle")
        self.t.color(color)
        self.t.speed("slowest")
        self.t.penup()
        self.t.setposition(-230, postition_y)

    def run(self):
        self.t.forward(random.randint(0, 10))

    def is_goal(self):
        return 230 <= self.t.xcor()
