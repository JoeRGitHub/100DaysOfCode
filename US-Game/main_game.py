import turtle
from pandas import *
import string

def setup_screen():
    screen = turtle.Screen()
    screen.title("US State Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    turtle.setup(725, 491)
    turtle.penup()
    screen.tracer(0) # empty screen


FONT_SIZE = 15
turtle.color("red")
df = read_csv('50_states.csv')

def main():
    screen = turtle.Screen()
    number_of_guess = 0
    guess = []

    while number_of_guess < 50:
        # state_answer = string.capwords(screen.textinput(f"{number_of_guess}/50", "Guess USAs 50 states:"))
        state_answer = screen.textinput(f"{number_of_guess}/50", "Guess USAs 50 states:").title()
        print(state_answer)

        if state_answer == "Exit":
            break

        if state_answer in df['state'].values:
            print("Good guess!")
            state_data = df[df.state == state_answer]
            # I have add "iloc[0]" because single element Series is deprecated
            turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            turtle.write(state_answer, font=("Arial", FONT_SIZE, "bold"), align="center")
            number_of_guess += 1
            print(f'Debug: {state_answer}')
            guess.append(state_answer)
            print(guess)
        else:
            print("Incorrect guess. Try again!")

    # show new screen after 'screen.tracer(0)'
    screen.update()

if __name__ == "__main__":
    setup_screen()
    main()