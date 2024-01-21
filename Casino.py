import Roulette as rl
import BlackJack as bj
import Craps as cr
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

#if the person is coming back to the casino floor 
retuner = " "

balance = 1000
play = True
while play == True:
    clear_terminal()
    slow_print("Welcome" + retuner + "to the |CodeBoy Casino| floor! You have a balance of " + str(balance) + ".")

    play_game = False 

    while (play_game ==  False):
        slow_print("Which game room would you like to enter? BlackJack, Roulette, or Craps?")

        game = (str(input())).lower()
        clear_terminal()

        if game == "blackJack":
            balance = bj.blackJack(balance)
            play_game = True
        if game == "roulette":
            balance = rl.roulette(balance)
            play_game = True
        if game == "craps":
            balance = cr.craps(balance)
            play_game = True
        else:
            slow_print("Please enter a valid game room you would like to enter.")

print(balance)
        