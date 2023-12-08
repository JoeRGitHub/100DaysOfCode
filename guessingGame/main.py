# Scoope:
# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# def bar():
#     if 16 > 9:
#       my_variable = 16
#     print(my_variable)
 
# bar()

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

##Get a randome number from 1 to 100 and save it in a ver

import random
rand_num = random.randint(1, 100) #60
print(rand_num)
# Choice game leval #Easy=10 guess #Hard=5 guess

easy = 1
hard = 5

def choice_game_lavel(easy,hard):
    leval_game = input("Choice game leval 'Easy' or 'Hard': ")
    #gusee_num()
    #out = int(input('Guess a number between 1 to 100: '))
    # print(type(out))
    # print(type(rand_num))

    if leval_game == 'easy':
        #number = input('Guess a number between 1 to 100: ')
        print(f'out befroe while: {gusee_num()}')
        while gusee_num() != rand_num and easy > 0:
            print(f'out after while:{gusee_num()}')
            print(easy)
            print(rand_num)
            easy -= 1
            #out = int(input('Guess a number between 1 to 100: '))
            #gusee_num()
        else:
            if easy == 0:
                print('no more guess!')
            elif out == rand_num:
                print('nice guess!')
    
    elif leval_game == 'hard':
        #number = input('Guess a number between 1 to 100: ')
        print(f'out befroe while: {out}')
        while out != rand_num and hard > 0:
            print(f'out after while:{out}')
            print(hard)
            print(rand_num)
            hard -= 1
            out = int(input('Guess a number between 1 to 100: '))
            #gusee_num()
        else:
            if hard == 0:
                print('no more guess!')
            elif out == rand_num:
                print('nice guess!')

def gusee_num():
    return input('Guess a number between 1 to 100: ')

choice_game_lavel(easy,hard)
#gusee_num()