import unittest
from main import Card, Deck, Player


class TestDeck(unittest.TestCase):


    def test_build(self):

        deck = [
            "Two of Hearts",
            "Three of Hearts",
            "Four of Hearts",
            "Five of Hearts",
            "Six of Hearts",
            "Seven of Hearts",
            "Eight of Hearts",
            "Nine of Hearts",
            "Ten of Hearts",
            "Jack of Hearts",
            "Queen of Hearts",
            "King of Hearts",
            "Ace of Hearts",
            "Two of Diamonds",
            "Three of Diamonds",
            "Four of Diamonds",
            "Five of Diamonds",
            "Six of Diamonds",
            "Seven of Diamonds",
            "Eight of Diamonds",
            "Nine of Diamonds",
            "Ten of Diamonds",
            "Jack of Diamonds",
            "Queen of Diamonds",
            "King of Diamonds",
            "Ace of Diamonds",
            "Two of Spades",
            "Three of Spades",
            "Four of Spades",
            "Five of Spades",
            "Six of Spades",
            "Seven of Spades",
            "Eight of Spades",
            "Nine of Spades",
            "Ten of Spades",
            "Jack of Spades",
            "Queen of Spades",
            "King of Spades",
            "Ace of Spades",
            "Two of Clubs",
            "Three of Clubs",
            "Four of Clubs",
            "Five of Clubs",
            "Six of Clubs",
            "Seven of Clubs",
            "Eight of Clubs",
            "Nine of Clubs",
            "Ten of Clubs",
            "Jack of Clubs",
            "Queen of Clubs",
            "King of Clubs",
            "Ace of Clubs",
        ]

        mydeck = Deck()
        mydeck_name = []
        for card in mydeck.cards:
            mydeck_name.append(f"{card.rank} of {card.suit}")
        self.assertEqual(deck, mydeck_name)


if __name__ == "__main__":
    unittest.main()