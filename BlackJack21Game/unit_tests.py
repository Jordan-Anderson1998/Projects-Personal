from types import NoneType


def check_card_deck_length(card_deck):
    try:
        assert len(card_deck) == 52
    except AssertionError:
        raise ValueError(f'Warning! Standard deck of cards is 52, len of deck: {len(card_deck)}')

def check_if_shuffled_deck(shuffled_deck: list, original_deck: list):

    try:
        assert shuffled_deck != original_deck
    except AssertionError:
        raise ValueError('The shuffled deck and original deck are equivalent')

def check_score_type(player_score: int, dealer_score: int):

    try:
        assert (type(player_score) != NoneType) and (type(dealer_score) != NoneType)

    except AssertionError:
        raise TypeError(f"""
                        Warning! player_score and dealer_score cannot be of None Type
                        player_score type: {type(player_score)}
                        dealer_score type: {type(dealer_score)}
                        
""")

def check_if_end_of_deck(index, stop: int):
    try:
        assert index < stop
    except AssertionError:
        raise ValueError('Warning! Reached end of deck!')
