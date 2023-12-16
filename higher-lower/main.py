# The goal of the game is to guess the correct answer as many times as possible.
# Each correct guess earns a point.
# An incorrect answer disqualifies from the game.
# The guesses are based on any two options and the player must choose one of them (A or B)
# The comparison will be made from an existing dic within a list of options under the 'follower_count' key.
# From the second guessesing options, the guesses B will become A, anb a new randome options will appear under option B etc.
# The info for user to guess: "Neymar, a Footballer, from Brasil."

import random
from game_data import data
import os
clear = lambda: os.system('clear')

dbRandomNumber = {'key':None} 

def generate_different_numbers():
    x = random.randint(0, 49) 
    print(f'Befroe: {dbRandomNumber}')
    while dbRandomNumber['key'] == x: 
        print('The numbers are the same')
        x = random.randint(0, 49)
    else:
        dbRandomNumber['key'] = x
        print(f'After: {dbRandomNumber}')
        return x

def getChoice():
    x = generate_different_numbers()
    NAME = data[x]['name']
    DESCRIPTION = data[x]['description']
    COUNTRY = data[x]['country']
    FOLLOWER_COUNT = data[x]['follower_count']
    #print(NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT )
    return NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT

# Check which of the answers is correct - which is bigger
# Ask user to choose between the options A or B
# If the answer is correct, the player gets a point. 
score = 0
compareA = getChoice()

def a_VS_b():
    global compareA
    global score

    compareB = getChoice()

    resultA = f'Compare A: {compareA[0]} a {compareA[1]}, from {compareA[2]}.'
    print(resultA)
    resultB = f'Compare B: {compareB[0]} a {compareB[1]}, from {compareB[2]}.'
    print(resultB)

    resultA_count = compareA[3]
    print(f'The resultA: {resultA_count}')
    resultB_count = compareB[3]
    print(f'The resultB: {resultB_count}')
    
    a = resultA_count 
    b = resultB_count

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a':
        if a > b:
            # And guesses 'B' becomes 'A', anb a new randome options will appear under option B etc.
            compareA = compareB
            score += 1
            clear()
            print(f"You're right! Current score:{score}")
            a_VS_b()
        # if the answer is incorrect - game over.    
        else:
            print(f"Sorry, that's wrong. Your final score: {score}")
            playAgain = input('Do you wish to try to play again y/n?  ')
            if playAgain == 'y':
                a_VS_b()
            else:
                print('See you next time.')
    elif answer == 'b':
        if b > a:
            # And guesses 'B' becomes 'A', anb a new randome options will appear under option B etc.
            compareA = compareB
            score += 1
            clear()
            print(f"You're right! Current score:{score}")
            a_VS_b()
        # if the answer is incorrect - game over.
        else:
            print(f"Sorry, that's wrong. Your final score: {score}")
            playAgain = input('Do you wish to try to play again? y/n ')
            if playAgain == 'y':
                a_VS_b()
            else:
                print('See you next time.')

    else:
        print("\n## Invalid character ##\n")
        playAgain = input('Do you wish to try to again? y/n ')
        if playAgain == 'y':
            clear()
            a_VS_b()
        else:
            print('See you next time.')
a_VS_b()

