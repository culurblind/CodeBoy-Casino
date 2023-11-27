#Roulette
import random
import time

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

balance = 1000

while game_over == False:
    while round_over == False:

        # bet
        print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet

        typeOfBet = input('''
        Pick A Bet:
            Straight Up , Split , Street , Corners , Six-Line Bet , 
            Column , Dozen , Odd , Even , Red , Black , 1-18 , 19-36
        ''')

        placeHolder = True
        while (placeHolder):
            if (bets.get(typeOfBet) == None):
                print("That is not a valid bet")
                typeOfBet = input('''
                Pick A Bet:
                    Straight Up , Split , Street , Corners , Six-Line Bet , 
                    Column , Dozen , Odd , Even , Red , Black , 1-18 , 19-36
                ''')
            else:
                placeHolder = False
        
        if balance <= 0:
            print("You ran out of money, game over.")
            game_over = True
