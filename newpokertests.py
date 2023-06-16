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


class ThreeOfAKindTest(unittest.TestCase):
    def test_three_4(self):
        cards = [
            Card("SPADE", "4"),
            Card("HEART", "4"),
            Card("CLUB", "4"),
            Card("SPADE", "6"),
            Card("SPADE", "7"),
        ]
        three_fours = Hand(cards)
        self.assertEqual(three_fours.three_of_a_kind(), "4 three of a kind")

    def false_three_4(self):
        cards = [
            Card("SPADE", "4"),
            Card("HEART", "4"),
            Card("CLUB", "3"),
            Card("SPADE", "6"),
            Card("SPADE", "7"),
        ]
        false_three = Hand(cards)
        self.assertEqual(false_three.three_of_a_kind(), False)

    def test_three_4(self):
        cards = [
            Card("SPADE", "7"),
            Card("HEART", "4"),
            Card("CLUB", "4"),
            Card("SPADE", "6"),
            Card("CLUB", "10"),
            Card("SPADE", "4"),
        ]
        three_fours = Hand(cards)
        self.assertEqual(three_fours.three_of_a_kind(), "4 three of a kind")


class TwoPairTest(unittest.TestCase):
    def test_aces_twos(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "A"),
            Card("CLUB", "2"),
            Card("SPADE", "2"),
            Card("SPADE", "7"),
        ]
        aces_twos = Hand(cards)
        self.assertEqual(aces_twos.two_pair(), "A and 2 two pair")

    def test_aces_three(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "A"),
            Card("CLUB", "3"),
            Card("SPADE", "7"),
            Card("SPADE", "3"),
            Card("SPADE", "10"),
        ]
        aces_threes = Hand(cards)
        self.assertEqual(aces_threes.two_pair(), "A and 3 two pair")

    def test_false_two_pair1(self):
        cards = [
            Card("SPADE", "A"),
            Card("HEART", "A"),
            Card("CLUB", "3"),
            Card("SPADE", "7"),
            Card("SPADE", "2"),
            Card("SPADE", "10"),
        ]
        false_two_pair = Hand(cards)
        self.assertEqual(false_two_pair.two_pair(), False)

    def test_false_two_pair2(self):
        cards = []
        false_two_pair = Hand(cards)
        self.assertEqual(false_two_pair.two_pair(), False)


class OnePairTest(unittest.TestCase):
    def test_twos(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "2"),
            Card("CLUB", "3"),
            Card("SPADE", "7"),
            Card("SPADE", "9"),
            Card("SPADE", "10"),
        ]
        one_pair_twos = Hand(cards)
        self.assertEqual(one_pair_twos.one_pair(), "2 pair")


class HighCard(unittest.TestCase):
    def test_high_card(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "2"),
            Card("CLUB", "3"),
            Card("SPADE", "7"),
            Card("SPADE", "9"),
            Card("HEART", "10"),
        ]
        one_pair_twos = Hand(cards)
        self.assertEqual(one_pair_twos.high_card(), "HEART 10 high card")

    def test_false_high_card(self):
        cards = []
        empty = Hand(cards)
        self.assertEqual(empty.high_card(), False)


class BestHand(unittest.TestCase):
    def test_best_hand_straight(self):
        cards = [
            Card("SPADE", "2"),
            Card("HEART", "3"),
            Card("SPADE", "4"),
            Card("SPADE", "5"),
            Card("SPADE", "6"),
        ]
        five_high_straight = Hand(cards)
        self.assertEqual(five_high_straight.straight(), "Straight with 6 SPADE high")


if __name__ == "__main__":
    unittest.main()
