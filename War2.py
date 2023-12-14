# War
import random
import time
from itertools import product

# Prints given string slowly
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.02

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Counts cards in a list
def get_element_count(int_list):
    if isinstance(int_list, int):
        return 1
    else:
        return len(int_list)

# Plays a single round of the war game
def playGame(playerDeck, computerDeck):
    playerBet = playerDeck[0]
    playerTie = 0
    computerBet = computerDeck[0]
    computerTie = 0

    slow_print(f"You drew {playerBet} and the computer drew {computerBet}!")

    while playerBet is not None and computerBet is not None:
        if playerBet > computerBet:
            winner = "player"
            computerTie += 1
            slow_print(f"You won the round with your {playerBet}! The computer had {computerBet}. You gained {computerTie} tie card.")
        elif computerBet > playerBet:
            winner = "computer"
            playerTie += 1
            slow_print(f"The computer won the round with its {computerBet}. You had {playerBet}. The computer gained {playerTie} tie card.")
        else:  # Tie
            playerTie += 1
            computerTie += 1
            slow_print("It's a tie! Both players draw 3 more cards.")
            slow_print(f"You have {playerTie} tie cards and the computer has {computerTie} tie cards.")

            if len(playerDeck) >= 3 and len(computerDeck) >= 3:
                playerWarBet, playerWarTie = playWar(playerDeck[1:4], computerDeck[1:4])
                playerTie += playerWarTie
                computerTie += computerWarTie
                slow_print(f"You gained {playerWarTie} more tie cards from the mini-war!")

                if playerWarBet:
                    playerBet = playerWarBet
                else:
                    playerBet = None
                    computerBet = None if not computerDeck else computerDeck[0]

            else:
                winner = None
                slow_print("Not enough cards for another war. This round is a tie.")

        # Update decks and display deck size
        del playerDeck[0]
        if winner == "player":
            playerDeck.extend(computerDeck[:computerTie])
            del computerDeck[:computerTie]
            slow_print(f"You now have {len(playerDeck)} cards. The computer has {len(computerDeck)} cards.")
        elif winner == "computer":
            computerDeck.extend(playerDeck[:playerTie])
            del playerDeck[:playerTie]
            slow_print(f"The computer now has {len(computerDeck)} cards. You have {len(playerDeck)} cards.")

    return playerBet, playerTie, computerBet, computerTie, winner

# Plays a mini-war with the specified cards
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

# Game variables
gameOver = False
playerScore = 0
computerScore = 0

# Game setup
slow_print("Welcome to War! The goal of this game is to win all the cards in a deck. Each player starts out with half the deck facedown.")
slow_print("At the same time, both players draw a singular card. The player with the highest value card wins, and takes all the cards drawn.")
slow_print("If the cards drawn hold the same value and the players tie, each player continues drawing cards until one person wins")

# Mapping