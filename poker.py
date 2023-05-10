from terminal_playing_cards import Deck
from terminal_playing_cards import View
from terminal_playing_cards import Card as tpc_Card

SUITS = ["spades", "hearts", "diamonds", "clubs"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card(tpc_Card):
    def __init__(self, rank, suit, value=0):
        super().__init__(rank, suit, value)

    def __eq__(self, card):
        return (card.face == self.face) and (card.suit == self.suit)


class Dealer:
    """
    need to implement dictionary
    """

    def __init__(self):
        self.hand = []
        self.suit_dict = dict()
        self.rank_dict = dict()
        for suit in SUITS:
            self.suit_dict[suit] = []
        for rank in RANKS:
            self.rank_dict[rank] = []

    def show_hand(self):
        print(View(self.hand))

    def add_card(self, card):
        self.hand.append(card)


class Player:
    """
    need to implement dictionary
    """

    def __init__(self):
        self.hand = []
        self.suit_dict = dict()
        self.rank_dict = dict()
        self.requested_cards = []
        for suit in SUITS:
            self.suit_dict[suit] = []
        for rank in RANKS:
            self.rank_dict[rank] = []

    def show_hand(self):
        print(View(self.hand))

    def add_card(self, card):
        self.hand.append(card)


class Game:
    def __init__(self):
        player = Player()
        dealer = Dealer()
        deck = Deck()
        deck.shuffle()

    def take_card(self, text):
        rank = text[0]
        suit = text[1:]
        if rank not in RANKS:
            print("Invalid rank. Please specify something from:")
            print(RANKS)
            return None
        if suit not in SUITS:
            print("Invalid rank. Please specify something from:")
            print(SUITS)
            return None
        return Card(rank, suit)

    def take_cards(self):
        """
        Takes in cards from input from the user and returns a list of cards
        """
        text = input(
            "Give me the card you'd like to take this turn, in the form of RANKSUIT, separated by commas \n"
        )
        card_list_string = text.split(",")
        print(card_list_string)
        card_list = [self.take_card(card) for card in card_list_string]
        print(View(card_list))
        return card_list

    def draw(self, card_list):
        """
        Draws a card from the deck, and
        """
        card = self.deck.pop()


game = Game()
game.take_cards()
