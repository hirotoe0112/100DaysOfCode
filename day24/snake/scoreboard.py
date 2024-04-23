from turtle import Turtle

font_settings = {
    "font": ("Arial", 16, "normal"),
    "align": "center",
}
file_name = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file_name, "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.write_score()

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    def write_score(self):
        self.clear()
        self.write(
            f"Score: {self.get_score()} High Score: {self.get_high_score()}",
            align=font_settings["align"],
            font=font_settings["font"],
        )

    def increase_score(self, increase_score):
        self.score += increase_score
        self.write_score()

    def reset(self):
        if self.get_score() > self.get_high_score():
            self.high_score = self.score
            self.write_data(self.high_score)
        self.score = 0
        self.write_score()

    def write_data(self, data):
        with open(file_name, "w") as file:
            file.write(f"{data}")
