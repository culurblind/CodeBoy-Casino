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
    # double ace case
    if card1 == "A" and card2 == "A":
        sum -= 10
        playerHand.remove("A")
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
            balance = int(balance)
        elif dealerSum == 21:
            print("Push")
            balance += bet
        else:
            balance += 2.5 * bet
            balance = int(balance)
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
                print("dealer's card: " + str(dealerExtraCard))
                if "A" in dealerHand and dealerSum > 21:
                    dealerSum -= 10
                    dealerHand.remove("A")
                print("Dealer total = " + str(dealerSum))
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
        
        # case 2 - hit
        elif decision == "hit":
            extraCard = cardKeys[random.randint(0, 12)]
            playerHand.append(extraCard)
            print(extraCard)
            extraCardVal = cards.get(extraCard)
            sum += extraCardVal
            if sum > 21:
                if "A" in playerHand:
                    sum -= 10
                    playerHand.remove("A")
                else:
                    print("bust")
                    turn = False
            print("total = " + str(sum))
            if sum == 21:
                dealerCard = cardKeys[random.randint(0, 12)]
                dealerHand.append(dealerCard)
                dealerCardVal = cards.get(dealerCard)
                print("dealer's card: " + str(dealerCard))
                dealerSum += dealerCardVal
                print("dealer total: " + str(dealerCardVal))
                if dealerCard == 21:
                    print("push")
                    balance += bet
                else:
                    print("you win")
                    balance += 2*bet
                    balance = int(balance)
                turn = False
        
        # case 3 - double (only if us have enough to double)
        elif decision == "double":
            balance -= bet
            if balance < 0:
                print("don't have the money to double")
                balance += bet
            else:
                bet *= 2
                extraCard = cardKeys[random.randint(0, 12)]
                print(extraCard)
                playerHand.append(extraCard)
                extraCardVal = cards.get(extraCard)
                sum += extraCardVal
                print("total = " + str(sum))
                time.sleep(0.25)
                if sum > 21:
                    if "A" in playerHand:
                        sum -= 10
                        playerHand.remove("A")
                    else:
                        print("bust")
                        turn = False
                elif sum == 21:
                    dealerCard = cardKeys[random.randint(0, 12)]
                    dealerHand.append(dealerCard)
                    dealer_card_val = cards.get(dealerCard)
                    print("dealer's card: " + str(dealerCard))
                    dealerSum += dealer_card_val
                    print("dealer total: " + str(dealerSum))
                    if dealerSum == 21:
                        print("push")
                        balance += bet
                        balance = int(balance)
                    else:
                        print("you win")
                        balance += 2*bet
                    turn = False
                else:
                    while dealerSum < 17:
                        dealerExtraCard = cardKeys[random.randint(0, 12)]
                        dealerHand.append(dealerExtraCard)
                        dealerExtraCardVal = cards.get(dealerExtraCard)
                        dealerSum += dealerExtraCardVal
                        print("dealer's card: " + str(dealerCard))
                        if "A" in dealerHand and dealerSum > 21:
                            dealerSum -= 10
                            dealerHand.remove("A")
                        print("Dealer total = " + str(dealerSum))
                        time.sleep(0.5)
                    if dealerSum > 21:
                        print("dealer bust")
                        balance += 2*bet
                    elif dealerSum > sum:
                        print("dealer won")
                    elif dealerSum < sum:
                        print("you win")
                        balance += 2*bet
                    else:
                        print("push")
                        balance += bet
                    turn = False        
        
        #case 4 - split
        elif decision == "split":
            if card1Val == card2Val:
                balance -= bet
                if balance < 0:
                    print("don't have the money to split")
                    balance += bet
                else:
                    print("balance: " + str(balance))
                    splitHand1 = []
                    splitHand2 = []
                    splitHand1.append(card1)
                    splitHand2.append(card2)
                    
                    splitCard1 = cardKeys[random.randint(0, 12)]
                    splitHand1.append(splitCard1)
                    splitCard1Val = cards.get(splitCard1)
                    sum1 = card1Val + splitCard1Val

                    splitCard2 = cardKeys[random.randint(0, 12)]
                    splitHand2.append(splitCard2)
                    splitCard2Val = cards.get(splitCard2)
                    sum2 = card2Val + splitCard2Val

                    print("first split: " + splitCard1)
                    print("first split total: " + str(sum1))
                    print("second split: " + splitCard2)
                    print("first split total: " + str(sum2))

                    splitTurn1 = True
                    splitTurn2 = False
                    dealerReveal = False

                    while (splitTurn1):
                        if sum1 == 21:
                            print("Black Jack!")
                            dealerReveal = True
                            splitTurn1 = False
                            splitTurn2 = True
                        elif sum1 > 21:
                            print("split 1 busts")
                            splitTurn1 = False
                            splitTurn2 = True
                        else:
                            splitDecision = input("Split 1: hit or stand? ")
                            if splitDecision == "hit":
                                extraCard1 = cardKeys[random.randint(0, 12)]
                                splitHand1.append(extraCard1)
                                extraCard1Val = cards.get(extraCard1)
                                sum1 += extraCard1Val
                                print("split 1 card: " + extraCard1)
                                if sum1 > 21:
                                    if "A" in splitHand1:
                                        sum -= 10
                                        playerHand.remove("A")
                                    else:
                                        print("split 1 busts")
                                        splitTurn1 = False
                                        splitTurn2 = True
                                print("total = " + str(sum1))
                                if sum1 == 21:
                                    dealerReveal = True
                                    splitTurn1 = False
                                    splitCard2 = True

                            elif splitDecision == "stand":
                                dealerReveal = True
                                splitTurn1 = False
                                splitTurn2 = True
                        
                        while (splitTurn2):
                            if sum2 == 21:
                                print("Black Jack!")
                                dealerReveal = True
                                splitTurn2 = False
                            elif sum2 > 21:
                                print("split 2 busts")
                                splitTurn2 = False
                            else:
                                splitDecision = input("Split 2: hit or stand? ")
                                if splitDecision == "hit":
                                    extraCard2 = cardKeys[random.randint(0, 12)]
                                    splitHand2.append(extraCard2)
                                    extraCard2Val = cards.get(extraCard2)
                                    sum2 += extraCard2Val
                                    print("split 1 card: " + extraCard1)
                                    if sum1 > 21:
                                        if "A" in splitHand2:
                                            sum -= 10
                                            playerHand.remove("A")
                                        else:
                                            print("split 2 busts")
                                            splitTurn2 = False
                                    print("total = " + str(sum2))
                                    if sum2 == 21:
                                        dealerReveal = True
                                        splitCard2 = False
                                elif splitDecision == "stand":
                                    dealerReveal = True
                                    splitTurn2 = False
                            
                        if (dealerReveal):
                            while dealerSum < 17:
                                dealerExtraCard = cardKeys[random.randint(0, 12)]
                                dealerHand.append(dealerExtraCard)
                                dealerExtraCardVal = cards.get(dealerExtraCard)
                                dealerSum += dealerExtraCardVal
                                print()
                                print("dealer's card: " + str(dealerCard))
                                if "A" in dealerHand and dealerSum > 21:
                                    dealerSum -= 10
                                    dealerHand.remove("A")
                                print("Dealer total = " + str(dealerSum))
                                time.sleep(0.5)

                            if dealerSum > 21:
                                print("Dealer Bust!")
                                if sum1 <= 21:
                                    balance += bet
                                if sum2 <= 21:
                                    balance += 2*bet

                            if dealerSum > sum1:
                                print("first split loses")
                            elif dealerSum < sum1:
                                print("first split wins")
                                balance += 2*bet
                            else:
                                print("first split pushes")
                                balance += bet

                            if dealerSum > sum2:
                                print("second split loses")
                            elif dealerSum < sum2:
                                print("second split wins")
                                balance += 2*bet
                            else:
                                print("second split pushes")
                                balance += bet

                        turn = False

            else:
                print("your cards are not the same, you can not split")
