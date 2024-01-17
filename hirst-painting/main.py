import turtle
import random

color_list = [(219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98),
              (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102),
              (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174),
              (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53),
              (232, 209, 16), (74, 79, 40)]

tim = turtle.Turtle()
# Using this because: https://stackoverflow.com/questions/62442393/what-is-turtle-colormode255-for
turtle.colormode(255)
tim.pensize(2)
tim.speed(50)


def change_color():
    x = random.choices(color_list)[0]
    return x


def draw_kube_art():
    for _ in range(10):  # Number of rows
        tim.dot(20, change_color())
        tim.penup()
        tim.forward(30)


def loop_kube(num_of_lines, spass_between_lines):
    for _ in range(num_of_lines):
        draw_kube_art()
        tim.setpos(0, spass_between_lines)
        spass_between_lines += 30


loop_kube(10, 30)

turtle.exitonclick()
