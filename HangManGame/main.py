from random import choice

FRUITS = set({'strawberry', 'banana', 'orange', 'grapefruit', 'peach', 'mango', 'blueberry', 'blackberry', 'pomegrante',
              'papaya', 'passionfruit', 'lemon', 'lime', 'avacado', 'tomato', 'cucumber'})

CANADIAN_CITIES = set({'edmonton', 'calgary', 'halifax', 'winnipeg', 'toronto', 'toronto', 'regina', 'saskatoon', 'vancouver',
                       'victoria', 'kelowna', 'hamilton', 'montreal', 'quebec'})

INSECTS = set({'centipide', 'ant', 'millipide', 'ladybug', 'wasp', 'bee', 'cockroach', 'bedbug', 'tick', 'flea', 'bettle',
               'fly', 'mosquito', 'butterfly', 'moth'})


def select_word(category: set) -> str:

    """
    Randomly selects a word based on a set of unique words related to various categories.

    :param category: set of categorical options to choose from
    :return: random option
    """

    return choice(list(category))


def hang_man_game(player_name: str, category_name: set, cheat:bool =False, num_of_attempts_to_solve: int=10) -> str:

    """
    In this game a random word will be selected from a set of different categories eg. (fruits, cars, canadian cities).
    Players will get length of word + 2 attempts at solving the word.

    :return: a value of either 'hangman' or 'victory'
    """

    selected_word = select_word(category=category_name)
    player_guess = '_' * len(selected_word)
    list_player_guess = list(player_guess)
    player_letters_guessed = []
    correct_letters_player_guesses = []

    while num_of_attempts_to_solve > 0:

        if cheat:
            print(selected_word)

        print(f"""{player_name} here are the letters you have guessed: {player_letters_guessed} \n

                Word:
                
            """)

        print(f'Word: {list_player_guess}')

        player_selection = str(input('Select your letter: '))

        while len(player_selection) > 1 or player_selection.isnumeric():

            player_selection = str(input('Please enter ONE valid alphabet character only: '))

        player_letters_guessed.append(player_selection)

        for _ in range(0, len(selected_word)):

            if player_selection == selected_word[_]:

                list_player_guess[_] = player_selection
                correct_letters_player_guesses.append(player_selection)

        if sorted(correct_letters_player_guesses) == sorted(selected_word):

            print(f'{player_name} guessed the word! The correct word was {selected_word}')
            return 'Victory!'

        num_of_attempts_to_solve -= 1

    print(f'The word was {selected_word}')
    return 'Hangman'


if __name__ == '__main__':

    player_name = 'Jordan'
    category_name = FRUITS

    hang_man_game(player_name=player_name, category_name=category_name)