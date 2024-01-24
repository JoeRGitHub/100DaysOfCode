import turtle
from turtle import *
import random

tim = turtle.Turtle()
tim.pensize(2)
tim.speed(50)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

# create a Spirograph with random color
def spirograph_shape():
    for _ in range(37):
        tim.circle(100)
        tim.left(10)
        change_color()

#spirograph_shape()

# def random_walk(x):
#     if x == 1:
#         tim.right(90)
#         tim.forward(20)
#     elif x == 2:
#         tim.left(90)
#         tim.forward(20)
#
# for _ in range(20):
#     x = random.randint(1, 2)
#     change_color()
#     random_walk(x)

def drawing_different_shapes():
    max_shape = 3
    degrees = 360
    degree = 120
    interactions = 3

    while max_shape < 10:
        for _ in range(interactions):
            tim.forward(100)
            tim.right(degree)
        change_color()
        interactions += 1
        max_shape += 1
        degree = int(degrees / max_shape)
        # print(max_shape)
        # print(degree)
# drawing_different_shapes()
def triangle():
    change_color()
    tim.forward(100)
    tim.right(120)
    tim.forward(100)
    tim.right(120)
    tim.forward(100)
    tim.right(120)

def square():
    change_color()
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)


def penragon():
    change_color()
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)

# triangle()
# square()
# penragon()

turtle.exitonclick()

