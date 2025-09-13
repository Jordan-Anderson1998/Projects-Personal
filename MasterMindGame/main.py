from random import randint
from math import floor

def binary_chop(max_value_range: int, target: int) -> int:

    """

    Applies a binary chop algorithm for the CPU to solve player guess.

    Args:
        max_value_range: the highest value the number can be to guess
        target: number to find, inputted by human

    """

    guess = floor(max_value_range / 2)
    num_of_guesses = 0

    while guess != target:

        num_of_guesses += 1

        print(f'Guessing: {guess} incorrect...')
        
        if guess > target:
           guess =  floor(guess / 2)
        else:
            guess = guess + (target - floor(guess)) / 2

    print(f'Guesses target: {target} in {num_of_guesses} guesses.')

    return num_of_guesses

def master_mind_game(player_1_name: str, player_2_name: str='CPU', is_single_player: bool=True, debug :bool=False) -> str|None:

    """

        In the game of mastermind, there are two players [player1, player2]
        player1 thinks of a number consisting of integers for example [1234]
        player2 makes their first guess, any correct digits they get will be displayed
        and then they can continue making guesses until they are correct.
        For example, if player2 guesses [2534] the output will be:
            'Incorrect. you got 2 numbers correct [**34]'
        Once player2 guesses the correct number, it's player2's turn to think of a number and player1
        to guess. If player1 guesses the correct number in less number of guesses than it took player2, player1 wins.
        else player2 wins.

        Args:

            player_1_name: name of player1
            player_2_name: name of player2 | defaults to CPU which assumes a one-player game
            is_single_player: defaults to True
            debug:  if True, will explicitly print the CPU guess to the user 

    """

    if is_single_player:

        mastermind = None
        cpu_number = randint(1000, 9999)
        # player_1_guess = None
        num_of_player_guesses = 1
        player_1_guess = int(input(f'{player_1_name} make your first guess:'))

        while player_1_guess != cpu_number:

            num_of_player_guesses += 1
            player_1_correct_digits = ''
            num_of_digits_correct = 0
            cpu_number_comp_str = str(cpu_number)
            player_1_comp_str = str(player_1_guess)

            # output the digits we got correct
            for i in range(0, 4):

                if player_1_comp_str[i] == cpu_number_comp_str[i]:
                    player_1_correct_digits += player_1_comp_str[i]
                    num_of_digits_correct += 1
                else:
                    player_1_correct_digits += '*'

            if debug:
                print(f'CPU randomly generated number = {cpu_number}')
            
            print(f'Incorrect. You got {num_of_digits_correct} digits correct. {player_1_correct_digits}')
            print('Player_1 make a guess or press 0 to quit')
            player_1_guess = int(input(f'{player_1_name} make your {num_of_player_guesses} guess: '))

            if player_1_guess == 0:
                break
                return 0

        print(f"""You got the number {cpu_number} correct! \n Number of guesses required: {num_of_player_guesses}

                    Now it's time for player_1 {player_1_name} to make a number between (1000, 9999) and the CPU will
                    try and guess your number.
        
              """)

        player_1_generated_number = int(input('Please enter a number between [1000, 9999]: '))
        # player_1_generated_number = 0
        # num_of_CPU_guesses = 0
        # CPU_guess = 0

        while (player_1_generated_number < 1000 or player_1_generated_number > 10000) or type(player_1_generated_number) != int:

            player_1_generated_number = int(input('Please enter a valid number between [1000, 9999]'))

        # initialize the cpu guesses    
        num_of_CPU_guesses = binary_chop(max_value_range=10000, target=player_1_generated_number)

        if num_of_CPU_guesses == num_of_player_guesses:

            return "Tie"

        elif num_of_player_guesses < num_of_CPU_guesses:

            print(f'Player_1 {player_1_name} wins! {player_1_name} is the mastermind!')
            mastermind = player_1_name

        else:

            print(f'CPU Wins! CPU is the mastermind!')
            mastermind = player_2_name

        dict_values =  {'names': [player_1_name, player_2_name],
                        'CPU number': cpu_number,
                        'player 1 number': player_1_generated_number,
                        'number of guesses': (num_of_player_guesses, num_of_CPU_guesses)}

        print(dict_values)

        return mastermind

if __name__ == '__main__':

    player_1 = 'Jordan'

    master_mind_game(player_1_name=player1)

