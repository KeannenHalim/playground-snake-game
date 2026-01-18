from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.initiate_snake()
        self.head = self.segments[0]

    def initiate_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def check_colision_with_self(self):
        for segment in self.segments[1::]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].teleport(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return None
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            return None
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            return None
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            return None
        self.head.setheading(RIGHT)
