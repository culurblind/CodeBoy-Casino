import random
import time

cards = {
    "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11
}
cardKeys = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

balance = 1000

while balance > 0:
    # initial bet
    print("balance: " + str(balance))
    bet = int(input("How much do you want to bet? "))
    balance -= bet
    # condition if person bets more money than they have
    while balance < 0:
        print("You do not have that much money")
        balance += bet
        print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet

    # player hand
    playerHand = []
    card1 = cardKeys[random.randint(0, 12)]
    card2 = cardKeys[random.randint(0, 12)]
    playerHand.append(card1)
    playerHand.append(card2)
    card1Val = cards.get(card1)
    card2Val = cards.get(card2)
    sum = card1Val + card2Val
    print(card1)
    print(card2)
    print("total = " + str(sum))
    print()
    time.sleep(1)

    # dealer hand
    dealerHand = []
    dealerCard = cardKeys[random.randint(0, 12)]
    dealerHand.append(dealerCard)
    dealerCard1Val = cards.get(dealerCard)
    dealerSum = dealerCard1Val
    print("Dealer Card: " + dealerCard)
    print("Dealer total = " + str(dealerSum))
    
    turn = False

    # case 1 - black jack
    if sum == 21:
        print("Black Jack!")
        # dealer chance
        while dealerSum < 17:
            dealerExtraCard = cardKeys[random.randint(0, 12)]
            dealerHand.append(dealerExtraCard)
            dealerExtraCardVal = cards.get(dealerExtraCard)
            dealerSum += dealerExtraCardVal
            print("Dealer Card: " + dealerExtraCard)
            print("Dealer total = " + str(dealerSum))
            if "A" in dealerHand and dealerSum > 21:
                dealerSum -= 10
                dealerHand.remove("A")
            time.sleep(0.5)
        if dealerSum > 21:
            print("Dealer Bust")
            balance += 2.5 * bet
        elif dealerSum == 21:
            print("Push")
            balance += bet
        else:
            balance += 2.5 * bet
    else:
        # if it is not a black jack give the options
        turn = True

    while turn:
        decision = input("stand, hit, double, or split? ")

        # case 2 - stand
        if decision == "stand":
            while dealerSum < 17:
                dealerExtraCard = cardKeys[random.randint(0, 12)]
                dealerHand.append(dealerExtraCard)
                dealerExtraCardVal = cards.get(dealerExtraCard)
                dealerSum += dealerExtraCardVal
                print("Dealer total = " + str(dealerSum))
                if "A" in dealerHand and dealerSum > 21:
                    dealerSum -= 10
                    dealerHand.remove("A")
                time.sleep(0.5)
            if dealerSum > 21:
                print("Dealer Bust")
                balance += 2 * bet
            elif dealerSum == sum:
                print("Push")
                balance += bet
            elif dealerSum < sum:
                print("You Win!")
                balance += 2 * bet
            elif dealerSum > sum:
                print("Dealer Wins")
            turn = False

