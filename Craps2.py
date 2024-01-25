# Craps.py is a python file that runs the back end code for the casino game craps
# it contains functions that print text slowly, clear the terminal, check if an input is a number, and also a method for rolling the dice 
# and the main function where the actual game runs, returning the new balance

import random

#craps

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def craps(balance, bet):

    if balance <= 0:
        gameplay = False
    else:
        gameplay = True

    while gameplay == True:

        balance -= bet

        diceNum = dicetotal()

        if diceNum == 7 or diceNum == 11:
            balance += 2 * bet
            return balance
        
        elif diceNum == 2 or diceNum == 3 or diceNum == 12:
            balace += 0
        
        else:
            #true/flase for if a number is rerolled
            pastNumber = False

            while pastNumber == False:
                newNum = dicetotal()
                if newNum == diceNum:
                    pastNumber == True
                    balance += 2 * bet
                    break
                elif newNum == 7:
                    balance - 2 * bet
                    pastNumber = True
                    break
                else:
                    pastNumber = False
