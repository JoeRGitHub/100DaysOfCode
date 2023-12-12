# The goal of the game is to guess the correct answer as many times as possible.
# Each correct guess earns a point.
# An incorrect answer disqualifies from the game.
# The guesses are based on any two options and the player must choose one of them (A or B)
# The comparison will be made from an existing dic within a list of options under the 'follower_count' key.
# From the second guessesing options, the guesses B will become A, anb a new randome options will appear under option B etc.
# The info for user to guess: "Neymar, a Footballer, from Brasil."

# #Did not use this func because I can't easily know what's the random number generated 
# def randomeChoice():
#     dic1 = random.choices(data)
#     dic2 = random.choices(data)
#     print(f"Compare A: {dic1[0]['name']}, a {dic1[0]['description']}, from {dic1[0]['country']}")
#     print(f"Compare B: {dic2[0]['name']}, a {dic2[0]['description']}, from {dic2[0]['country']}")

#     a = (f"Compare A: {dic1[0]['name']}, a {dic1[0]['description']}, from {dic1[0]['country']}")
#     b = (f"Compare B: {dic2[0]['name']}, a {dic2[0]['description']}, from {dic2[0]['country']}")    
#     return a, b
# randomeChoice()

# git commit -m 'finsh game, wroks but need to arrange the code'

# From random import randint
import random
from game_data import data
import os
clear = lambda: os.system('clear')

def randomeNum():
    #Added the check to revent two of the same random numbers
    x = random.randint(0, 50)
    while True:
      y = random.randint(0, 53)
      if x != y:
          return x

def getChoice():
    x = randomeNum()
    print(f'randomeNum: {x}')
    NAME = data[x]['name']
    DESCRIPTION = data[x]['description']
    COUNTRY = data[x]['country']
    FOLLOWER_COUNT = data[x]['follower_count']
    #print(NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT )
    return NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT, x

# Check which of the answers is correct - which is bigger
# Ask user to choose between the options A or B
compareA = getChoice()

# If the answer is correct, the player gets a point. 
score = 0

def a_VS_b():
    #compareA = getChoice()
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
            playAgain = input('Do you wish to try to play again? y/n ')
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
        print("Invalid character")
        playAgain = input('Do you wish to try to play again? y/n ')
        if playAgain == 'y':
            a_VS_b()
        else:
            print('See you next time.')
a_VS_b()

