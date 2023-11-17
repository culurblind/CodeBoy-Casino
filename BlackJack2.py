import random
import time

# mapping cards to numerical values


# linking cards to numerial values+
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


game_over = False
balance = 1000

while game_over == False:
    #bet
    print("balance: " + str(balance))
    bet = int(input("how much do you want to bet? "))
    balance -= bet
    
    hand = []
    dealer_hand = []
    
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

        