"""
Let"s play black jack using python
"""
from random import shuffle

# set up all the necessary material for the game
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
          "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 10, "Queen": 10, "King": 10,
          "Ace": 11}


# set up the class Card
class Card:
    """
    Build a class card
    """
    def __init__(self, suit, rank):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# set up the class Deck
class Deck:
    """
    A deck is composed by 52 cards
    """
    def __init__(self):
        self.cards = Deck.build()

    @classmethod
    def build(cls):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        return deck

    def shuffle_cards(self):
        """shuffle cards"""
        return shuffle(self.cards)

    def deal_one(self):
        """get one card from the deck"""
        return self.cards.pop(0)

# set up the Player
class Player:
    """
    Here we will define a player or an automated dealer
    a player can hit or stay
    """

    def __init__(self, name, role, chips=0):
        self.name = name
        self.role = role
        self.chips = chips
        self.cards = []


    def tally_cards(self):
        """
        totalize player card value
        an Ace can take as value 1 or 11
        """
        value = 0
        for card in self.cards:
            value += values[card.rank]
        if "Ace" in [card.rank  for card in self.cards] and value > 21:
            return value - 10
        return value

    def player_move(self):
        """
        get the player move
        """
        move = ""
        while move  not in ["Hit", "Stand"]:
            move = input("Hit or Stand?:  ")
        return move

    def play_again(self):
        """
        ask the player if he want to play again
        """
        replay = ""
        while replay  not in ["Yes", "No"]:
            replay = input("want to play again? Yes or No ")
            if self.chips <= 5:
                print("Sorry, but you don't have enough chips to bet!")
                return False
        if replay == "Yes":
            return True
        return False


class BoardGame():
    """
    setting up a round
    """

    def __init__(self, bet, player_number=1):
        self.player_number=player_number
        self.bet = bet

    def set_initial_cards(self, player, dealer, deck):
        """
        distribute two cards for the player and the dealer
        """
        for _ in range(2):
            player.cards.append(deck.deal_one())
            dealer.cards.append(deck.deal_one())
        return(player.cards, dealer.cards[0])

    def display_card(self, user):
        """Show player card"""
        if user.role == "guest":
             print(f"{user.name}, your cards are: ")
             print(",".join([f"{card.rank} of {card.suit}" for card in
                             user.cards]))
        else:
            print(f" MrWhite : My first card is {user.cards[0]}")


    def win_check(self, player, dealer):
         """Check who win the round"""
         if player.tally_cards() > 21:
             player.chips -= bet
             print(f"Bust!  you have lost. Current wage {player.chips}")
         elif player.tally_cards() == 21:
             player.chips +=  2/3*(self.bet)
             print(f"wow! you have got a Black Jack! current wage : {player.chips}")
         elif dealer.tally_cards() == 21:
             player.chips -= bet
             print("Black Jack for the dealer! You have lost!")
         elif player.tally_cards() > dealer.tally_cards():
             player.chips += self.bet
             print( f"You win, current wage {player.chips}")
         else:
             player.chips -= bet
             print(f"You have  lost! current wage {player.chips}")

class Round:
    """
     set up a round
    """
    def __init__(self, deck, player, dealer):
        deck.cards.extend(player.cards)
        player.cards = []
        deck.cards.extend(dealer.cards)
        dealer.cards = []
        deck.shuffle_cards()


if __name__=="__main__":
    # logic game
    # Ask if they want to play a round?
    print(f"Hey! this is a Blackjack Game")
    print(
        """
          Blackjack, or twenty-one,
          Card game whose object is to be dealt cards having a higher count
          than those of the dealer, up to but not exceeding 21.
          --britannica.com--

          In this first version:

          There will be one automated dealer called MrWhite
          and one player called Romeo The cat
          The player is able to Hit or Stand
        """
     )
    ready = ""
    game_on = False
    while ready not in ["Yes", "No" ]:
        ready  = input("How about to  play a round? : Yes or No " )

    if ready == "Yes":
        game_on = True
        deck = Deck()
        player_one = Player(name="Romeo", role="guest", chips=42)
        dealer = Player(name="MrWhite", role="dealer")
        bet = 44
        while bet > player_one.chips:
            bet = int(input(
                f"""
                    MrWhite :
                    Romeo, your current chips is {player_one.chips}.
                    How much do you want to bet?  """))
    else:
        print("Thank you, Bye then!")


    # start a round
    while game_on:
        board = BoardGame(bet=bet)
        Round(deck=deck, player=player_one,dealer=dealer)
        board.set_initial_cards(player=player_one, dealer=dealer,
                                deck=deck)
        board.display_card(player_one)
        board.display_card(dealer)
        move = player_one.player_move()
        while move == "Hit":
            player_one.cards.append(deck.deal_one())
            board.display_card(player_one)
            move = player_one.player_move()
        else:
            for card in dealer.cards:
                print(card)
            board.win_check(player=player_one, dealer=dealer)
        if not player_one.play_again():
            game_on = False
