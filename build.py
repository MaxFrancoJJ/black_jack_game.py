import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#create Card object
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

#create Deck object
class Deck():

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp= ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'This deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Create Hand object
class Hand():
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1

#Create chips object
class Chips():

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#function to track bets
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

#function to hit
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#gameplay asking to hit or stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        y = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if y[0].lower() == 'h':
            hit(deck,hand)
        elif y[0].lower() == 's':
            print('Player stands. Dealer playing')
            playing = False
        else:
            print("Sorry, i can't understand, try again")
            continue
        break

#display cards
def show_some(player,dealer):
    print("\nDealer's hand:")
    print("<card hidden>")
    print('', dealer.cards[1])
    print("\n")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card)
    print("\nPlayer's hand:")


#functions to handle different game situations
def player_busts(player, dealer, chips):
    print('Bust player')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Player wins! Dealer BUST!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.win_bet()

def push(player, dealer):
    print('Player and dealer! PUSH')
