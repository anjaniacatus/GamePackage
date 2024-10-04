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
        """
        a class method to build a deck
        """
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        return deck

    def __str__(self):

       deck_comp = ""
       for card in self.cards:
           deck_comp += "\n" + card.__str__()
       return f"The deck has: {deck_comp}"

    def shuffle_cards(self):
        """shuffle cards"""
        return shuffle(self.cards)

    def deal_one(self):
        """get one card from the deck"""
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

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


    def values(self):
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

    def set_move(self):
        """
        get the player move
        """
        move = ""
        while move  not in ["Hit", "Stand"]:
            move = input(f"{self.name}, Hit or Stand?:  ")
        return move

    def play_again(self):
        """
        ask the player if he want to play again
        the player should also have enough chips to bet
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

    def __init__(self, player_number=1):
        self.player_number=player_number
        self.bet = 44
        self.reset = False

    def set_bet_amount(self, player_chips):
        bet = 44
        if self.reset:
             bet = int(input("How much chips do you want to bet?: "))
        while bet > player_chips:
            bet = int(input("How much chips do you want to bet?: "))
        self.bet = bet

    def set_initial_cards(self, player, dealer, deck):
        """
        distribute two cards for the player and the dealer
        """
        for _ in range(2):
            player.cards.append(deck.deal_one())
        for _ in range(2):
            dealer.cards.append(deck.deal_one())
        return(player.cards, dealer.cards[0])

    def win_check(self, player, dealer):
        """Check who is winning the current round"""
        v1 = player.values()
        v2 = dealer.values()
        print(v1)
        if (v1 == v2 or (v1 > 21 and v2 > 21)) :
            return "Game Tie, Push ..."
        elif v1 == 21:
            player.chips += self.bet + ( 2/3 * self.bet)
            return "Black Jack , Player has win"
        elif v2 == 21:
            player.chips -= self.bet + (2/3 * self.bet)
            return "Black Jack , Player has lost"
        elif v1 > 21:
            player.chips -= self.bet
            return "The Player is Busting!"
        elif v2 > 21:
            player.chips += self.bet
            return "The Dealer is Busting! Player has win"
        elif v2 > v1 :
            player.chips -= self.bet
            return "The Dealer is closer to 21! Player has lost"
        else:
            player.chips -= self.bet
            return "The Player is closer 21! Player has win"


    def display_card(self, user):
        """Show player card"""
        if user.role == "guest":
             print("Romeo, your cards are: ", *user.cards)
        else:
            print(f"MrWhite : My second card is {user.cards[-1]}")


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
          The player is only able to Hit or Stand
        """
     )
    ready = ""
    game_on = False
    while ready not in ["Yes", "No" ]:
        ready  = input("How about to  play a round? : Yes or No " )

    if ready == "Yes":
        game_on = True
        deck = Deck()
        board = BoardGame()
        player = Player(name="Romeo", role="guest", chips=42)
        dealer = Player(name="MrWhite", role="dealer")
    else:
            print("Thank you, Bye then!")


    # start a round
    while game_on:
        board.set_bet_amount(player.chips)
        Round(deck=deck, player=player, dealer=dealer)
        board.set_initial_cards(player=player, dealer=dealer,
                                deck=deck)
        board.display_card(player)
        board.display_card(dealer)
        move = player.set_move()
        while move == "Hit":
            player.cards.append(deck.deal_one())
            dealer.cards.append(deck.deal_one())
            print(board.display_card(player))
            print("The dealer cards: ", *dealer.cards[:0:-1])
            if  player.values() > 21:
                print("Sorry! You are busting ....")
                player.chips -= board.bet
                break
            move = player.set_move()
        else:
            print(f"The whole dealer cards are: {dealer.values()}", *dealer.cards)
            print(f"The whole player cards are: {player.values()}", *player.cards)
            print(board.win_check(player, dealer))
        if not player.play_again():
            game_on = False
        else:
            board.reset = True
