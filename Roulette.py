#Roulette
import random
import time
import os
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
    "Row" : 3,
    "Dozen" : 3,
    "Odd" : 2,
    "Even" : 2,
    "Red" : 2,
    "Black" : 2,
    "Low" : 2,
    "High" : 2
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

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

balance = 1000

#Welcome Statement
clear_terminal()
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
        clear_terminal()
        slow_print("Slow your roll there pal, you don't have " + str(bet) + ".")
        balance += bet
        slow_print("Your balance is: " + str(balance))
        slow_print("How much do you want to bet? ")
        bet = int(input())
        balance -= bet

    clear_terminal()

    #Friendly Banter
    if balance == 0:
        slow_print("Wow, we have a real risk taker here!")

    #Initialize type of roulette bet
    slow_print("You have " + str(bet) + " on the line.")
    slow_print("How would you like to bet: ")
    typeOfBet = input('''
    Straight Up, Split, Street, Corners, Six-Line Bet, 
    Row,  Dozen, Odd, Even,  Red, Black, Low (1 -18), High (19-36)

    ''')

    placeHolder = True
    while (placeHolder):
        if (bets.get(typeOfBet) == None):
            clear_terminal()
            slow_print("That is not a valid bet")
            typeOfBet = input('''
            Please Choose Again:
                Straight Up, Split, Street, Corners, Six-Line Bet, 
                Row,  Dozen, Odd, Even,  Red, Black, Low (1 -18), High (19-36)
                              
            ''')
            print()
        else:
            placeHolder = False
    
    clear_terminal()

    #get number for Straight Up bet
    if (typeOfBet == "Straight Up"):
        isInt = False
        while(isInt == False):
            Straight_Up = int(input("Which number between 0 and 36 would you like to bet on? "))
            if Straight_Up >= 0 and Straight_Up <= 36:
                isInt = True
            else:
                print("That is not a valid roullete number.")
                print()

    #get number for Split bet
    if typeOfBet == "Split":
        isInt = False
        while(isInt == False):
            slow_print("Which two numbers would you like to bet on that are")
            slow_print("directly next to eachother vertically or horizontally? (EX: '8 11')")
            print('''3   6   9   12  15  18  21  24  27  30  33  36
2   5   8   11  14  17  20  23  26  29  32  35
1   4   7   10  13  16  19  22  25  28  31  34
                  ''')
            split = input().split(" ")

            if len(split) > 2 or int(split[0]) > 36  or int(split[0]) < 1 or int(split[0]) > 36  or int(split[0]) < 1:
                if abs(int(split[0]) - int(split[1])) != 3 or abs(int(split[0]) - int(split[1])) != 3:
                    clear_terminal()
                    print("Those are not valid roullete numbers.")
                    print() 
            else:
                print()
                isInt = True

    if typeOfBet == "Row":
        isInt = False
        while isInt == False:
            slow_print("Which row would you like to bet on? (Top, Bottom, or Middle)")
            print('''3   6   9   12  15  18  21  24  27  30  33  36
2   5   8   11  14  17  20  23  26  29  32  35
1   4   7   10  13  16  19  22  25  28  31  34''')
            row = input()
            
            if row != "Top" and row != "Middle" and row != "Bottom":
                clear_terminal()
                print("That is not a valid Row bet.")
        
            else:
                isInt = True
                clear_terminal()

    #get number for Dozen bet
    if typeOfBet == "Dozen":
        isInt = False
        while isInt == False:
            slow_print("Which Dozen set would you like to bet on: ")
            slow_print("Please enter either 'First' (1-12), 'Second' (13-24), or 'Third' (24-36)")
            dozen = input()

            if dozen != "First" and dozen != "Second" and dozen != "Third":
                clear_terminal()
                print("Those are not valid roulette numbers.")
            
            else:
                isInt = True
                clear_terminal()
                

    #roullete wheel simulation
    slow_print("Alright, betting " + typeOfBet)
    slow_print( "Time to Roll")
    print()
    slow_print("Rolling... Rolling... Rolling... ", 0.2)
    print()
    value = randint(0, 37)
    slow_print(str(value) + " " + str(wheel[value]))
    print()
    
    #Results for Straight Up bet
    if typeOfBet == "Straight Up":
        if value == Straight_Up:
            win = True

    #Results for Split bet
    if typeOfBet == "Split":
        if value == int(split[0]) or value == int(split[1]):
            win = True

    #Results for Row bet
    if typeOfBet == "Row":
        if row == "Top" and value % 3 == 0:
            win = True
        elif row == "Middle" and (value + 1) % 3 == 0:
            win = True
        elif row == "Bottom" and (value + 2) % 3 == 0:
            win = True

    #Results for Dozen bet
    if typeOfBet == "Dozen":
        if value >= 13 and value <= 24 and dozen == "Second":
            win = True
        elif value >= 1 and value <= 12 and dozen == "First":
            win = True
        elif value >= 25 and dozen == "Third":
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

    #Results for Red or Black bet
    if wheel[value] == typeOfBet:
            win = True

    #Results for Low bet
    if typeOfBet == "Low":
        if value >= 1 and value <= 18:
            win = True

    #Results for High bet
    if typeOfBet == "High":
        if value >= 19:
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
    slow_print("Would you like to play again? Y or N ")
    if input() == "N":
        slow_print("Are you really sure? You might win it big. Y or N ")
        if input() == "N":
            slow_print("Are you 100 percent sure? Y or N ")
            if input() == "N":
                slow_print("Fine. Come back any time!")
                break
    else:
        clear_terminal()
        slow_print("Great choice!")
        slow_print("Your balance is " + str(balance) + ".")