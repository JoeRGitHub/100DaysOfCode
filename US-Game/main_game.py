import turtle
# from pandas import *
import pandas as pd

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
df = pd.read_csv('50_states.csv')


def main():
    screen = turtle.Screen()
    number_of_guess = 0
    guess_list = []
    update_list = []

    while number_of_guess < 50:
        state_answer = screen.textinput(f"{number_of_guess}/50", "Guess USAs 50 states:").title()
        print(state_answer)

        if state_answer == "Exit":

            # for i in df.state:
            #     if i not in guess_list:
            #         update_list.append(i)

            # Change to list comprehension
            missing_states = [state for state in df.state if state not in guess_list]

            # Create a new CSV file form the reminder state
            # The 'w+' overwrite the exists file

            # Change to list comprehension
            # new_csv = pd.DataFrame(update_list)
            new_csv = pd.DataFrame(missing_states)
            new_csv.to_csv("remind_states.csv", mode='w+')

            print(guess_list)
            print(f'List of missing countries:\n{result}')
            break

        if state_answer in df['state'].values and state_answer not in guess_list:
            print("Good guess!")
            state_data = df[df.state == state_answer]
            # I have added "iloc[0]" because single element Series is deprecated
            turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            turtle.write(state_answer, font=("Arial", FONT_SIZE, "bold"), align="center")
            number_of_guess += 1
            print(f'Debug: {state_answer}')
            guess_list.append(state_answer)
            print(guess_list)
        else:
            print("Incorrect guess. Try again!")

    if number_of_guess == 50:
        print("You won!")
    else:
        print("You lost!")
    # show new screen after 'screen.tracer(0)'
    screen.update()


if __name__ == "__main__":
    setup_screen()
    main()
