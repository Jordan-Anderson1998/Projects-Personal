import os
import re

"""
Make a word search solver

Read the file that contains the word search
Make functions that will solve different parts of the word search based on how the words are structured.

"""

def make_line_separator(num_of_char):

    print('*'* num_of_char + '\n')

def read_file(file_path: str) -> str:

    """

    :param file_path: name of file path to be opened and processed
    :return: the contents of text file

    """

    with open(file_path) as file:

        word_search = file.read()
        print(file.readlines())
        return word_search

def create_word_index(*args: str) -> list:
    """

    :param args: string arguments to be added to a list of words to be found in the word search
    :return: list of words
    """

    word_index_list = []
    for arg in args:
        word_index_list.append(arg)

    return word_index_list

def compile_words_do_search(word_list: list, text: str, type_of_search: str='linear') -> str:


    """

    compile regular expression matches to be searched, then search through text for matches.


    :param word_list: list of words to compile into regular expressions
    :param text: text to search through attempting to find matches based on word_list
    :param type_of_search:[linear, reverse, up-to-down] the type of search to be implemented
        If: type_of_search = 'linear':
        Function will only find the words in the word search that can be found left-to-right,
        and will omit any words in reverse order or up-to-down.
        If: type_of_search = 'reverse'
        Function will only find the words in the words search that are spelled backwards, and will
        omit any words that can be found linearly or up-to-down
        If: type_of_search = 'up_to_down'
        Function will only find the words that can be found up-to-down across the word search, and will omit
        and words that can be found linearly or backwards.
    :return: matches, index of matches in text
    """

    words_found = []
    words_not_found = []

    if type_of_search == 'linear':

        for word in word_list:
            pattern = re.compile(word.lower())
            print(pattern)
            matches = pattern.search(text)
            print(matches)
            # Find the indices of any matches found in text
            try:
                match_indexes = matches.span()
                print(match_indexes)

            # Index and print the text in the range where the matches are found
                print(text[matches.span()[0]: matches.span()[1]])

                words_found.append(word)

            except AttributeError:
                print('No match found, no indices found')
                words_not_found.append(word)

    elif type_of_search == 'up_to_down':

        last_row_start_index = 2067
        vertical_characters = ''

        # get the first column in word search
        # end_of_word_search_index = text.find('---') - 1

        # Index from nth column to last_row nth position with a step of 53
        for ii in range(0, 52):
            vertical_characters += text[ii: last_row_start_index + ii: 53]
            # print(text[ii: last_row_start_index + ii: 53])

        for word in word_list:
            pattern = re.compile(word.lower())
            print(pattern)
            matches = pattern.search(vertical_characters)
            print(matches)
            # Find the indices of any matches found in text
            try:
                match_indexes = matches.span()
                print(match_indexes)

                # Index and print the text in the range where the matches are found
                print(vertical_characters[matches.span()[0]: matches.span()[1]])

                words_found.append(word)

            except AttributeError:
                print('No match found, no indices found')
                words_not_found.append(word)

    elif type_of_search == 'reverse':

        for word in word_list:
            reverse_word = word[::-1]
            reverse_pattern = re.compile(reverse_word)

            print(reverse_pattern)

            reverse_matches = reverse_pattern.search(text)
            print(reverse_matches)

            try:
                match_indexes = reverse_matches.span()
                print(match_indexes)

                # Index and print the text in the range where the matches are found
                print(text[reverse_matches.span()[0]: reverse_matches.span()[1]])

                words_found.append(word)

            except AttributeError:
                print('No match found, no indices found')
                words_not_found.append(word)

    else:
        raise ValueError(f'arg: {type_of_search} is not valid, use one of [linear, reverse, up_to_down]')

    return f'Words found: {words_found}, words not found: {words_not_found}'


if __name__ == '__main__':

    file_name = os.listdir()[2]
    word_search = read_file(file_name)

    print(word_search)

    make_line_separator(75)

    words_to_find = create_word_index('edmonton', 'calgary', 'vancouver', 'hamilton', 'toronto', 'victoria', 'regina',
                                      'saskatoon', 'winnipeg', 'reddeer', 'halifax', 'montreal', 'kelowna')

    print(words_to_find)

    make_line_separator(75)

    linear_words = compile_words_do_search(words_to_find, word_search, 'linear')
    print(linear_words)

    make_line_separator(75)

    reverse_words = compile_words_do_search(words_to_find, word_search, 'reverse')
    print(reverse_words)

    make_line_separator(75)

    vertical_words = compile_words_do_search(words_to_find, word_search, 'up_to_down')
    print(vertical_words)
