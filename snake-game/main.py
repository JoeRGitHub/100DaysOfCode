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



# square_pos = [(0,0), (-20,0), (-40,0)]
# square_list = []
#
# for i in square_pos:
#     square = Turtle("square")
#     square.penup()
#     square.color("white")
#     square.goto(i)
#     square_list.append(square)
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
    screen.update()  # show new screen after 'screen.tracer(0)'
    time.sleep(SNAKE_SPEED)  # snake speed
    # for seg_num in range(len(square_list) -1 ,0, -1): #the -1 is for the square_list[0-2]
    #     print(seg_num)
    #     new_segment_x = square_list[seg_num - 1].xcor() #use the -1 to start form the end
    #     new_segment_y = square_list[seg_num - 1].ycor()
    #     #square_list[seg_num].forward(20)
    #     square_list[seg_num].goto(new_segment_x, new_segment_y)
    # square_list[0].forward(20)
    snake.move()

    # move dot to random point as soon as the snake is in distance of the dot
    if snake.head.distance(food) < 15:
        food.random_food()
        increase_score.score()

screen.exitonclick()
