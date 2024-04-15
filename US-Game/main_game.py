import turtle
from pandas import *
import string

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(725, 491)
turtle.penup()
screen.tracer(0) # empty screen

number_of_guess = 0
trace_guess = 0



FONT_SIZE = 15
turtle.color("red")

df = read_csv('50_states.csv')

# # monday = df[df.state == answer]
# # print(monday)


while number_of_guess < 50:

    state_answer = string.capwords(screen.textinput(f"{number_of_guess}/50", "Guess USAs 50 states:"))
    print(state_answer)

    if state_answer in df['state'].values:
        print("You won!")
        #print(df['x'].values)
        x = df[df.state == state_answer]
        #x = df['x'].tolist() == state_answer
        y = x.values.tolist()
        #y = x.to_dict
        print(x)
        print(f'the X: {y[0][1]}')
        print(f'the Y: {y[0][2]}')
        turtle.goto(y[0][1], y[0][2])
        turtle.write(state_answer, font=("Arial", FONT_SIZE, "bold"), align="center")
        number_of_guess += 1
    else:
        print("You lost!")


screen.update() # show new screen after 'screen.tracer(0)'
screen.exitonclick()