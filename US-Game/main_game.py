import turtle
import pandas as pd
import string

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(725, 491)
screen.tracer(0) # empty screen

number_of_guess = 0
trace_guess = 0



FONT_SIZE = 15
turtle.color("red")

df = pd.read_csv('50_states.csv')

# # monday = df[df.state == answer]
# # print(monday)

while number_of_guess < 50:
    screen.update() # show new screen after 'screen.tracer(0)'
    state_answer = string.capwords(screen.textinput(f"{number_of_guess}/50", "prompt"))
    print(state_answer)

    if state_answer in df['state'].values:
        print("You won!")
        turtle.write(state_answer, font=("Arial", FONT_SIZE, "bold"), align="center")
        number_of_guess += 1
    else:
        print("You lost!")



screen.exitonclick()