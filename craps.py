import random
import time
import os
#craps


#prints given string slowly
#default delay of 0.1s if no delay peramter is given
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.03

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

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

#instance when first roll doesn't end game
def reRoll(diceNum):
    while pastNumber == False:
        print("you rolled " + str(diceNum) + " the die will reroll")
        if diceNum == list:
            slow_print("You rerolled " + str(list) + " again! You win!")
            pastNumber == True
            balance += 2 * bet
        if diceNum == 7:
            slow_print("You rolled a 7! You have lost the game")
            pastNumber == True
        else:
            diceNum= dicetotal()


# opening commands
slow_print("welcome to Craps! Your goal is to see whether the dice will roll a winning number. In the first round,")
slow_print("if you roll a 7 or 11, you win. If you roll a 2, 3, or 12, you automatically lose")
slow_print("any other combination of values will be added to the point, and you will continue rerolling until you get that number again or roll a 7, in which you lose")
time.sleep(1)
clear_terminal()

gameplay = True
list = []
nextnumber = []
balance = 1000

#runs game
while gameplay == True:
    time.sleep(1)
    clear_terminal()
    # Balance/ Betting set up
    slow_print("balance: " + str(balance))
    bet = input("How much do you want to bet? ")
    # makes sure the bet is an int
    while isnt_int(bet):
        slow_print("You need to type a number as a valid bet")
        time.sleep(1.5)
        clear_terminal()
        bet = input("How much do you want to bet? ")
    bet = int(bet)
    balance -= bet
    turn = True
    # condition if person bets more money than they have
    while balance < 0:
        slow_print("You do not have that much money")
        print()
        balance += bet
        slow_print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet
    
    while turn:
        diceNum = dicetotal()

        nextStep = input("Type roll! ")
        if nextStep == "roll":
            slow_print("Rolling... Rolling... Rolling... ", 0.1)
            if diceNum == 7 or diceNum == 11:
                slow_print("The dice rolled " + str(diceNum) + ", You won!")
                balance += 2 * bet
                turn = False
            elif diceNum == 2 or diceNum == 3 or diceNum == 12:
                slow_print("You lost the bet, the dice rolled " + str(diceNum))
                turn = False
            else:
                list.append(diceNum)
                #true/flase for if a number is rerolled
                pastNumber = False
                reRoll(diceNum)
        else:
            print("You did not type roll")
    
    gameContinuing = True
    while gameContinuing:
        continueGame = input("Do you still want to play? (y/n) ")
        if continueGame == "n":
            gameContinuing = False
            gameplay = False
            slow_print("Thanks for playing Craps!")
        elif continueGame == "y":
            gameContinuing = False
            print()
        else:
            slow_print("Type y or n")

