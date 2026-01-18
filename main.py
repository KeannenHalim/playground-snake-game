from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)


snake = Snake()
food = Food()
wall = Wall()
scoreboard = Scoreboard()

wall.draw_wall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.game_over()
        game_is_on = False

    if snake.check_colision_with_self():
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
