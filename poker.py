from terminal_playing_cards import Deck as tpc_Deck
from terminal_playing_cards import View
from terminal_playing_cards import Card as tpc_Card


SUITS = ["spades", "hearts", "diamonds", "clubs"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card(tpc_Card):
    def __init__(self, rank, suit, value=0):
        rank_value_dict = {
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

        suit_value_dict = {"diamonds": 0.1, "clubs": 0.2, "hearts": 0.3, "spades": 0.4}
        super().__init__(
            rank, suit, value=rank_value_dict[rank] + suit_value_dict[suit]
        )

    def __eq__(self, card):
        return (card.face == self.face) and (card.suit == self.suit)


# class Deck(tpc_Deck):
#     @staticmethod
#     def _build(specs_dict: dict, **kwargs: bool):
#         """Builds a deck of cards according to specifications."""
#         return [
#             Card(face, suit)
#             for face in specs_dict.keys()
#             for suit in specs_dict.get(face).keys()
#         ]


class Player:
    """
    >>> game = Game()
    >>> player = Player()
    >>> cards = [Card('A', 'spades'), Card('2', 'spades'),Card('3', 'spades'),Card('4', 'spades'),Card('5', 'spades'), Card('6', 'hearts')]
    >>> for i in cards:
    ...     player.add_card(i)
    ...
    >>> player.has_flush()
    Card('5', 'spades', value=5.4, hidden=False, picture=True)
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
        self.suit_dict[card.suit].append(card)
        self.rank_dict[card.face].append(card)

    def has_flush(self):
        # Returns highest card of the best flush if exists. Otherwise, return None.
        largest = Card("3", "diamonds", value=0)
        for suit in self.suit_dict.keys():
            if len(self.suit_dict[suit]) >= 5:
                largest = max(largest, max(self.suit_dict[suit]))
        if largest.value == 0:
            return None
        else:
            return largest

    def best_hand(self):
        """
        Returns the best hand that you have
        """
        if len(self.hand) < 5:
            print("Less than 5 cards")


class Dealer(Player):
    """
    The Dealer.
    """


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
