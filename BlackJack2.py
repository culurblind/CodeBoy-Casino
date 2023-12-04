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
                print("dealer's card: " + str(dealerCard))
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
                print("dealer total: " + str(dealerCard))
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
                        print("Dealer total = " + str(dealerSum))
                        if "A" in dealerHand and dealerSum > 21:
                            dealerSum -= 10
                            dealerHand.remove("A")
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
                    print("first split: " + str(splitCard1))
                    sum1 = card1Val + splitCard1Val
                    print("total for first split: " + str(sum1))
                    splitDecision1 = input("stand, hit? ")
                    while splitDecision1 == "hit":
                        extraCard = cardKeys[random.randint(0, 12)]
                        splitHand1.append(extraCard)
                        print(extraCard)
                        extraCardVal = cards.get(extraCard)
                        sum1 += extraCardVal
                        print("total = " + str(sum1))
                        if sum1 > 21:
                            if "A" in splitHand1:
                                sum1 -= 10
                                splitHand1.remove("A")
                            else:
                                print("bust")
                                splitDecision1 = "stand"
                                sum1 = 0
                                break
                        if sum1 == 21:
                            splitDecision1 = "stand"
                        else:
                            splitDecision1 = input("stand, hit ")
                        
                    if splitDecision1 == "stand":
                        splitCard2 = cardKeys[random.randint(0, 12)]
                        splitHand2.append(splitCard2)
                        splitCard2Val = cards.get(splitCard2)
                        print("second split: " + str(splitCard2))
                        sum2 = card2Val + splitCard2Val
                        print("total for second cards: " + str(sum2))
                        splitDecision2 = input("stand, hit? ")
                        while splitDecision2 == "hit":
                            extraCard = cardKeys[random.randint(0, 12)]
                            splitHand2.append(extraCard)
                            print(extraCard)
                            extraCardVal = cards.get(extraCard)
                            sum2 += extraCardVal
                            print("total = " + str(sum2))
                            if sum2 > 21:
                                if "A" in splitHand2:
                                    sum2 -= 10
                                    splitHand2.remove("A")
                                else:
                                    print("bust")
                                    sum2 = 0
                                    if sum1 == 0:
                                        dealerCard = cardKeys[random.randint(0, 12)]
                                        dealerHand.append(dealerCard)
                                        dealerCardVal = cards.get(dealerCard)
                                        dealerSum += dealerCardVal
                                        print("dealer's card: " + str(dealerCard))
                                        print("dealer total: " + str(dealerSum))
                                        print("dealer won")
                                        turn = False
                                    else:
                                        splitDecision2 = "stand"
                                    break
                            elif sum2 == 21:
                                splitDecision2 = "stand"
                            else:
                                splitDecision2 = input("stand or hit? ")
                            
                        if splitDecision2 == "stand":
                            while dealerSum < 17:
                                dealerCard = cardKeys[random.randint(0, 12)]
                                dealerHand.append(dealerCard)
                                dealerCardVal = cards.get(dealerCard)
                                print("dealer's card: " + str(dealerCard))
                                dealerSum += dealerCardVal
                                print("dealer total: " + str(dealerSum))
                                time.sleep(0.5)
                            if dealerSum > 21:
                                if "A" in dealerHand and dealerSum > 21:
                                    dealerSum -= 10
                                    dealerHand.remove("A")
                                else:
                                    print("dealer bust")
                                    balance += 4*bet
                                    turn = False
                            else:
                                if dealerSum > sum1:
                                    print("dealer won against split 1")
                                    turn = False
                                if dealerSum > sum2:
                                    print("dealer won against split 2")
                                    turn = False
                                if dealerSum < sum1:
                                    print("split 1 wins")
                                    if sum1 == 21:
                                        balance += 2.5*bet
                                        balance = int(balance)
                                    else:
                                        balance += 2*bet
                                    turn = False
                                if dealerSum < sum2:
                                    if sum2 == 21:
                                        balance += 2.5*bet
                                        balance = int(balance)
                                    else:
                                        balance += 2*bet
                                    print("split 2 wins")
                                    turn = False
                                if dealerSum == sum1:
                                    print("push")
                                    balance += bet
                                    turn = False
                                if dealerSum == sum2:
                                    print("push")
                                    balance += 2*bet
                                    turn = False
            else:
                print("your cards are not the same, you can not split")
