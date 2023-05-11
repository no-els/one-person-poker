from terminal_playing_cards import Deck
from terminal_playing_cards import View
from terminal_playing_cards import Card as tpc_Card

SUITS = ["spades", "hearts", "diamonds", "clubs"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card(tpc_Card):
    def __init__(self, rank, suit, value=0):
        rank_dictionary = {
            "A": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "J": 10,
            "Q": 11,
            "K": 12,
        }
        super().__init__(rank, suit, value=rank_dictionary[rank])

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

    def best_hand(self):
        """
        Returns the best hand that the Dealer has
        """
        if len(self.hand) < 5:
            print("Less than 5 cards")
        else:
            s


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
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()

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
        card_list = [self.take_card(card) for card in card_list_string]
        print("Cards requested: \n")
        print(View(card_list))
        return card_list

    def draw(self, card_list):
        """
        Draws a card from the deck, and if the card is in the card_list, then the card is added to
        to the player. Otherwise, it goes to the dealer. Returns True if dealt to player. Otherwise False
        """
        card = self.deck.pop()
        print("Card drawn \n")
        print(View([card]))
        if card in card_list:
            self.player.add_card(card)
            print("Player's hand \n")
            self.player.show_hand()
            print("Dealer's hand \n")
            self.dealer.show_hand()
            return True
        else:
            self.dealer.add_card(card)
            print("Player's hand \n")
            self.player.show_hand()
            print("Dealer's hand \n")
            self.dealer.show_hand()
            return False

    def draw_until_player(self, card_list):
        while True:
            if len(self.deck) == 0:
                print("Out of cards! Dealer wins \n")
                break
            if self.draw(card_list) == True:
                break

    def is_straight(self, card_list):
        """
        If is straight, returns the highest card
        """
        if len(card_list) != 5:
            print("Need length 5 cards")
        else:
            card_list.sort()


game = Game()
card_list = game.take_cards()

game.draw_until_player(card_list)
