# The goal of the game is to guess the correct answer as many times as possible.
# Each correct guess earns a point.
# An incorrect answer disqualifies from the game.
# The guesses are based on any two options and the player must choose one of them (A or B)
# The comparison will be made from an existing dic within a list of options under the 'follower_count' key.
# From the second guessesing options, the guesses B will become A, anb a new randome options will appear under option B etc.
# The info for user to guess: "Neymar, a Footballer, from Brasil."


# from random import randint
import random
from game_data import data
#print(len(data))

# Create 2 randme numbers to display 2 options

def randomeChoice():

    dic1 = random.choices(data)
    dic2 = random.choices(data)
    print(f"Compare A: {dic1[0]['name']}, a {dic1[0]['description']}, from {dic1[0]['country']}")
    print(f"Compare B: {dic2[0]['name']}, a {dic2[0]['description']}, from {dic2[0]['country']}")

    # a = (f"Compare A: {dic1[0]['name']}, a {dic1[0]['description']}, from {dic1[0]['country']}")
    # b = (f"Compare B: {dic2[0]['name']}, a {dic2[0]['description']}, from {dic2[0]['country']}")    
    # return a, b
#randomeChoice()

# randomNum = random.randint(0,50)
# print(randomNum)
# a = f"Compare A: {data[randomNum]['name']}, a {data[randomNum]['description']}, from {data[randomNum]['country']}"
# print(a)
    
# randomNum2 = random.randint(0,50)
# print(randomNum2)
# b = f"Compare A: {data[randomNum2]['name']}, a {data[randomNum2]['description']}, from {data[randomNum2]['country']}"
# print(b)

# one = data[randomNum]['follower_count']
# two = data[randomNum2]['follower_count']
# print(one)
# print(two)

# if one > two:
#     print('randomNum big')
# else:
#     print('randomNum2 big')


def randomeNum():
    return random.randint(0,50)

#print(data[randomeChoice1()]['name'],data[randomeChoice1()]['description'])
def getChoice():
    x = randomeNum()
    print(x)
    NAME = data[x]['name']
    DESCRIPTION = data[x]['description']
    COUNTRY = data[x]['country']
    FOLLOWER_COUNT = data[x]['follower_count']

    #print(NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT )
    return NAME, DESCRIPTION, COUNTRY, FOLLOWER_COUNT 

# check which of the answers is correct - which is bigger
# Ask user to choose between the options A or B

def a_VS_b():
    a = getChoice()
    b = getChoice()

    print(a)
    print(b)

    answer = input('A vs B: ')
    a = 81
    b = 110
    
    while "A"(3) > B(3):


    print(a[3])
    print(b[3])

    if a[3] > b[3]:
        print('a biger')
    else:
        print('b biger')

# If the answer is correct, the player gets a point. 
# And guesses 'B' becomes 'A', anb a new randome options will appear under option B etc.
# if the answer is incorrect - game over.



#Compare A: Neymar, a Footballer, from Brasil.

# Against B: 9GAG, a Social media platform, from China.

# Who has more followers? Type 'A' or 'B': 