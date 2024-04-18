from turtle import Turtle
import random

starting_level = 1
font_settings = {
    "font": ("Arial", 30, "bold"),
    "align": "center",
}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(
            (random.randint(0, 170), random.randint(0, 170), random.randint(0, 170))
        )
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=-220, y=240)
        self.level = starting_level
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(
            f"level: {self.level}",
            align=font_settings["align"],
            font=font_settings["font"],
        )

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto((0, 0))
        self.write(
            "Game Over",
            align=font_settings["align"],
            font=font_settings["font"],
        )
