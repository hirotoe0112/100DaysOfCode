from turtle import Turtle
import random

font_settings = {
    "font": ("Arial", 80, "bold"),
    "align": "center",
}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(
            (
                random.randint(180, 255),
                random.randint(180, 255),
                random.randint(180, 255),
            )
        )
        self.speed("fastest")
        self.goto(x=0, y=180)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            f"{self.l_score}    {self.r_score}",
            align=font_settings["align"],
            font=font_settings["font"],
        )

    def increase_l_score(self):
        self.l_score += 1
        self.write_score()

    def increase_r_score(self):
        self.r_score += 1
        self.write_score()
