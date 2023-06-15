from newpoker import *
from newutils import *
import unittest


class StraightFlushTest(unittest.TestCase):
    def test_spade10JQKA(self):
        cards = [
            Card("SPADE", "A"),
            Card("SPADE", "10"),
            Card("SPADE", "J"),
            Card("SPADE", "Q"),
            Card("SPADE", "K"),
        ]
        AceStraightFlushHand = Hand(cards)
        self.assertEqual(
            AceStraightFlushHand.straight_flush(), "SPADE Royal Flush with A high"
        )

    def test_heartflush1(self):
        cards = [
            Card("HEART", "A"),
            Card("HEART", "2"),
            Card("HEART", "3"),
            Card("HEART", "4"),
            Card("HEART", "5"),
            Card("HEART", "6"),
        ]
        sixStraightFlushHand = Hand(cards)
        self.assertEqual(
            sixStraightFlushHand.straight_flush(), "HEART Royal Flush with 6 high"
        )

    def test_heartflush2(self):
        cards = [
            Card("HEART", "2"),
            Card("HEART", "A"),
            Card("HEART", "3"),
            Card("HEART", "4"),
            Card("HEART", "5"),
            Card("HEART", "6"),
        ]
        sixStraightFlushHand = Hand(cards)
        self.assertEqual(
            sixStraightFlushHand.straight_flush(), "HEART Royal Flush with 6 high"
        )

    def test_falseflush1(self):
        cards = [
            Card("HEART", "A"),
            Card("HEART", "2"),
            Card("HEART", "3"),
            Card("HEART", "5"),
            Card("HEART", "6"),
        ]
        sixStraightFlushHand = Hand(cards)
        self.assertEqual(sixStraightFlushHand.straight_flush(), False)

    def test_falsestraightflush2(self):
        cards = [
            Card("HEART", "A"),
            Card("HEART", "2"),
            Card("SPADE", "3"),
            Card("HEART", "4"),
            Card("HEART", "5"),
            Card("HEART", "6"),
            Card("SPADE", "7"),
        ]
        sixStraightFlushHand = Hand(cards)
        self.assertEqual(sixStraightFlushHand.straight_flush(), False)

    def test_wholedeck(self):
        cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                cards.append(Card(suit, rank))
            deck = Hand(cards)
        self.assertEqual(deck.straight_flush(), "SPADE Royal Flush with A high")


class FourOfAKindTest(unittest.TestCase):
    def test_four_aces(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "A"),
            Card("CLUB", "A"),
            Card("DIAMOND", "A"),
            Card("SPADE", "2"),
        ]
        ace_four_kind = Hand(cards)
        self.assertEqual(ace_four_kind.four_of_a_kind(), "A 4 of a kind")

    def test_four_cards(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "A"),
            Card("CLUB", "A"),
            Card("DIAMOND", "A"),
        ]
        ace_four_kind = Hand(cards)
        self.assertEqual(ace_four_kind.four_of_a_kind(), False)

    def test_best_hand(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "3"),
            Card("CLUB", "A"),
            Card("DIAMOND", "A"),
            Card("SPADE", "3"),
            Card("HEART", "A"),
            Card("CLUB", "3"),
            Card("DIAMOND", "3"),
        ]
        ace_four_kind = Hand(cards)
        self.assertEqual(ace_four_kind.four_of_a_kind(), "A 4 of a kind")


class FullHouseTest(unittest.TestCase):
    def test_3_full_house(self):
        cards = [
            Card("SPADE", "3"),
            Card("HEART", "3"),
            Card("DIAMOND", "3"),
            Card("DIAMOND", "A"),
            Card("SPADE", "A"),
        ]
        three_full_house = Hand(cards)
        self.assertEqual(three_full_house.full_house(), "3 over A Full House")

    def test_2_full_house_more_cards(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "2"),
            Card("DIAMOND", "4"),
            Card("SPADE", "4"),
            Card("DIAMOND", "8"),
            Card("DIAMOND", "9"),
            Card("SPADE", "10"),
            Card("DIAMOND", "2"),
        ]
        two_full_house = Hand(cards)
        self.assertEqual(two_full_house.full_house(), "2 over 4 Full House")

    def test_false_full_house(self):
        cards = [
            Card("SPADE", "2"),
            Card("DIAMOND", "4"),
            Card("SPADE", "4"),
            Card("DIAMOND", "8"),
            Card("DIAMOND", "9"),
            Card("SPADE", "10"),
            Card("DIAMOND", "2"),
        ]
        false_full_house = Hand(cards)
        self.assertEqual(false_full_house.full_house(), False)

    def test_empty_full_house(self):
        cards = []
        empty_full_house = Hand(cards)
        self.assertEqual(empty_full_house.full_house(), False)


class FlushTest(unittest.TestCase):
    def test_spade_flush(self):
        cards = [
            Card("SPADE", "2"),
            Card("SPADE", "4"),
            Card("SPADE", "5"),
            Card("SPADE", "8"),
            Card("SPADE", "9"),
        ]
        nine_high_flush = Hand(cards)
        self.assertEqual(nine_high_flush.flush(), "9")

    def test_spade_flush(self):
        cards = [
            Card("SPADE", "2"),
            Card("SPADE", "4"),
            Card("SPADE", "5"),
            Card("SPADE", "8"),
            Card("SPADE", "9"),
        ]
        nine_high_flush = Hand(cards)
        self.assertEqual(nine_high_flush.flush(), "9 high SPADE flush")

    def test_false_spade(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "4"),
            Card("SPADE", "5"),
            Card("SPADE", "8"),
            Card("SPADE", "9"),
        ]
        nine_high_flush = Hand(cards)
        self.assertEqual(nine_high_flush.flush(), False)


class StraightTest(unittest.TestCase):
    def test_6_straight(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "3"),
            Card("SPADE", "4"),
            Card("SPADE", "5"),
            Card("SPADE", "6"),
        ]
        five_high_straight = Hand(cards)
        self.assertEqual(five_high_straight.straight(), "Straight with 6 SPADE high")

    def test_6_straight_2(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "3"),
            Card("SPADE", "4"),
            Card("SPADE", "5"),
            Card("HEART", "6"),
        ]
        five_high_straight = Hand(cards)
        self.assertEqual(five_high_straight.straight(), "Straight with 6 HEART high")

    def test_6_straight_3(self):
        cards = [
            Card("SPADE", "A"),
            Card("SPADE", "2"),
            Card("HEART", "3"),
            Card("SPADE", "6"),
            Card("SPADE", "4"),
            Card("HEART", "6"),
            Card("HEART", "5"),
        ]
        five_high_straight = Hand(cards)
        self.assertEqual(five_high_straight.straight(), "Straight with 6 SPADE high")

    def test_false_straight(self):
        cards = [
            Card("SPADE", "A"),
            Card("SPADE", "2"),
            Card("HEART", "3"),
            Card("SPADE", "6"),
        ]
        five_high_straight = Hand(cards)
        self.assertEqual(five_high_straight.straight(), False)


if __name__ == "__main__":
    unittest.main()
