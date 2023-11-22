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
player = {}
dealer = {}
player_list = []
dealer_list = []

player_score = 0
dealer_score = 0

def playe_cards(num_of_cards=1):
    global player_score
    while num_of_cards > 0:
        cards_player = random.choice(cards)
        player_list.append(cards_player)
        player_score += cards_player
        num_of_cards -= 1
        player['player_cards'] = player_list

    if player_score >= 21:
        print('You scroe is more then 21, you loss')
        return

    print(f"Player cards: {player['player_cards']}, Current score: {player_score}")

def check_21():
    if player_score >=21:
        print(f'You scroe is {player_score}, more then 21, You loss')

def dealer_cards(num_of_cards=1):
    global dealer_score
    while num_of_cards > 0:
        cards_dealer = random.choice(cards) #Get random number from list
        dealer_list.append(cards_dealer) #Create one list 
        dealer_score += cards_dealer #Sum score
        num_of_cards -= 1 #Count down
        dealer['dealer_cards'] = dealer_list #Add to dic

    if dealer_score >= 21:
        print('You scroe is more then 21, you loss')
        return
    
    print(f"Dealer cards: {dealer['dealer_cards'][0]}, Current score: {dealer_score}")

    continue_round = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_round == 'y':
        playGame(continue_round)
    else:
        print("See you!")

def playGame(continue_round):
    while continue_round == 'y':
        continue_round = 'n'
        #print(f'\nBefore: {player}')
        playe_cards()
        #check_21()
        #print(f'After: {player}')
        #print(f'Befroe: {dealer}')
        dealer_cards()
        
        #print(f'After: {dealer}')

def startGame():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        playe_cards(num_of_cards=2)
        dealer_cards(num_of_cards=2)
    else:
        print("ByBy")

startGame()

