
class Player:
    """
    A Player of the game.
    """
    def __init__(self):
        #Includes the Player's hand, the player's name
    def get_num_cards(self):
        #Return the number of cards the Player has
    def get_hand(self):
        #Return the Hand of the Player
    


class Dealer(Player):
    """
    Inherits the Player class.
    """
    


class Card:
    """
    A Card.
    """
    def __init__(self, suit, rank):
        #Has suit and rank. Also has suit value and rank value

    

class Deck:
    """
    A Deck. Starts off with 52 cards. 
    """
    def __init__(self):
        
    def shuffle(self):
        #Shuffles the deck
    def draw(self):
        #Pops a card from the top of the deck

        


class Hand:
    """
    The Hand.
    """


class Game:
    """
    The Game.
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player()
        self.dealer =  Dealer()

    def deal_card(self):
