#War
import random
import time
from itertools import product

#prints given string slowly
#default delay of 0.1s if no delay peramter is given
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.02

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def get_element_count(int_list):
  if isinstance(int_list, int):
    return 1
  else:
    return len(int_list)

# game over variable
gameStatus = False
slow_print("Welcome to War! The goal of this game is to win all the cards in a deck. Each player starts out with exactly half the deck facedown.")
slow_print("At the same time, both players draw a singular card. The player with the highest value card wins, and takes all the cards drawn.")
slow_print("If the cards drawn hold the same value and the players tie, each player continues drawing cards until one person wins")
# mapping cards to numerical values

#card combinations
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#shuffles deck
deck = list(product(ranks, suits))
random.shuffle(deck)

#sets half the deck to player and computer
index = 26
playerDeck = deck[:26]
computerDeck = deck[:26]

while get_element_count(playerDeck) >= 0 and get_element_count(computerDeck) >= 0:
    slow_print("You have " + str(get_element_count(playerDeck)) + "cards now and I " + str(get_element_count(computerDeck)) + "cards") 
    play_Game()

def play_Game() :
    playerBet = playerDeck[0]
    playerTie = 0
    computerBet = computerDeck[0]
    computerTie = 0
    if computerDeck >= playerDeck :
        del computerDeck[0, computerTie]
        del playerDeck[0, computerTie]
        computerDeck.extend(playerBet)
        computerDeck.extend(computerBet)
    elif playerDeck >= computerDeck :
        del computerDeck.remove[0, computerTie]
        playerDeck.remove[0, playerTie]
        playerDeck.extend(playerBet)
        playerDeck.extend(computerBet)
    elif playerBet == computerBet :
        while playerBet == computerBet :
            playerTie += 1
            computerTie += 1
            playGame() 

