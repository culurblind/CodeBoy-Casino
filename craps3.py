import random
import time
import os
#craps

#prints given string slowly
#default delay of 0.1s if no delay peramter is given
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

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2



slow_print("welcome to Craps! Your goal is to see whether the dice will roll a winning number. In the first round,")
slow_print("if you roll a 7 or 11, you win. If you roll a 2, 3, or 12, you automatically lose")
slow_print("any other combination of values will be added to the point, and you will continue rerolling until you get that number again or roll a 7, in which you lose")
time.sleep(1)
clear_terminal()


balance = 1000
gameplay = True


while gameplay == True:
    time.sleep(1)
    clear_terminal()

    # Balance/ Betting set up
    slow_print("Balance: " + str(balance))
    bet = input("How much do you want to bet? ")
    # makes sure the bet is an int
    while isnt_int(bet):
        slow_print("You need to type a number as a valid bet")
        time.sleep(1.5)
        clear_terminal()
        bet = input("How much do you want to bet? ")
    bet = int(bet)
    balance -= bet
    # condition if person bets more money than they have
    while balance < 0:
        slow_print("You do not have that much money")
        balance += bet
        slow_print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet

    diceNum = dicetotal()
    nextStep = input("Type roll! ")
    if nextStep == "roll":
        slow_print("Rolling... Rolling... Rolling... ", 0.1)
        if diceNum == 7 or diceNum == 11:
            slow_print("The dice rolled " + str(diceNum) + ", You won!")
            balance += 2 * bet
        elif diceNum == 2 or diceNum == 3 or diceNum == 12:
            slow_print("You lost the bet, the dice rolled " + str(diceNum))
        else:

            print("you rolled " + str(diceNum) + " the die will reroll")
            #true/flase for if a number is rerolled
            pastNumber = False

            print()
            while pastNumber == False:
                time.sleep(0.55)
                newNum = dicetotal()
                if newNum == diceNum:
                    slow_print("You rerolled " + str(diceNum) + " again! You win!")
                    pastNumber == True
                    balance += 2 * bet
                    break
                elif newNum == 7:
                    slow_print("You rolled a 7! You have lost the game")
                    balance - 2 * bet
                    pastNumber = True
                    break
                else:
                    slow_print("You rolled, " + str(newNum) + " the dice will roll again")
            
            slow_print("balance: " + str(balance))

    else:
        print("You did not type roll")

    print()
    status = input("Do you want to play again? (y/n) ")
    statusLoop = True

    while statusLoop:
        if status == "y":
            statusLoop = False
        elif status == "n":
            gameplay = False
            statusLoop = False
            slow_print("Thanks for playing craps!")
        else:
            slow_print("Type y or n")
        

