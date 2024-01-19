import random
import time
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

slow_print("welcome to Craps! Your goal is to see whether the dice will roll a winning number. In the first round,")
slow_print("if you roll a 7 or 11, you win. If you roll a 2, 3, or 12, you automatically lose")
slow_print("any other combination of values will be added to the point, and you will continue rerolling until you get that number again or roll a 7, in which you lose")
gameplay = True
list = []

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

#instance when first roll doesn't end game
def reRoll():
    diceNum
    while pastNumber == False:
        print("you rolled " + dicetotal + " the die will reroll")
        if diceNum == list:
            slow_print("You rerolled " + str(list) + " again! You win!")
            pastNumber == True
        if diceNum == 7:
            slow_print("You rolled a 7! You have lost the game")
            pastNumber == True

#runs game
while gameplay == True:
    diceNum = dicetotal()

    nextStep = input("Type roll! ")
    if nextStep == "roll":
        slow_print("Rolling... Rolling... Rolling... ", 0.2)
        if diceNum == 7 or diceNum == 11:
            slow_print("The dice rolled " + str(diceNum) + ", You won!")
            gameplay = False
        elif diceNum == 2 or diceNum == 3 or diceNum == 12:
            slow_print("You lost the bet, the dice rolled " + str(diceNum))
            gameplay = False
        else:
            list = input(diceNum)
            #true/flase for if a number is rerolled
            pastNumber = False
            reRoll()
            gameplay == False
    else:
        print("You did not type roll")