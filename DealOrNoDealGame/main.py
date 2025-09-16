from random import choice
from unit_tests import check_if_cases_unique_values


def print_rules(text_file: str):

    with open(text_file, 'r') as f:
        rules = f.read()
        f.close()
        return rules


def generate_cases(num_of_cases: int=25) -> dict:

    """
    Generate a select number of cases with randomly chosen values assigned to each key corresponding to (case number).
    Each case should contain a unique value. No 2 cases should have the same value.

    args:
        num_of_cases: the number of cases to be generated
    Return:
        dictionary of cases with case number, value


    """
    case_values = [0.01, 1, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000,
                    10000, 25000, 50000, 75000, 100000, 125000, 150000, 175000,
                    200000, 2500000, 500000, 750000, 1000000]


    cases = {}

    for i in range(num_of_cases):
        cases[i] = choice(case_values)
        # remove from the list so that no 2 values are assigned to different briefcases
        case_values.remove(cases[i])

    check_if_cases_unique_values(cases=cases)

    return cases

def dealer_offer(cases: dict) -> int:
    """
    The dealer offer will be based on the formula:

    average of remaining cases / number of cases selected by player for turn.:

    (sum of remaining cases / number of cases remaining) / 3.

    """

    sum_of_cases = 0

    for case in cases.values():
        sum_of_cases += case

    offer = (sum_of_cases / len(cases)) / 3

    return round(offer)

def deal_or_no_deal(player_name: str) -> str|None:
    """

    Brief overview:

    The user chooses an initial case from a random selection of 25 cases. This will be considered their personal case.
    After every 3 new cases selected, the dealer will make an offer. The player can then choose if they want to stick with
    their original case and deny the dealer offer, or they can take the dealer's offer and leave the other cases and their
    potential money on the table.

    args:
        player_name: Name of user

    Return:
        'Jackpot!' or 'Game Over' or None
    """

    cases = generate_cases(num_of_cases=25)
    num_of_cases = len(cases)
    num_of_guesses = 0
    accumulative_sum = 0
    case_list = []

    print(f'{player_name} welcome to deal or no deal. \n press 1 to continue to the game \n press 2 to get an overview of the rules. \n press 0 to quit the game')

    user_input_start = int(input('1: Continue to game \n 2: Print rules of game \n 0: Quit Game'))

    while user_input_start != 0 and user_input_start != 1 and user_input_start != 2:
        user_input_start = int(input('Please enter a valid selection of [0, 1, 2] \n 1: Start game \n 2: Print rules of the game \n 0: Quit Game'))

    if user_input_start == 0:
        return None
    
    if user_input_start == 2:

        rules = print_rules(text_file='game_desc.txt')
        print(rules)

    print(f'{player_name} choose your case: ')

    player_choice = int(input('Select the case you want. \n Valid options are between 1 and 25'))
    player_case = cases[player_choice]
    cases.pop(player_choice)
    case_list.append(player_choice)

    while 1 > player_choice > 25:
        player_choice = int(input(f'player:{player_name} made an invalid choose. Valid options are between 1 and 25'))

    next_player_case_choice = None
    _dealer_offer = 0

    while num_of_guesses < 25:

        num_of_guesses += 1
        num_of_cases -= 1

        print(f'{player_name} the cases you have selected are: \n {case_list}')
        print(f'{player_name} your case: {player_choice}')
        next_player_case_choice = int(input('Choose your next case: '))

        try:
            print(f'Case: {next_player_case_choice} contained ${cases[next_player_case_choice]}')
        except KeyError:
            while next_player_case_choice < 1 or next_player_case_choice > 24:
                next_player_case_choice = int(input(f'There is no case {next_player_case_choice}. '
                                                    f'Or case {next_player_case_choice} has already been chosen. '
                                                    f'Please enter a valid choice.'))

        cases.pop(next_player_case_choice)
        case_list.append(next_player_case_choice)
        # accumulative_sum += cases[next_player_case_choice]

        if num_of_guesses % 3 == 0:

            _dealer_offer = dealer_offer(cases=cases)

            print(f'{player_name} the dealer has made an offer. The offer is ${_dealer_offer}')

            player_decision = input('Do you accept the dealer offer?')

            if player_decision == 'y'.lower():

                print(f'You accepted the offer of {_dealer_offer}. Your case was {player_case} and contained ${cases[player_choice]}.')
                return 'Game Over'

    print(f"""Player you have rejected all of the offers from the dealer. It is time to unveil your case.

            You choose case {player_case} and it contains ${cases[player_choice]}.
                
                """)

    if cases[player_case] == 1000000:
        print(f'{player_name} you are the ultimate winner!')
        return 'Jackpot!'

    return 'Game Over'

if __name__ == '__main__':

    player_name = 'Jordan'

    # cases = generate_cases(num_of_cases=25)

    deal_or_no_deal(player_name=player_name)