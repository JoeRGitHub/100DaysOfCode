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
#from art import logo_01
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
        print(f'You went over. You lose 😬\n')
        startGame()
    elif dealer_score >=21:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Dealer went over. You win 🤩\n')       
        startGame()
    else:
        continue_round()
    

def continue_round():
    global player_score
    global dealer_score

    continue_round = input("Type 'y' to get another card, type 'n' to pass: ")

    if continue_round == 'y':
        player_cards()
        dealer_cards()
    else:
        check_17()

def check_17():
    global dealer_score
    #print(f'Out: {dealer_score}')
    
    while dealer_score <= 17:
        cards_dealer = random.choice(cards)
        dealer_list.append(cards_dealer)
        dealer_score += cards_dealer
        #print(f'In: {dealer_score}')
        
    finel()

def finel():
    print(f'player: {player_score} dealer: {dealer_score}')
    if player_score > 21 or dealer_score > 21:
        #print('check 21')
        check_21()

    elif player_score == dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Draw result! 🙃\n')
        startGame()

    elif player_score < dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'Dealer win! 😬\n')
        startGame()

    elif player_score > dealer_score:
        print(f"\nYou finel hand: {player['player_cards']}, Current score: {player_score}")
        print(f"Dealer finel hand: {dealer['dealer_cards']}, Current score: {dealer_score}")
        print(f'You win! 🤩\n')
        startGame() 

def startGame():
    global player_score
    global dealer_score
    global player_list
    global dealer_list
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'y':
        clear()
        player.clear()
        player_list.clear()
        dealer.clear()
        dealer_list.clear()
        player_score = 0
        dealer_score = 0
        player_cards(num_of_cards=2)
        dealer_cards(num_of_cards=2)
    else:
        print("\nSee you next time 😀")

startGame()
