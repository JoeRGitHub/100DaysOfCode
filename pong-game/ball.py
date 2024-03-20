import random
from turtle import Turtle
from random import randint
x_random = random.randint(5, 10)
y_random = random.randint(5, 10)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_x_position = self.xcor() + self.x_move
        new_y_position = self.ycor() + self.y_move
        self.goto(new_x_position, new_y_position)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1