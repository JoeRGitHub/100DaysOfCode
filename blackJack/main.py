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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
result = {}
player_list = []
dealer_list = []

def cards_random_number(num_of_cards=1):
    player_score = 0
    dealer_score = 0
    while num_of_cards > 0:
        
        cards_player = random.choice(cards)
        cards_dealer = random.choice(cards)
        player_list.append(cards_player)
        dealer_list.append(cards_dealer)
        ##result['player_cards'].append([cards_list]) # {'player_cards': [10]}
        player_score += cards_player
        dealer_score += cards_dealer
        num_of_cards -= 1
        result['player_cards'] = player_list
        result['dealer_cards'] = dealer_list
    print(f"Player cards: {result['player_cards']}, Current score: {player_score}")
    print(f"Dealer cards: {result['dealer_cards'][0]}, Current score: {dealer_score}")

def playGame():
    #play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    continue_round = 'y'
    while continue_round == 'y':
        #print(f'before: {continue_round}')
        continue_round = input("Type 'y' to get another card, type 'n' to pass: ")
        #print(f'efter: {continue_round}')

def startGame():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print(play)
    if play == 'y':
        cards_random_number(num_of_cards=2)
        playGame()
        print("Good") # check why the func is returning this print
    else:
        print("ByBy")


startGame()
# game = startGame()
# print(game)

#playGame()    

#def get2Cards():


# play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# print(play)
# if play == 'y':
#     playGame()
# else:
#     print("ByBy")
