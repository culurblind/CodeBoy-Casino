import BlackJack as bj
import Roulette as rl
import craps as cr
import time
import os

def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.05

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# clear_terminal() func clears the terminal after every round
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# isnt_int func makes sure an input is a int
def isnt_int(raw_inp):
    if(not raw_inp.isdigit()):
        return True

balance = 1000
play = True
while play == True:
    slow_print("Welcome to CodeBoy Casino! You have a balance of " + str(balance) + ".")
    slow_print("Which game would you like to play? BlackJack, Roulette, or Craps?")
    print() 
    game = str(input())
    if game == "BlackJack":
        bj.blackJack(balance)
    if game == "Roulette":
        rl.roulette(balance)
    if game == "Craps":
        cr.craps(balance)
    else:
        print()
        