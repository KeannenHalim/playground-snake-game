from turtle import Turtle

TEXT_POSITION = (0, 300)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(TEXT_POSITION)
        self.color("white")
        self.hideturtle()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="Game Over.",
            align=ALIGNMENT,
            font=FONT,
        )

    def write_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )
