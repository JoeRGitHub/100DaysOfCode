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

user_cards = []
computer_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    #print(card)
    return card

def calculate_score(sum_cards_list):
    return sum(sum_cards_list)

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
# print(f'player in round1: {user_cards}, {calculate_score(user_cards)}')
# print(f'computer in round1: {computer_cards}, {calculate_score(computer_cards)}') 

def player():
    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    #print(user_cards)
    #print(user_score)
    return user_cards, user_score 
    
def computer():
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    #print(computer_cards)
    #print(computer_score)
    return  computer_cards, computer_score

def check_21_ply():
    if calculate_score(user_cards) < 21:
        print(f'player in IF check_21_ply lest:  {user_cards}, {calculate_score(user_cards)}')    
        return True
    # elif calculate_score(computer_cards) < 21:
    #     print(f'player in check_21 lest:  {computer_cards}, {calculate_score(computer_cards)}')      
    #     return True        
    else:
        #print(f'player in ELSE check_21_ply more: {user_cards}, {calculate_score(user_cards)}')
        #print(f'computer in check_21 more: {computer_cards}, {calculate_score(computer_cards)}')   
        return False
       #check_17()

def check_21_com():
    if calculate_score(computer_cards) < 21:
        print(f'computer in IF check_21_com lest:  {computer_cards}, {calculate_score(computer_cards)}')      
        return True  
    else:
        #print(f'player in check_21 more: {user_cards}, {calculate_score(user_cards)}')
        #print(f'computer in ELSE check_21_com more: {computer_cards}, {calculate_score(computer_cards)}')   
        return False
    
def check_17():
    while calculate_score(computer_cards) <= 17:
        computer()
    else:
        if calculate_score(user_cards) >= 21:
            print('User los')
            # print(f'player in check_17: {user_cards}, {calculate_score(user_cards)}')        
            # print(f'computer in check_17: {computer_cards}, {calculate_score(computer_cards)}')
        elif calculate_score(computer_cards) >= 21:
            print('Computer los')
        elif calculate_score(user_cards) > calculate_score(computer_cards):
            print('User Won!')
        elif calculate_score(user_cards) < calculate_score(computer_cards):
            print('Computer Won!')


        print(f'player in check_17: {user_cards}, {calculate_score(user_cards)}')        
        print(f'computer in check_17: {computer_cards}, {calculate_score(computer_cards)}')
        return

def continue_round():
    while check_21_ply() and check_21_com() == True and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':# calculate_score(user_cards) <= 21 or calculate_score(computer_cards) <= 21:
       #player_cards_result, player_score_result = player()
       #computer_cards_result, computer_score_result = computer()
      
            player()
            computer()

    else:
        print('ByBY')
        check_17()
        
continue_round()

