#Roulette
import random
import time
from random import randint

game_over = False
round_over = False

wheel = {
    0 : "Green",
    1 : "Black",
    2 : "Red",
    3 : "Black",
    4 : "Black",
    5 : "Red",
    6 : "Black",
    7 : "Red",
    8 : "Black",
    9 : "Red",
    10 : "Black",
    11 : "Black",
    12 : "Red",
    13 : "Black",
    14 : "Red",
    15 : "Black",
    16 : "Red",
    17 : "Black",
    18 : "Red",
    19 : "Red",
    20 : "Black",
    21 : "Red",
    22 : "Black",
    23 : "Red",
    24 : "Black",
    25 : "Red",
    26 : "Black",
    27 : "Red",
    28 : "Black",
    29 : "Black",
    30 : "Red",
    31 : "Black",
    32 : "Red",
    33 : "Black",
    34 : "Red",
    35 : "Black",
    36 : "Red"
}

bets = {
    "Straight Up" : 36,
    "Split" : 18,
    "Street" : 12,
    "Corners" : 9,
    "Six-Line Bet" : 6,
    "Column" : 3,
    "Dozen" : 3,
    "Odd" : 2,
    "Even" : 2,
    "Red" : 2,
    "Black" : 2,
    "1-18" : 2,
    "19-36" : 2
}

#prints given string slowly
#default delay of 0.1s if no delay peramter is given
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.05

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#returns true if given value is an int
def is_int(variable):
    return isinstance(variable, int)

balance = 1000

#Welcome Statement
slow_print("Welcome to the Roulette table.")
slow_print("You have a balance of: " + str(balance))

#Main roulette game
while game_over == False:
    
    win = False

    #Betting
    slow_print("How much do you want to bet? ")
    bet = int(input())
    print()
    balance -= bet

    #Loop if the bet exceeds balance
    while (balance < 0):
        slow_print("Slow your roll there pal, you don't have that much money.")
        balance += bet
        slow_print("Your balance is: " + str(balance))
        slow_print("How much do you want to bet? ")
        bet = int(input())
        balance -= bet

    #Friendly Banter
    if balance == 0:
        slow_print("Wow, we have a real risk taker here!")

    #Initialize type of roulette bet
    typeOfBet = input('''
    Pick Your Bet:
        Straight Up, Split, Street, Corners, Six-Line Bet, 
        Column,  Dozen, Odd, Even,  Red, Black, '1-18', '19-36'
    ''')
    print()


    placeHolder = True
    while (placeHolder):
        if (bets.get(typeOfBet) == None):
            slow_print("That is not a valid bet")
            typeOfBet = input('''
            Please Bet Again:
                Straight Up, Split, Street, Corners, Six-Line Bet, 
                Column,  Dozen, Odd, Even,  Red, Black, '1-18', '19-36'
            ''')
            print()
        else:
            placeHolder = False

    if (typeOfBet == "Straight Up"):
        isInt = False
        while(isInt == False):
            Straight_Up = int(input("Which number between 0 and 36 would you like to bet on? "))
            if Straight_Up >= 0 and Straight_Up <= 36:
                isInt = True
            else:
                print("That is not a valid roullete number.")
                print()

    #roullete wheel simulation
    print("Time to Roll")
    print()
    slow_print("Rolling... Rolling... Rolling... ", 0.1)
    print()
    value = randint(0, 36)
    print(value, wheel[value])
    print()
    
    #Results for Straight Up bet
    if typeOfBet == "Straight Up":
        if value == Straight_Up:
            win = True

    #Results for Odd bet
    if typeOfBet == "Odd":
        if value != 0:
            if value % 2 != 0:
                win = True
    
    #Results for Even bet
    if typeOfBet == "Even":
        if value % 2 == 0:
            win = True

    #Results for win
    if win:
        profit = (bet * bets.get(typeOfBet))
        balance += profit
        slow_print("You won " + str(profit) + ", your balance is now " + str(balance) + "!")
    
    #Results for loss
    if win == False:
        if balance <= 0:
            slow_print("Better luck next time, you're out of money bud.")
            game_over = True
            break
        else:
            slow_print("Tough luck, house wins. You still have " + str(balance) + " left in your balance.", 0.05)

    #Play again? prompt
    slow_print("Would you like to play again? Y or N - ")
    if input() == "N":
        slow_print("Are you really sure? You might win it big. Y or N - ")
        if input() == "N":
            slow_print("Are you 100 percent sure? Y or N - ")
            if input() == "N":
                slow_print("Fine. Come back any time!")
                break
    else:
        slow_print("Great choice!")
        print()





