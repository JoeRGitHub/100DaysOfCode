from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5)  # the dot is 20x20 (1), half of that is 10x10 (0.5)
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.random_food()

    def random_food(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x=x_random, y=y_random)