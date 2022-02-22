# print('hello world!')
import random

replay = True
playing = True
player_bust = False
blackjack = False

class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = {}
        self.total = 0
        self.count = 0
    def add(self, new_card):
        self.cards[self.count] = new_card
        self.count += 1
        if new_card.number == 'A':
            new_card.ace_is_eleven()
        self.total += int(new_card.value)
        if self.total > 21:
            for x in self.cards:
                if self.cards[x].value == 11:
                    self.cards[x].ace_is_one()
                    break
            self.total = 0
            for x in self.cards:
                self.total += int(self.cards[x].value)

    def __str__(self):
        to_print = ''
        if self.name == 'dealer hand':
            if not playing:
                self.show_dealer_hand()
            else:
                for x in self.cards:
                    if x == 0:
                        to_print += 'down card \n'
                    else:
                        to_print += str(self.cards[x])
                to_print += 'dealer is showing: ' + str(self.total - self.cards[0].value) + '\n\n'
        else:
            for x in self.cards:
                to_print += str(self.cards[x])
            to_print += 'player total: ' + str(self.total) + ''
        return to_print

    def show_dealer_hand(self):
        to_print = 'dealer has:\n'
        for x in self.cards:
            to_print += str(self.cards[x])
        to_print += 'dealer total: ' + str(self.total) + '\n'
        print(to_print)

class Card:
    def __init__(self, name, suit):
        self.suit = suit
        self.name = name + suit
        self.number = name
        if name == 'J' or name == 'Q' or name == 'K':
            self.value = 10
        elif name == 'A':
            self.value = name
        else:
            self.value = int(name)
    def __str__(self):
        if self.value == 'A':
            self.value = '1 or 11'
        return str(self.name) + '\n'
    def ace_is_one(self):
        self.value = 1
    def ace_is_eleven(self):
        self.value = 11

    def sum2Cards(card1, card2):
        if card1.value == 'A' and card2.value == 'A':
            return 12
        elif card1.value == 'A':
            return card2.value + 11
        elif card2.value == 'A':
            return card1.value + 11
        else:
            score = card1.value + card2.value
            if score == 21:
                return 'BLACKJACK!'
            else:
                return score

class Deck:
    deck = {}
    delt_cards = []
    count = 0
    suits = ['S', 'C', 'H', 'D']

    def __str__(self):
        if self.count == 0:
            return 'this deck is empty'
        else:
            str_to_return = ''
            for x in self.deck:
                str_to_return += (str(x) + ':\n' + str(self.deck[x]) + '\n\n')
            return str_to_return

    def build_deck(self):
        self.count += 1
        for n in self.suits:
            self.deck[self.count] = Card('A', n)
            self.count += 1
            for m in range(2, 11):
                self.deck[self.count] = Card(str(m), n)
                self.count += 1
            self.deck[self.count] = Card('J', n)
            self.count += 1
            self.deck[self.count] = Card('Q', n)
            self.count += 1
            self.deck[self.count] = Card('K', n)
            self.count += 1
#End Classes ======================================================================================
def deal_a_card(a_hand):
    print('dealing a card')
    is_card_new = False
    while not is_card_new:
        card_to_deal = random.randint(1, 52)
        if card_to_deal not in the_deck.delt_cards:
            is_card_new = True
            a_hand.add(the_deck.deck[card_to_deal])
            the_deck.delt_cards.append(card_to_deal)
    # print(a_hand.name + ' now holds:\n' + str(a_hand))

def deal_an_ace(a_hand):
    print('dealing an ace')
    card_to_deal = 1
    is_card_new = False
    while not is_card_new:
        if card_to_deal not in the_deck.delt_cards:
            is_card_new = True
            a_hand.add(the_deck.deck[card_to_deal])
            the_deck.delt_cards.append(card_to_deal)
        else:
            card_to_deal += 13
    print(a_hand.name + ' now holds:\n' + str(a_hand))
def deal_a_ten(a_hand):
    print('dealing a ten')
    card_to_deal = 10
    is_card_new = False
    while not is_card_new:
        if card_to_deal not in the_deck.delt_cards:
            is_card_new = True
            a_hand.add(the_deck.deck[card_to_deal])
            the_deck.delt_cards.append(card_to_deal)
        else:
            card_to_deal += 13
    print(a_hand.name + ' now holds:\n' + str(a_hand))
def deal_a_hand(a_hand):
    deal_a_card(a_hand)
    deal_a_card(a_hand)
    print(a_hand.name + ' now holds:\n' + str(a_hand))
def deal_hands():
    deal_a_card(player_hand)
    deal_a_card(dealer_hand)
    deal_a_card(player_hand)
    deal_a_card(dealer_hand)

#End Methods ======================================================================================

while replay:
    the_deck = Deck()
    the_deck.build_deck()

    dealer_hand = Hand('dealer hand')
    deal_a_hand(dealer_hand)

    player_hand = Hand('player hand')
    deal_a_hand(player_hand)



    while playing == True:
        answer = input('hit? (y/n)').lower()
        if answer == 'y':
            deal_a_card(player_hand)
            print('player total: \n' + str(player_hand))
           # print('dealer is showing: ' + str(dealer_hand.total - dealer_hand.cards[0].value) + '\n')
            if player_hand.total > 21:
                print("player bust")
                player_bust = True
                playing = False
            if player_hand.total == 21:
                print("PLAYER HAS 21")
                blackjack = True
                playing = False
        else:
            playing = False
    dealer_hand.show_dealer_hand()


    if player_bust:
        print('Player loses')
    else:
        if dealer_hand.total == 21:
            if blackjack:
                print('push')
            else:
                print('player loses')
        else:
            while dealer_hand.total < 17 and player_hand.total > dealer_hand.total:
                deal_a_card(dealer_hand)
                dealer_hand.show_dealer_hand()
                if dealer_hand.total > 21:
                    print('dealer bust, Player wins!')
            if player_hand.total > dealer_hand.total:
                print('Player wins!')
            if player_hand.total == dealer_hand.total:
                print('push')
            else:
                print('Player loses')
    play_again = input('play again?(y/n)').lower()
    if play_again:
        playing = True
        player_bust = False
        blackjack = False
        print('==============================================')
    else:
        replay = False
# print('player hand:\n' + str(player_hand) + '\n\n')
# print('dealer hand:\n' + str(dealer_hand))





#used Tests
# a = 'a word'
# a += ' can have many leters'
# print(a)
# aCard = Card('A','H')
# print(aCard)
# aDeck = Deck()
# #print(aDeck)
# aDeck.build_deck()
# print('\n')
# print(aDeck)
#
# b = 1
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))
# print(str(random.randint(b,3)))

# a_list = [0,1,3,4,5,]
# if 2 in a_list:
#     print('2 is in the list')
# if 2 not in a_list:
#     print('2 is NOT in the list')
