### Util functions
from poker import *


def is_straight(card_list):
    """
    If is straight, returns the highest card. Else, returns None

    >>> card_list1 = [Card('A', 'spades'), Card('2', 'spades'), Card('3', 'spades') ,Card('4', 'hearts') ,Card('5', 'spades')]
    >>> is_straight(card_list1)
    Card('5', 'spades', value=5.4, hidden=False, picture=True)
    >>> card_list2 = [Card('A', 'spades'), Card('2', 'spades'), Card('3', 'spades') ,Card('4', 'hearts') ,Card('6', 'spades')]
    >>> is_straight(card_list2)
    """
    if len(card_list) != 5:
        print("Need length 5 cards")
        return None
    else:
        card_list.sort()
        if int(card_list[4].value) - int(card_list[0].value) == 4:
            return card_list[4]
        else:
            return None


def get_straight(card_list):
    """
    If list of cards has a straight, return list of cards with the strongest straight. O(nlog(n)) time.

    >>> card_list1 = [Card('A', 'spades'), Card('2', 'spades'), Card('3', 'spades') ,Card('4', 'hearts') ,Card('5', 'spades')]
    >>> get_straight(card_list1)
    [Card('A', 'spades', value=1.4, hidden=False, picture=True), Card('2', 'spades', value=2.4, hidden=False, picture=True), Card('3', 'spades', value=3.4, hidden=False, picture=True), Card('4', 'hearts', value=4.3, hidden=False, picture=True), Card('5', 'spades', value=5.4, hidden=False, picture=True)]
    >>> card_list2 = [Card('A', 'spades'), Card('7', 'spades'), Card('3', 'spades') ,Card('4', 'hearts') ,Card('5', 'hearts') , Card('2', 'hearts'),Card('J', 'hearts')]
    >>> get_straight(card_list2)
    [Card('A', 'spades', value=1.4, hidden=False, picture=True), Card('2', 'hearts', value=2.3, hidden=False, picture=True), Card('3', 'spades', value=3.4, hidden=False, picture=True), Card('4', 'hearts', value=4.3, hidden=False, picture=True), Card('5', 'hearts', value=5.3, hidden=False, picture=True)]
    >>> card_list3 = [Card('A', 'spades'), Card('2', 'spades'), Card('3', 'spades') ,Card('4', 'hearts') ,Card('6', 'hearts') , Card('6', 'hearts'),Card('7', 'hearts')]
    >>> get_straight(card_list3)
    [Card('3', 'spades', value=3.4, hidden=False, picture=True), Card('4', 'hearts', value=4.3, hidden=False, picture=True), Card('6', 'hearts', value=6.3, hidden=False, picture=True), Card('6', 'hearts', value=6.3, hidden=False, picture=True), Card('7', 'hearts', value=7.3, hidden=False, picture=True)]
    >>> card_list4 = []
    >>> get_straight(card_list4)
    Need 5 cards or more
    """
    if len(card_list) < 5:
        print("Need 5 cards or more")
    else:
        card_list.sort()
        for i in range(len(card_list), 4, -1):
            five_cards = card_list[i - 5 : i]
            highest_in_straight = is_straight(five_cards)
            if highest_in_straight is not None:
                return five_cards
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
