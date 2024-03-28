import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Your bet', prompt='Which turtle will when?')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_height = -100

follow_result = []
for turtle_index in range(0, 6):
    tim = turtle.Turtle()
    tim.color(colors[turtle_index])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-238, y=y_height)
    y_height += 50
    follow_result.append(tim)

in_race = True

while in_race:
    for i in follow_result:  #1
        if i.xcor() < 220:
            x = random.choice(follow_result)
            x.forward(5.5)
            print(i.xcor())
        else:
            in_race = False
            win_color = i.pencolor()
            if win_color == user_bet:
                print("Congratulations!")
            else:
                print("Sorry")





# def f():
#     tim.forward(25)
#
# def b():
#     tim.backward(25)
#
# def cc():
#     tim.right(25)
#
# def cw():
#     tim.left(25)
#
# def home():
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def clean_screen():
#     tim.clear()
#     home()
#
# screen.listen()
# screen.onkey(key="Up", fun=f)
# screen.onkey(key="Down", fun=b)
# screen.onkey(key="Right", fun=cc)
# screen.onkey(key="Left", fun=cw)
# screen.onkey(key="h", fun=home)
# screen.onkey(key="c", fun=clean_screen)

turtle.exitonclick()