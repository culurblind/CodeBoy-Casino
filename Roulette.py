#Roulette
import random
import time
from random import randint

game_over = False
round_over = False

wheel = {
    0 : "G",
    1 : "B",
    2 : "R",
    3 : "B",
    4 : "B",
    5 : "R",
    6 : "B",
    7 : "R",
    8 : "B",
    9 : "R",
    10 : "B",
    11 : "B",
    12 : "R",
    13 : "B",
    14 : "R",
    15 : "B",
    16 : "R",
    17 : "B",
    18 : "R",
    19 : "R",
    20 : "B",
    21 : "R",
    22 : "B",
    23 : "R",
    24 : "B",
    25 : "R",
    26 : "B",
    27 : "R",
    28 : "B",
    29 : "B",
    30 : "R",
    31 : "B",
    32 : "R",
    33 : "B",
    34 : "R",
    35 : "B",
    36 : "R"
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

def print_slow(str):
        for letter in str:
            print(letter)
            time.sleep(.2)

balance = 1000

while game_over == False:

    if balance <= 0:
        print("don't have that much money game over")
        game_over = True
        break
    
    # bet
    print("balance: " + str(balance))
    bet = int(input("how much do you want to bet? "))
    balance -= bet
    while (balance < 0):
        print("You do not have that much money")
        balance += bet
        print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet

    typeOfBet = input('''
    Pick A Bet:
        Straight Up , Split , Street , Corners , Six-Line Bet , 
        Column , Dozen , Odd , Even , Red , Black , 1-18 , 19-36
    ''')
    print()

    placeHolder = True
    while (placeHolder):
        if (bets.get(typeOfBet) == None):
            print("That is not a valid bet")
            typeOfBet = input('''
            Pick A Bet:
                Straight Up , Split , Street , Corners , Six-Line Bet , 
                Column , Dozen , Odd , Even , Red , Black , 1-18 , 19-36
            ''')
            print()
        else:
            placeHolder = False

    if (typeOfBet ==  "Straight Up"):
        isInt = False
        while(isInt == False):
            Straight_Up = int(input("Which number between 0 and 36 would you like to bet on? "))
            if Straight_Up >= 0 and Straight_Up <= 36:
                isInt = True
            else:
                print("That is not a valid roullete number.")
                print()

    if balance <= 0:
        print("don't have that much money game over")
        game_over = True

    #roullete wheel simulation
    print("Time to Roll")
    print_slow("Rolling... Rolling...")
    print()
    value = randint(0, 1)
    print(value, wheel[value])

    #Straight Up win condition
    if (typeOfBet == "Straight Up"):
        if value == Straight_Up:
            profit = (bet * 36)
            balance += profit
            print("You won " + str(profit))

    #if typeOfBet == 





