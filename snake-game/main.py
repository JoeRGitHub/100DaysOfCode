from turtle import Screen
import time
from sanke import Snake
from food import Food
from scoreboard import Scoreboard, Increase_score

SNAKE_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Empty screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.text_box()
increase_score = Increase_score()
increase_score.dot_box()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.home, key="h")

game_on = True

while game_on:
    screen.update() # show new screen after 'screen.tracer(0)'
    time.sleep(SNAKE_SPEED) # snake speed
    snake.move()

    # move dot to random point as soon as the snake is in distance of the dot
    if snake.head.distance(food) < 15:
        food.random_food()
        increase_score.score()
        snake.snake_extend()

screen.exitonclick()
