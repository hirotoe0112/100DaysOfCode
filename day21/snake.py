from turtle import Turtle
import random

DIRECTIONS = {"up": 90, "down": 270, "left": 180, "right": 0}


class Snake:
    def __init__(self, body_length):
        self.segments = []
        for i in range(body_length):
            self.add_segment((-20 * i, 0))
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color(
            (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        )
        segment.speed("slowest")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
                self.segments[i - 1].xcor(), self.segments[i - 1].ycor()
            )
        self.head.forward(20)

    def turn_left(self):
        if self.head.heading() != DIRECTIONS["right"]:
            self.head.setheading(DIRECTIONS["left"])

    def turn_right(self):
        if self.head.heading() != DIRECTIONS["left"]:
            self.head.setheading(DIRECTIONS["right"])

    def turn_up(self):
        if self.head.heading() != DIRECTIONS["down"]:
            self.head.setheading(DIRECTIONS["up"])

    def turn_down(self):
        if self.head.heading() != DIRECTIONS["up"]:
            self.head.setheading(DIRECTIONS["down"])

    def is_hit_wall(self):
        return (
            self.head.xcor() > 290
            or self.head.xcor() < -290
            or self.head.ycor() > 290
            or self.head.ycor() < -290
        )

    def is_hit_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
