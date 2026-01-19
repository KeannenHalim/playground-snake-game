from turtle import Turtle

SCREEN_WIDTH = 580
SCREEN_HEIGHT = 580


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(x=(SCREEN_WIDTH / 2 * (-1)), y=(SCREEN_HEIGHT / 2 * (-1)))
        # self.pensize(10)

    def draw_wall(self):
        self.forward(SCREEN_WIDTH)
        self.left(90)
        self.forward(SCREEN_HEIGHT)
        self.left(90)
        self.forward(SCREEN_WIDTH)
        self.left(90)
        self.forward(SCREEN_HEIGHT)
