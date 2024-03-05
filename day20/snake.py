from turtle import Turtle

DIRECTIONS = {"up": 90, "down": 270, "left": 180, "right": 0}


class Snake:
    def __init__(self, body_length):
        self.segments = []
        for i in range(body_length):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.speed("slowest")
            segment.penup()
            segment.goto(-20 * i, 0)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
                self.segments[i - 1].xcor(), self.segments[i - 1].ycor()
            )
        self.segments[0].forward(20)

    def turn_left(self):
        if self.segments[0].heading() != DIRECTIONS["right"]:
            self.segments[0].setheading(DIRECTIONS["left"])

    def turn_right(self):
        if self.segments[0].heading() != DIRECTIONS["left"]:
            self.segments[0].setheading(DIRECTIONS["right"])

    def turn_up(self):
        if self.segments[0].heading() != DIRECTIONS["down"]:
            self.segments[0].setheading(DIRECTIONS["up"])

    def turn_down(self):
        if self.segments[0].heading() != DIRECTIONS["up"]:
            self.segments[0].setheading(DIRECTIONS["down"])
