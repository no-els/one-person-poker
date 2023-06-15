import random
import newutils


class Player:
    """
    A Player of the game.
    >>> player = Player('Devin', [])
    >>> player.get_name()
    'Devin'
    >>> player.get_num_cards()
    0
    """

    def __init__(self, name, card_list=[]):
        # Includes the Player's hand, the Player's name
        self.name = name
        self.hand = Hand(card_list)

    def get_num_cards(self):
        # Return the number of cards the Player has
        return self.hand.get_num_cards()

    def get_hand(self):
        # Return the Hand of the Player
        return self.hand

    def get_name(self):
        # Return Player's name
        return self.name

    def add_to_hand(self, card):
        self.hand.add_card(card)

    def print_hand(self):
        self.hand.print_hand()


class Dealer(Player):
    """
    Inherits the Player class.
    """


class Card:
    """
    A Card.

    >>> card = Card('HEART', '3')
    >>> print(card)
    HEART 3
    >>> card2 = Card('HEART', '3')
    >>> card == card2
    True
    """

    suit_values = {"DIAMOND": 0.001, "CLUB": 0.002, "HEART": 0.003, "SPADE": 0.004}

    rank_values = {
        "2": 0.01,
        "3": 0.02,
        "4": 0.03,
        "5": 0.04,
        "6": 0.05,
        "7": 0.06,
        "8": 0.07,
        "9": 0.08,
        "10": 0.09,
        "J": 0.1,
        "Q": 0.11,
        "K": 0.12,
        "A": 0.13,
    }

    def __init__(self, suit, rank):
        # Has suit and rank. Also has suit value and rank value.
        if suit not in Deck.suits:
            raise Exception("suit must be one of the following: " + Deck.suits)
        if rank not in Deck.ranks:
            raise Exception("rank must be one of the following: " + Deck.ranks)
        self.suit = suit
        self.rank = rank
        self.id = suit + rank

    def __str__(self):
        return self.suit + " " + self.rank

    def __eq__(self, other):
        if isinstance(other, Card):
            return other.id == self.id

    def get_suit_value(self):
        return self.suit_values[self.suit]

    def get_rank_value(self):
        return self.rank_values[self.rank]


class Deck:
    """
    A Deck. Starts off with 52 cards.

    >>> deck = Deck()
    >>> card = deck.draw()
    >>> print(card)
    DIAMOND 2
    >>> deck.get_num_cards()
    51
    """

    suits = ["SPADE", "HEART", "CLUB", "DIAMOND"]
    ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.cards)

    def draw(self):
        # Pops a card from the top of the deck
        return self.cards.pop()

    def get_num_cards(self):
        return len(self.cards)

    def print_deck(self):
        for card in self.cards:
            print(card)


class Hand:
    """
    A Hand of Cards for a Player.
    >>> hand = Hand(card_list=[])
    >>> hand.get_num_cards()
    0
    >>> spadesA = Card("SPADE", "A")
    >>> hand.add_card(spadesA)
    >>> hand.print_hand()
    SPADE A
    >>>
    """

    def __init__(self, card_list=[]):
        # implement checks
        self.cards = []
        self.suit_to_rank_dict = {
            "DIAMOND": set(),
            "CLUB": set(),
            "HEART": set(),
            "SPADE": set(),
        }
        self.rank_to_suit_dict = {
            "2": set(),
            "3": set(),
            "4": set(),
            "5": set(),
            "6": set(),
            "7": set(),
            "8": set(),
            "9": set(),
            "10": set(),
            "J": set(),
            "Q": set(),
            "K": set(),
            "A": set(),
        }
        for card in card_list:
            self.add_card(card)

    def get_num_cards(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.suit_to_rank_dict[card.suit].add(card.rank)
        self.rank_to_suit_dict[card.rank].add(card.suit)

    def print_hand(self):
        for card in self.cards:
            print(card)

    def straight_flush(self):
        # If hand has straight flush, then return string describing flush
        if self.get_num_cards() < 5:
            return False
        else:
            for suit in Deck.suits:
                ranks = self.suit_to_rank_dict[suit]
                card = newutils.get_straight_from_set(ranks)
                if card:
                    return suit + " Royal Flush with " + card + " high"
            return False

    def four_of_a_kind(self):
        # If hand has four of a kind, then return string describing best four of a kind. Else, return False.
        if self.get_num_cards() < 5:
            return False
        else:
            for rank in Deck.ranks:
                if len(self.rank_to_suit_dict[rank]) == 4:
                    return rank + " 4 of a kind"
            return False

    def full_house(self):
        # If hand has full house, then return string describing best full house.
        if self.get_num_cards() < 5:
            return False
        else:
            for rank in Deck.ranks:
                if len(self.rank_to_suit_dict[rank]) == 3:
                    for double_rank in Deck.ranks:
                        if double_rank != rank:
                            if len(self.rank_to_suit_dict[double_rank]) == 2:
                                return rank + " over " + double_rank + " Full House"
            return False

    def flush(self):
        # If hand has flush, then return string describing best flush.
        if self.get_num_cards() < 5:
            return False
        else:
            for suit in Deck.suits:
                ranks = self.suit_to_rank_dict[suit]
                if len(ranks) > 4:
                    return (
                        newutils.highest_rank(list(ranks)) + " high " + suit + " flush"
                    )
            return False

    def straight(self):
        # If hand has straight, then return string describing best straight
        ranks_present = []
        for rank in Deck.ranks:
            if len(self.rank_to_suit_dict[rank]) > 0:
                ranks_present.append(rank)
        highest = newutils.get_straight_from_set(set(ranks_present))
        if highest:
            suits = self.rank_to_suit_dict[highest]
            if "SPADE" in suits:
                return "Straight with " + highest + " SPADE high"
            if "HEART" in suits:
                return "Straight with " + highest + " HEART high"
            if "CLUB" in suits:
                return "Straight with " + highest + " CLUB high"
            if "DIAMOND" in suits:
                return "Straight with " + highest + " DIAMOND high"
            else:
                raise Exception("Something weird in the dictionary")
        else:
            return False


class Game:

    """
    The Game.
    >>> game = Game()
    >>> game.one_round([Card('SPADE', 'A')])
    >>> game.player.print_hand()
    SPADE A
    >>> game.dealer.get_num_cards() + game.player.get_num_cards() + game.deck.get_num_cards() == 52
    True
    """

    def __init__(self, player_name="devin", dealer_name="gaga"):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(player_name, card_list=[])
        self.dealer = Dealer(dealer_name, card_list=[])

    def deal_card(self, card_requests):
        # Takes in card_requests, a list of cards requested
        card_drawn = self.deck.draw()
        if card_drawn in card_requests:
            self.player.add_to_hand(card_drawn)
            return True
        else:
            self.dealer.add_to_hand(card_drawn)
            return False

    def one_round(self, card_requests):
        # Takes in card_requests, a set of cards requested, and deals cards until the player gets a card
        while True:
            if self.deal_card(card_requests) == True:
                break


if __name__ == "__main__":
    import doctest

    doctest.testmod()
