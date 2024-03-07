from turtle import Turtle

font_settings = {
    "font": ("Arial", 16, "normal"),
    "align": "center",
}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.write_score()

    def get_score(self):
        return self.score

    def write_score(self):
        self.clear()
        self.write(
            f"Score: {self.get_score()}",
            align=font_settings["align"],
            font=font_settings["font"],
        )

    def increase_score(self, increase_score):
        self.score += increase_score
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER", align=font_settings["align"], font=font_settings["font"]
        )
