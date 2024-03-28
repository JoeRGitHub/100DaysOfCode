from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

BALL_SPEED = 0.1

line_right = Paddle(position_x=350, position_y=0)
line_left = Paddle(position_x=-350, position_y=0)
ball = Ball()

screen.listen()
screen.onkey(fun=line_right.go_up, key="Up")
screen.onkey(fun=line_right.go_down, key="Down")
screen.onkey(fun=line_left.go_up, key="w")
screen.onkey(fun=line_left.go_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(BALL_SPEED)
    screen.update()
    ball.move()
    print(ball.ycor())

    # Collision detection with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision detection with paddle
    # if ball.distance(line_right) > 50 and ball.xcor() > 340:
    #     ball.bounce_x()
    # elif ball.distance(line_left) > 50 and ball.xcor() > -340:
    #     ball.bounce_y()
screen.exitonclick()
