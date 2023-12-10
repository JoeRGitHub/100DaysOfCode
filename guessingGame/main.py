
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
rand_num = random.randint(1, 100) #60
from art import logo

easy = 10
hard = 5

def choice_game_lavel(easy,hard):
    print(logo)
    leval_game = input("Choose a difficulty. Type 'easy' or 'hard': ")
    out = int(input('Guess a number between 1 to 100: '))
    if leval_game == 'easy':
        while out != rand_num and easy > 0:
            easy -= 1
            if rand_num > out:
              print("To low.")
            elif rand_num < out:
              print("To high.")
            print(f'You have {easy} attempts remaining to guess the number.')
            out = int(input('Guess a number between 1 to 100: '))
        else:
            if easy == 0:
                print('no more guess!')
            elif out == rand_num:
                print('nice guess!')
    
    elif leval_game == 'hard':
        print(f'out befroe while: {out}')
        while out != rand_num and hard > 0:
            hard -= 1
            print(f'You have {hard} attempts remaining to guess the number.')
            if rand_num > out:
              print("To low.")
            elif rand_num < out:
              print("To high.") 
            print(f'You have {hard} attempts remaining to guess the number.')                         
            out = int(input('Guess a number between 1 to 100: '))
        else:
            if hard == 0:
                print('no more guess!')
            elif out == rand_num:
                print('nice guess!')

def gusee_num():
    return input('Guess a number between 1 to 100: ')

choice_game_lavel(easy,hard)
