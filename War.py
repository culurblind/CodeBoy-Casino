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
def playWar(playerCards, computerCards):
  warTie = 0
  while playerCards and computerCards:
    playerCard = playerCards.pop(0)
    computerCard = computerCards.pop(0)
    if playerCard > computerCard:
      return playerCard, warTie
    elif computerCard > playerCard:
      return None, warTie
    else:
      warTie += 2

  if playerCards:  # Player wins with remaining cards
    return playerCards[0], warTie
  else:  # Computer wins with remaining cards
    return None, warTie
  
def playGame():
    # Get initial bets and ties
    playerBet = playerDeck[0]
    playerTie = 0
    computerBet = computerDeck[0]
    computerTie = 0

  # Play the round
    while playerBet is not None and computerBet is not None:
        # Compare cards
        if playerBet > computerBet:
            winner = "player"
            computerTie += 1  # Computer loses tie cards
        elif computerBet > playerBet:
            winner = "computer"
            playerTie += 1  # Player loses tie cards
        else:  # Tie
            playerTie += 1
            computerTie += 1
        # Handle war if both decks have enough cards
        if len(playerDeck) >= 3 and len(computerDeck) >= 3:
            # Play a mini-war with the next 3 cards
            playerWarBet, playerWarTie = playWar(playerDeck[1:4], computerDeck[1:4])
            playerTie += playerWarTie
            computerTie += computerWarTie
            playerBet = playerWarBet if playerWarBet else None
            computerBet = None if not computerDeck else computerDeck[0]
        else:  # Not enough cards for war, tie the round
            winner = None

        # Update decks based on result
        del playerDeck[0]
        if winner == "player":
                    playerDeck.extend(computerDeck[:computerTie])
                    del computerDeck[:computerTie]
        elif winner == "computer":
                    computerDeck.extend(playerDeck[:playerTie])
    del playerDeck[:playerTie]
        # Return remaining bets and accumulated tie cards
    return playerBet, playerTie, computerBet, computerTie, winner

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
    slow_print("You have " + str(get_element_count(playerDeck)) + " cards, and I have " + str(get_element_count(computerDeck)) + " cards") 
    playGame()


  

