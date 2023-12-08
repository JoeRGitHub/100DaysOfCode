############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.:


import random
import os
clear = lambda: os.system('clear')
from art import logo

user_cards = []
computer_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(sum_cards_list):
    return sum(sum_cards_list)

def player():
    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    return user_cards, user_score 
    
def computer():
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    return  computer_cards, computer_score


def check_21_ply():
    if calculate_score(user_cards) < 21:
        print(f'Player cards: {user_cards}, Current score: {calculate_score(user_cards)}')    
        return True  
    else:
        return False

def check_21_com():
    if calculate_score(computer_cards) < 21:
        print(f'Computer cards: {computer_cards}, Current score: {calculate_score(computer_cards)}')      
        return True  
    else:
        return False

def play_again():
    if input('Do you wish to play again?') =='y':
        user_cards.clear()
        computer_cards.clear()
        start_game()
    else:
        print("See you next time (-: ")
        return
        
def check_17():
    while calculate_score(computer_cards) <= 17:
        computer()
    else:
        print(f'Player last hand: {user_cards}, {calculate_score(user_cards)}')        
        print(f'Computer last hand: {computer_cards}, {calculate_score(computer_cards)}')
        if calculate_score(user_cards) >= 21:
            print('Computer Won')
        elif calculate_score(computer_cards) >= 21:
            print('User Won')
        elif calculate_score(computer_cards) > calculate_score(user_cards):
            print('Computer Won')
        elif calculate_score(computer_cards) < calculate_score(user_cards):
            print('User Won')
        elif calculate_score(user_cards) == calculate_score(computer_cards):
            print("Draw!")
        # elif calculate_score(user_cards) > calculate_score(computer_cards):
        #     print('User Won!')
        # elif calculate_score(user_cards) < calculate_score(computer_cards):
        #     print('Computer Won!')
        # and calculate_score(computer_cards) < 21 and calculate_score(user_cards) < calculate_score(computer_cards):
        # and calculate_score(user_cards) < 21 and calculate_score(user_cards) > calculate_score(computer_cards):

    play_again()    
        
def continue_round():
    while check_21_ply() and check_21_com() == True and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        player()
        computer()

    else:
        check_17()

def start_game():
    clear()
    print(logo)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    continue_round()

start_game()