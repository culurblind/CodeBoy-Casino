#BlackJack
import random
import time

# game over variable
game_over = False


# mapping cards to numerical values
def values(val):
    if val == "2":
        return 2
    if val == "3":
        return 3
    if val == "4":
        return 4
    if val == "5":
        return 5
    if val == "6":
        return 6
    if val == "7":
        return 7
    if val == "8":
        return 8
    if val == "9":
        return 9
    if val == "10":
        return 10
    if val == "J":
        return 10
    if val == "Q":
        return 10
    if val == "K":
        return 10
    if val == "A":
        return 11

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]



balance = 1000
while game_over == False:
    # bet
    print("balance: " + str(balance))
    bet = int(input("how much do you want to bet? "))
    balance -= bet
    # condition if person bets more money than they have
    while (balance < 0):
        print("You do not have that much money")
        balance += bet
        print("balance: " + str(balance))
        bet = int(input("how much do you want to bet? "))
        balance -= bet

    # lists of hands    
    hand = []
    dealer_hand = []
    
    # players cards
    card1 = cards[random.randint(0, 12)]
    print(card1)
    hand.append(card1)
    card2 = cards[random.randint(0, 12)]
    print(card2)
    hand.append(card2)
    card1_val = values(card1)
    card2_val = values(card2)
    sum = card1_val + card2_val
    print("total = " + str(sum))
    time.sleep(1)
    
    # dealers cards
    dealer_card = cards[random.randint(0, 12)]
    dealer_card_val = values(dealer_card)
    dealer_sum = dealer_card_val
    print("dealer's card: " + str(dealer_card))
    dealer_hand.append(dealer_card)
    turn = False
    
    # case - black jack
    if sum == 21:
        print("black jack")
        dealer_card = cards[random.randint(0, 12)]
        dealer_card_val = values(dealer_card)
        print("dealer's card: " + str(dealer_card))
        dealer_sum += dealer_card_val
        print("dealer total: " + str(dealer_sum))
        if dealer_sum == 21:
            # dealer gets a black jack too
            print("push")
            balance += bet
        else:
            print("you win")
            balance += 2.5*bet
            balance = int(balance)
    else:
        turn = True
    
    if turn == True:
        while turn == True:
            decision = input("stand, hit, double, or split? ")
            # case 1 - stand
            if decision == "stand":
                while dealer_sum < 17:
                    dealer_card = cards[random.randint(0, 12)]
                    dealer_hand.append(dealer_card)
                    dealer_card_val = values(dealer_card)
                    print("dealer's card: " + str(dealer_card))
                    dealer_sum += dealer_card_val
                    print("dealer total: " + str(dealer_sum))
                    time.sleep(0.5)
                if dealer_sum > 21:
                    if "A" in dealer_hand:
                        dealer_sum -= 10
                        dealer_hand.remove("A")
                        print("dealer total: " + str(dealer_sum))
                        print("Type stand")
                    else:
                        print("dealer bust")
                        balance += 2*bet
                        turn = False
                elif dealer_sum > sum:
                    print("dealer won")
                    turn = False
                elif dealer_sum < sum:
                    print("you win")
                    balance += 2*bet
                    turn = False
                else:
                    print("push")
                    balance += bet
                    turn = False
            # case 2 - hit
            elif decision == "hit":
                extra_card = cards[random.randint(0, 12)]
                print(extra_card)
                extra_card_val = values(extra_card)
                hand.append(extra_card)
                sum += extra_card_val
                if sum > 21:
                    if "A" in hand:
                        sum -= 10
                        hand.remove("A")
                    else:
                        print("bust")
                        turn = False
                print("total = " + str(sum))
                if sum == 21:
                    dealer_card = cards[random.randint(0, 12)]
                    dealer_hand.append(dealer_card)
                    dealer_card_val = values(dealer_card)
                    print("dealer's card: " + str(dealer_card))
                    dealer_sum += dealer_card_val
                    print("dealer total: " + str(dealer_sum))
                    if dealer_sum == 21:
                        print("push")
                        balance += bet
                        turn = False
                    else:
                        print("you win")
                        balance += 2.5*bet
                        balance = int(balance)
                        turn = False
            # case 3 - double (only if us have enough to double)
            elif decision == "double":
                balance -= bet
                if balance < 0:
                    print("don't have the money to double")
                    balance += bet
                else:
                    bet = bet * 2
                    extra_card = cards[random.randint(0, 12)]
                    print(extra_card)
                    hand.append(extra_card)
                    extra_card_val = values(extra_card)
                    sum += extra_card_val
                    print("total = " + str(sum))
                    time.sleep(0.25)
                    if sum > 21:
                        if "A" in hand:
                            sum -= 10
                            hand.remove("A")
                        else:
                            print("bust")
                            turn = False
                    elif sum == 21:
                        dealer_card = cards[random.randint(0, 12)]
                        dealer_hand.append(dealer_card)
                        dealer_card_val = values(dealer_card)
                        print("dealer's card: " + str(dealer_card))
                        dealer_sum += dealer_card_val
                        print("dealer total: " + str(dealer_sum))
                        if dealer_sum == 21:
                            print("push")
                            balance += bet
                            balance = int(balance)
                            turn = False
                        else:
                            print("you win")
                            balance += 2*bet
                            turn = False
                    else:
                        while dealer_sum < 17:
                            dealer_card = cards[random.randint(0, 12)]
                            dealer_hand.append(dealer_card)
                            dealer_card_val = values(dealer_card)
                            print("dealer's card: " + str(dealer_card))
                            dealer_sum += dealer_card_val
                            print("dealer total: " + str(dealer_sum))
                            time.sleep(0.5)
                        if dealer_sum > 21:
                            if "A" in dealer_hand:
                                dealer_sum -= 10
                                dealer_hand.remove("A")
                                print("dealer total: " + str(dealer_sum))
                                print("Type stand")
                            else:
                                print("dealer bust")
                                balance += 2*bet
                                turn = False
                        elif dealer_sum > sum:
                            print("dealer won")
                            turn = False
                        elif dealer_sum < sum:
                            print("you win")
                            balance += 2*bet
                            turn = False
                        else:
                            print("push")
                            balance += bet
                            turn = False
            # case 4 - split (if 2 cards have same numerical value)
            elif decision == "split":
                if card1_val == card2_val:
                    balance -= bet
                    if balance < 0:
                        print("don't have the money to split")
                        balance += bet
                    else:
                        split_hand1 = []
                        split_hand2 = []
                        split_hand1.append(card1)
                        split_hand2.append(card2)
                        
                        split_card1 = cards[random.randint(0, 12)]
                        split_hand1.append(split_card1)
                        split_card1_val = values(split_card1)
                        print("first split: " + str(split_card1))
                        sum1 = card1_val + split_card1_val
                        print("total for first split: " + str(sum1))
                        split_decision1 = input("stand, hit ")
                        while split_decision1 == "hit":
                            extra_card = cards[random.randint(0, 12)]
                            split_hand1.append(extra_card)
                            print(extra_card)
                            extra_card_val = values(extra_card)
                            sum1 += extra_card_val
                            print("total = " + str(sum1))
                            if sum1 > 21:
                                if "A" in split_hand1:
                                    sum1 -= 10
                                    split_hand1.remove("A")
                                else:
                                    print("bust")
                                    split_decision1 = "stand"
                                    sum1 = 0
                                    break
                            elif sum1 == 21:
                                split_decision1 = "stand"
                            split_decision1 = input("stand, hit ")
                        if split_decision1 == "stand":
                            split_card2 = cards[random.randint(0, 12)]
                            split_hand2.append(split_card2)
                            split_card2_val = values(split_card2)
                            print("second split: " + str(split_card2))
                            sum2 = card2_val + split_card2_val
                            print("total for second cards: " + str(sum2))
                            split_decision2 = input("stand, hit ")
                            while split_decision2 == "hit":
                                extra_card = cards[random.randint(0, 12)]
                                split_hand2.append(extra_card)
                                print(extra_card)
                                extra_card_val = values(extra_card)
                                sum2 += extra_card_val
                                print("total = " + str(sum2))
                                if sum2 > 21:
                                    if "A" in split_hand2:
                                        sum2 -= 10
                                        split_hand2.remove("A")
                                    else:
                                        print("bust")
                                        sum2 = 0
                                        if sum1 == 0:
                                            dealer_card = cards[random.randint(0, 12)]
                                            dealer_hand.append(dealer_card)
                                            dealer_card_val = values(dealer_card)
                                            dealer_sum += dealer_card_val
                                            print("dealer's card: " + str(dealer_card))
                                            print("dealer total: " + str(dealer_sum))
                                            print("dealer won")
                                            turn = False
                                        else:
                                            split_decision2 = "stand"
                                        break
                                elif sum2 == 21:
                                    split_decision2 = "stand"
                                split_decision2 = input("stand or hit? ")
                            if split_decision2 == "stand":
                                while dealer_sum < 17:
                                    dealer_card = cards[random.randint(0, 12)]
                                    dealer_hand.append(dealer_card)
                                    dealer_card_val = values(dealer_card)
                                    print("dealer's card: " + str(dealer_card))
                                    dealer_sum += dealer_card_val
                                    print("dealer total: " + str(dealer_sum))
                                    time.sleep(0.5)
                                if dealer_sum > 21:
                                    if "A" in dealer_hand:
                                        dealer_sum -= 10
                                        dealer_hand.remove("A")
                                        print("dealer total: " + str(dealer_sum))
                                        print("Type stand")
                                    else:
                                        print("dealer bust")
                                        balance += 4*bet
                                        turn = False
                                else:
                                    if dealer_sum > sum1:
                                        print("dealer won against split 1")
                                        turn = False
                                    if dealer_sum > sum2:
                                        print("dealer won against split 2")
                                        turn = False
                                    if dealer_sum < sum1:
                                        print("split 1 wins")
                                        if sum1 == 21:
                                            balance += 2.5*bet
                                            balance = int(balance)
                                            turn = False
                                        else:
                                            balance += 2*bet
                                            turn = False
                                    if dealer_sum < sum2:
                                        if sum2 == 21:
                                            balance += 2.5*bet
                                            balance = int(balance)
                                            turn = False
                                        else:
                                            balance += 2*bet
                                            turn = False
                                        print("split 2 wins")
                                        balance += 2*bet
                                        turn = False
                                    if dealer_sum == sum1:
                                        print("push")
                                        balance += bet
                                        turn = False
                                    if dealer_sum == sum2:
                                        print("push")
                                        balance += 2*bet
                                        turn = False
                else:
                    print("your cards are not the same, you can not split")
        if balance <= 0:
            print("don't have that much money game over")
            game_over = True



