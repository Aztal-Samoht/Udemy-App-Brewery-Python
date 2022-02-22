# print('hello world!')
import random
class Hand:
    name = ''
    cards = {}
    total = 0
    count = 0
    def __init__(self, name):
        self.name = name
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
        for x in self.cards:
            to_print += str(self.cards[x])
        to_print += '\n\ntotal: ' + str(self.total) + '\n'
        return to_print

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
        return 'name: ' + str(self.name) + '\nsuit: ' + self.suit + '\nvalue: ' + str(self.value) + '\n'
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
    print(a_hand.name + ' now holds:\n' + str(a_hand))
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

def deal_hands():
    card_is_new = False
    card_to_deal = 0
    dealing_to_player = True
    left_to_deal = 4
    while left_to_deal > 0:
        while not card_is_new:
            card_to_deal = random.randint(1,52)
            if card_to_deal not in the_deck.delt_cards:
                card_is_new = True
        the_deck.delt_cards.append(card_to_deal)
        if dealing_to_player:
            player_hand.add(the_deck.deck[card_to_deal])
            dealing_to_player = not dealing_to_player
        else:
            dealer_hand.add(the_deck.deck[card_to_deal])
            dealing_to_player = not dealing_to_player
        left_to_deal -= 1
#End Methods ======================================================================================
the_deck = Deck()
the_deck.build_deck()
# print(the_deck)

player_hand = Hand('player hand')
dealer_hand = Hand('dealer hand')

aCard = Card('A', 'H')
aCard.ace_is_one()
print(aCard)
aCard.ace_is_eleven()
print(aCard)

deal_a_ten(player_hand)
deal_a_ten(player_hand)
deal_an_ace(player_hand)


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
