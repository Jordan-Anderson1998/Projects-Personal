from unit_tests import check_card_deck_length, check_if_shuffled_deck, check_score_type, check_if_end_of_deck
from random import randint
from copy import deepcopy

def display_cards_and_score(player_cards, dealer_cards, player_score, dealer_score):

    print(f'Player Cards: {player_cards}')
    print(f'Dealer Cards: {dealer_cards}')

    print(f'Player Score: {player_score}')
    print(f'Dealer Score: {dealer_score}')


class CardDeck:
    def __init__(self, name):
        self.name = name
        self.cards = {}
        self.shuffled_cards = False

    def make_card_deck(self, num_of_cards: int, card_class: list, special_card: list):

        cards = {}
        # Generate cards with value 1-10
        for i in card_class:
            for j in range(num_of_cards - 1):
                key = f'{j + 2}_of_{i}'
                cards[key] = j + 2
                # print(f'{j + 2}_of_{i}')
        # Generate special cards
        for card in card_class:
            for name in special_card:
                special_class_name = f'{name}_of_{card}'
                cards[special_class_name] = 10

        self.cards = cards

    def shuffle_deck(self) -> list:
        """
        Take each index from a new list of cards, and switch with them a random index from the original deck.
        :return: List of randomized card objects
        """
        card_array = []
        for i in self.cards:
            dict_cards = {i: self.cards[i]}
            card_array.append(dict_cards)
        card_array_copy = deepcopy(card_array)

        for i in range(0, len(card_array)):
            card_array_copy[i] = card_array[randint(0, len(card_array) - 1)]

        check_if_shuffled_deck(shuffled_deck=card_array_copy, original_deck=card_array)
        check_card_deck_length(card_deck=card_array_copy)

        self.shuffled_cards = card_array_copy
        return card_array_copy


class Player:
    def __init__(self, name, wager):
        self.name = name
        self.wager = wager
        self.cards = []
        self.score = 0

    def add_cards(self, deck, card_pos):
        card = deck[card_pos]
        self.cards.append(card)

    def sum_score(self, cards: list, card_sum: list, score: int = 0) -> int:

        """

        :param cards: deck of shuffled cards
        :param card_sum: an empty list that will take the value of the cards assigned
        :param score: the initial score of player. A new game will default to 0
        :return: the new score of the player based on cards they get
        """

        player_score = score

        for i in cards:
            # print([j for j in i.values()])
            card_sum.append([j for j in i.values()])

        for i in card_sum:
            for j in i:
                player_score += j

        self.score = player_score
        return player_score


class Dealer(Player):
    pass


class BlackJackTable:
    def __init__(self, player, dealer, cards):

        self.player = player
        self.dealer = dealer
        self.cards = cards.cards
        self.shuffled_cards = cards.shuffled_cards
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0
        self.num_of_games = 0
        self.card_index = 0

    def check_scores(self, player, dealer):

        if player.score == 21 and dealer.score != 21:
            print('BlackJack 21 for Player! Player Wins!')
            self.player_wins += 1

        elif dealer.score == 21 and player.score != 21:
            print('BlackJack 21 for Dealer! Dealer wins!')
            self.dealer_wins += 1

        elif 21 > player.score > dealer.score:
            print('Player Wins!')
            self.player_wins += 1

        elif 21 > dealer.score > player.score:
            print('Dealer Wins!')
            self.dealer_wins += 1

        elif player.score > 21 >= dealer.score:
            print('Player Busts!')
            self.dealer_wins += 1

        elif dealer.score > 21 >= player.score:
            print('Dealer busts!')
            self.player_wins += 1

        # elif player.score > 21 and dealer.score > 21:
        #     print('Player and Dealer both bust')
        #     self.ties += 1

        else:
            print('Player and Dealer Tie')
            self.ties += 1

    def play_game(self):

        # card_index = 0

        check_if_end_of_deck(index=self.card_index, stop=49)

        new_player = Player(name=self.player.name, wager=self.player.wager)
        new_dealer = Dealer(name=self.dealer.name, wager=self.dealer.wager)

        new_player.add_cards(deck=self.shuffled_cards, card_pos=self.card_index)
        new_dealer.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + 1)
        new_player.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + 2)
        new_dealer.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + 3)

        new_player.sum_score(cards=new_player.cards, card_sum=[], score=0)
        new_dealer.sum_score(cards=new_dealer.cards, card_sum=[], score=0)

        display_cards_and_score(player_cards=new_player.cards, dealer_cards=new_dealer.cards,
                                player_score=new_player.score, dealer_score=new_dealer.score)

        while new_player.score < 21:

            player_input = input(f'Player your score: {new_player.score} Do you wish to hit or stand (stay)?')

            if player_input == 'hit':
                new_player.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + 4)

                if 21 > new_player.score > new_dealer.score:
                    new_dealer.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + 5)
                    new_dealer.sum_score(cards=new_dealer.cards, card_sum=[], score=0)

                new_player.sum_score(cards=new_player.cards, card_sum=[], score=0)
                new_dealer.sum_score(cards=new_dealer.cards, card_sum=[], score=0)

                display_cards_and_score(player_cards=new_player.cards, dealer_cards=new_dealer.cards,
                                        player_score=new_player.score, dealer_score=new_dealer.score)

                # self.check_scores(player=new_player, dealer=new_dealer)

                self.card_index += 1
                # deck_index_for_player += 1
                # deck_index_for_dealer += 1

            if player_input == 'stand':

                while 21 > new_player.score > new_dealer.score:

                    dealer_card_index = 5
                    new_dealer.add_cards(deck=self.shuffled_cards, card_pos=self.card_index + dealer_card_index)
                    new_dealer.sum_score(cards=new_dealer.cards, card_sum=[], score=0)
                    dealer_card_index += 1

                new_player.sum_score(cards=new_player.cards, card_sum=[], score=0)
                new_dealer.sum_score(cards=new_dealer.cards, card_sum=[], score=0)

                display_cards_and_score(player_cards=new_player.cards, dealer_cards=new_dealer.cards,
                                        player_score=new_player.score, dealer_score=new_dealer.score)

                # self.check_scores(player=new_player, dealer=new_dealer)
                break

        self.check_scores(player=new_player, dealer=new_dealer)
        self.num_of_games += 1
        self.card_index += 1


if __name__ == '__main__':

    num_of_cards = 10
    wager = 100
    card_classes = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    special_card_classes_names = ['Jack', 'Queen', 'King', 'Ace']

    new_deck = CardDeck(name='Standard Deck')
    new_deck.make_card_deck(num_of_cards=num_of_cards,
                            card_class=card_classes,
                            special_card=special_card_classes_names)

    new_deck.shuffle_deck()

    jordan = Player(name='Jordan', wager=wager)
    dealer = Dealer(name='Dealer', wager=wager)

    blackjack_table = BlackJackTable(player=jordan, dealer=dealer, cards=new_deck)

    print(new_deck)
    print(blackjack_table.cards)
    print(blackjack_table.shuffled_cards)

    # print(blackjack_table.play_game())