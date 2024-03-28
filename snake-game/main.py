from turtle import Screen
import time
from sanke import Snake
from food import Food
from scoreboard import Scoreboard

SNAKE_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # empty screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.home, key="h")

game_on = True

while game_on:
    screen.update()  # show new screen after 'screen.tracer(0)'
    time.sleep(SNAKE_SPEED)  # snake speed
    snake.move()

    # Move dot to random point as soon as the snake is in distance of the dot
    if snake.head.distance(food) < 15:
        food.random_food()
        scoreboard.increase_score()
        snake.snake_extend()
    # Transition between the edges of the square
    if snake.head.xcor() > 300:
        snake.head.goto(x=-300, y=snake.head.pos()[1])
    elif snake.head.xcor() < -300:
        snake.head.goto(x=300, y=snake.head.pos()[1])
    elif snake.head.ycor() > 300:
        snake.head.goto(x=snake.head.pos()[0], y=-300)
    elif snake.head.ycor() < -300:
        snake.head.goto(x=snake.head.pos()[0], y=300)
    #  Detect collision of the snake with itself
    for square in snake.square_list[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.save_high_score()
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
