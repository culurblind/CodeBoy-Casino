#War
import random
import time
from itertools import product

# game over variable
gameStatus = False
print("Welcome to War! The goal of this game is to win all the cards in a deck. Each player starts out with exactly half the deck facedown.")
print("At the same time, both players draw a singular card. The player with the highest value card wins, and takes all the cards drawn.")
print("If the cards drawn hold the same value and the players tie, each player continues drawing cards until one person wins")
# mapping cards to numerical values

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = list(product(ranks, suits))
random.shuffle(deck)

index = 26
playerDeck = deck[:26]
computerDeck = deck[:26]

#while playerDeck