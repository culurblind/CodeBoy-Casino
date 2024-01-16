import random, string

"""
Casino game, Baccarat:
    there are three choices for users, Player, Tie and Banker. If users choose either player or banker and win
        their money will be doubled. if the rep goes Tie and they had chosen P or B they get a refund.
        otherwise they lose their money. E.g: Kevin bets on player, but Banker wins, he loses his money.
        Kevin bets 100$ on Banker and he wins, he gets 200$.
        Kevin bets on player or banker, bet goes Tie, he gets his 100$ back.
        Kevin bets 100$ on Tie, bet goes Tie, he will get 800$.
    player and banker recieve two cards, if the sum is <= 5, they recieve another card.
        9 is the biggest number in baccarat. if users get a 9, and dealer has 8 or lower number, users win the game.
"""

# list of cards

card_lst = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# value of each card

card_value = {"A": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 0,
              "J": 0,
              "Q": 0,
              "K": 0}

# the range of money that players can bet

money_range = range(1, 10001)


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


player = "p"
banker = "b"
tie = "t"

# How to use

print(color.BOLD + "Guide:\ntype p for Player, t for Tie and b for Banker and q to quit the game" + color.END)
print()


# choose player / tie / banker to bet

while True:
    chosen_input = input("Bet on Player / Tie / Banker: ")
    if chosen_input in ("p", "P"):
        print("you bet on Player")
        break
    elif chosen_input in ("t", "T"):
        print("you bet on Tie")
        break
    elif chosen_input in ("b", "B"):
        print("you bet on Banker")
        break
    elif chosen_input in ("q", "Q"):
        print("Thanks for playing Baccarat.")
        break
    else:
        print(color.RED + "Please type P for Player, T for Tie or B for Banker" + color.END)


# How much money do you want to bet?

def bet_amount():
    while True:
        betamount_input = int(input("How much money do you want to bet on %s: " % chosen_input))
        if betamount_input in money_range:
            print("You bet {} on {}".format(betamount_input, chosen_input))
            break
        elif betamount_input != money_range:
            print("please type a number between 1 and 10,000")
            break
        elif betamount_input in ("q", "Q"):
            print("Thanks for playing Baccarat.")
            break


bet_amount()