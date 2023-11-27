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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = {}
dealer = {}
player_list = []
dealer_list = []
player_score = 0
dealer_score = 0

def player_cards(num_of_cards=1):
    global player_score
    while num_of_cards > 0:
        cards_player = random.choice(cards)
        player_list.append(cards_player)
        player_score += cards_player
        num_of_cards -= 1
        player['player_cards'] = player_list

    print(f"Player cards: {player['player_cards']}, Current score: {player_score}")


def dealer_cards(num_of_cards=1):
    global dealer_score
    while num_of_cards > 0:
        cards_dealer = random.choice(cards) #Get random number from list
        dealer_list.append(cards_dealer) #Create one list 
        dealer_score += cards_dealer #Sum score
        num_of_cards -= 1 #Count down
        dealer['dealer_cards'] = dealer_list #Add to dic

    print(f"Dealer cards: {dealer['dealer_cards'][0]}, Current score: {dealer_score}")
    check_21()
    

def check_21():
    global player_score
    global dealer_score
    if player_score >=21:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'You went over. You lose\n')
        player.clear()
        player_list.clear()
        dealer.clear()
        dealer_list.clear()
        player_score = 0
        dealer_score = 0
        startGame()
    elif dealer_score >=21:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Dealer went over. You win\n')
        player.clear()
        player_list.clear()
        dealer.clear()
        dealer_list.clear()
        player_score = 0
        dealer_score = 0        
        startGame()
    else:
        continue_round()
    
def continue_round():
    continue_round = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_round == 'y':
        player_cards()
        dealer_cards()
    else:
        check_17()
        print("See you!")

def check_17():
    global dealer_score
    if dealer_score <= 17:
        while dealer_score <= 17:
            cards_dealer = random.choice(cards) #Get random number from list
            dealer_list.append(cards_dealer) #Create one list 
            dealer_score += cards_dealer #Sum score
            check_17()
            #check_21()
    else:
        check_21()

def finel():
    if player_score == dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Draw result!\n')

    elif player_score < dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Dealer win!\n')

    elif player_score > dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'You win!\n')

    continue_round()   

player_score = 0
dealer_score = 0

def startGame():
    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'y':
        clear()
        player_cards(num_of_cards=2)
        dealer_cards(num_of_cards=2)
    else:
        print("ByBy")

startGame()

