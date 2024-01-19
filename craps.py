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
#true/flase for if a number is rerolled
pastNumber = False
list = []

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

#instance when first roll doesn't end game
def reRoll():
    dicetotal
    while pastNumber == False:
        print("you rolled" + dicetotal + "the die will reroll")
        if dicetotal == list:
            print("You rerolled" + list +"again! You win!")
            pastNumber == True
        if dicetotal == 7:
            print("You rolled a 7! You have lost the game")
            pastNumber == True

#runs game
while gameplay == True:
    dicetotal()
    if dicetotal == 7 or 11:
        print("The dice rolled" + dicetotal + ", You won!")
        gameplay = False
    if dicetotal == 2 or 3 or 12:
        print("You lost the bet, the dice rolled" + dicetotal)
        gameplay = False
    else:
        list = input(dicetotal)
        reRoll()
        gameplay == False