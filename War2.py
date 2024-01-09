#War
import random
import time
ranks=[2,3,4,5,6,7,8,9,10,'J','K','A','Q']
design =['H','D','S','C']

def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.5 

class Deck:
    def __init__(self):
        print("Creating new ordered deck!!")
        self.cards=[(j,i) for j in design for i in ranks]
    def shuffle(self):
        print("Shuffling Deck")
        random.shuffle(self.cards)
    def split_half(self):
        return (self.cards[:26],self.cards[26:]) 

class Hand:
    def __init__(self,cards_count):
         self.cards_count=cards_count
    def __str__(self):
        return "Contains {} cards".format(len(self.cards_count))
    def add(self,added_cards):
        self.cards_count.extend(added_cards)
    def remove(self):
        return self.cards_count.pop()
class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed : {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards_count)<3:
            return self.hand.cards_count
        else:
            for x in range(3):
                war_cards.append(self.hand.cards_count.pop())
            return war_cards
    def still_has_cards(self):
        """
        Return true if player has cards left
        """
        return len(self.hand.cards_count) != 0
    
slow_print("Welcome to War! Your goal is to hold all the cards in the deck. Each player starts out with half the deck facedown.")
slow_print("At the same time, both players draw a singular card, the player with the hightest values taking all the cards drawn.")
slow_print("If the cards drawn hold the same value and the players tie, each player continues drawing cards until one person wins. This is called a War")

# Create new deck and split it into half
shuffledeck= Deck()
shuffledeck.shuffle()
half1,half2=shuffledeck.split_half()

#Create both players !
comp = Player("Computer",Hand(half1))
name=input("Enter your name")
human = Player(name,Hand(half2))

total_rounds =0
war_count = 0

while human.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    slow_print("Time for a new round")
    slow_print("Here are the current standings")
    slow_print(human.name + "has the count:"+str(len(human.hand.cards_count)))
    slow_print(comp.name + "has the count:"+str(len(comp.hand.cards_count)))
    slow_print("Play a card!")
    slow_print("\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = human.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("War!!")
        table_cards.extend(human.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            human.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            human.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
slow_print("Game over,number of rounds:"+str(total_rounds))
slow_print("A war happened " + str(war_count) +" times")
slow_print("Does the computer still have cards?\t",str(comp.still_has_cards()))
slow_print("Does the Human player still have cards?\t:",str(human.still_has_cards()))