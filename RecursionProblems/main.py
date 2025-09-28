"""
Recursion Problems

Easier problems:

1. Sum Digits
- Write a function that sums the digits in any given integer
    - for example (123) return -> 6

2. Count Zeros
- Write a function that counts the number of 0's in a given integer
    - for example (0100010) Return -> 4

3. Palindrome Checker
- Write a function to check if a given input as string is a palindrome
    - palindrome: word that can be read the same way forwards as backwards
    - example ('racecar') return -> True
    - ('orange') return -> False

4. Compute power
- Write a function that takes (a,b) as input as returns a^b
- Example (10, 3) return -> 1000

5. Reverse string
- Write a function that reverses a given string as input
- Example ('hello') return -> 'olleh'

----------------------------------------

Intermediate recursion problems

1. Generate All Subsets (Power Set)
- Problem: Given a set of distinct integers, return all possible subsets.
- Concepts: Backtracking, recursion tree
- Bonus: Try it with duplicate elements and avoid duplicate subsets.

2. Permutations of a String
- Problem: Given a string, return all possible permutations.
- Concepts: Swapping, recursion depth
- Bonus: Handle duplicate characters efficiently.

3. N-Queens Problem
- Problem: Place N queens on an N×N chessboard so that no two queens threaten each other.
- Concepts: Backtracking, constraint checking
- Bonus: Count all valid solutions, not just one.

4. Word Break Problem
- Problem: Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of dictionary words.
- Concepts: Recursion with memoization
- Bonus: Return all possible segmentations.

5. Maze Solver
- Problem: Given a 2D grid with obstacles, find a path from the top-left to bottom-right.
- Concepts: Backtracking, recursion with direction vectors
- Bonus: Return all possible paths.

6. Recursive Palindrome Partitioning
- Problem: Partition a string into all possible combinations of palindromic substrings.
- Concepts: Backtracking, substring checking
- Bonus: Optimize with memoization.

7. Tower of Hanoi with Move Tracker
- Problem: Solve the Tower of Hanoi and return the sequence of moves.
- Concepts: Classic recursion, state tracking
- Bonus: Visualize the moves or animate them.

8. Count Ways to Climb Stairs (Variable Steps)
- Problem: You can climb 1, 2, or 3 steps at a time. How many ways to reach the top of a staircase with N steps?
- Concepts: Recursion with overlapping subproblems
- Bonus: Add constraints like forbidden steps.

9. Sum of All Paths in a Binary Tree
- Problem: Given a binary tree, return the sum of all root-to-leaf paths interpreted as numbers.
- Concepts: Tree traversal, recursive accumulation
- Bonus: Return the list of all path values.

10. Expression Add Operators
- Problem: Given a string of digits and a target value, insert +, -, or * operators to form expressions that evaluate to the target.
- Concepts: Recursion with expression building
- Bonus: Handle operator precedence correctly.

11. Fibonacci Sequence
    - Write a function to compute the n-term sequence of the fibonacci sequence.

"""

def sum_digits(n:int, _iter: int=0, running_total=0, print_nums: bool=False) -> int:
    """
    Given a number n, returns the sum of all digits in the number.
    Calculate the sum digits of n recursively.

    For example, given n = 123, return 6

    :param n: number
    :param _iter: where to start iterating on number
    :param print_nums: if True, print each number that is being calculated
    :param running_total: the running total of each digit in n
    :return: the sum of all digits in the number n

    """

    string_num = str(n)

    if print_nums:
        print(running_total)

    if _iter < len(string_num):

        running_total = sum_digits(n, _iter + 1, running_total + int(string_num[_iter]))

    return running_total


# def reverse_string(string):
#     """
#     Given a string, returns the reversed string using recursion.
#     For example, given string = 'hello', return 'olleh'
#     :param string:
#     :return:
#     """
#
#     string_index = len(string) - 1
#
#     if string_index > 0:
#
#         reverse_string(string[string_index - 1])
#         # print(string[string_index])
#
#     print(string[string_index])


def count_zeros(num: int, _iter=0) -> int:
    """
    Count the number of zeros in the number recursively.
    :return:
    """

    zeros = 0
    string_num = str(num)

    if _iter < len(string_num):

        if string_num[_iter] == '0':
            zeros += 1

        zeros += count_zeros(num, _iter + 1)

    return zeros

def compute_power(a: int, b: int) -> int:

    """
    compute a^b recursively.

    :param a: integer
    :param b: integer
    :return: a^b
    """

    total = 1 * a

    if b == 0:

        return 1

    else:

        total *= compute_power(a, b - 1)

    return total

def check_if_palindrome(word: str, i, j) -> bool:

    """
    check if string is a palindrome.
    A palindrome is any string that is spelled the same in both forward and reverse order.
    Example: racecar spelled backwards is racecar

    :param word: string to check if palindrome
    :return: true if palindrome, false otherwise
    """

    if len(word) == 1:
        return True

    if i != j:

        if word[i] != word[j]:
            return False
        else:
            try:
                check_if_palindrome(word, i + 1, j - 1)
            except IndexError:
                return True

    return True

def generate_set_of_nums(x: int) -> set:

    num_list = []

    for i in range(x + 1):
        num_list.append(i)

    return set(num_list)


def generate_subsets(nums: set, i: int=1) -> None:

    """
    Based on a set of unique integers, generate all of the possible combinations.

    Example:
        input: [1, 2, 3, 4, 5]
        expected output: [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]

    :param nums: set of integers
    :param i: print slice starting at 0:1
    :return:
    """

    num_list = list(nums)

    print(num_list[0:i])

    if i < len(num_list):
        generate_subsets(nums, i + 1)


def string_permutations(string: str):

    """

    Given a string, print all the possible permutations.

    Example:
        Input: 'abc'
        expected output: 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'

    :param string:
    :return:
    """

    pass

def fibonacci(n_terms: int) -> list:

    """
    Fibonaci Sequence {0, 1, 1, 2, 3, 5, 8, 13, 21...}

    n1: initialize at 0
    n2: initialize at 0
    n: initialize at 0

    n += 1 : n = 1

    n1 = n2
    n2 = n
    sequence = n2 + n1

    :param n_terms: Compute n-terms in the fibonacci sequence
    :return: List of sequences
    """

    n1 = 0
    n2 = 0
    n = 0
    sequence = [0, 1]


    while n_terms > 0:

        print(n)

        if n == 0:

            n += 1
            n2 += 1
            n1 += 1
            sequence.append(n)

            print(n)
            print(n)

        n1 = n2
        n2 = n
        n = n2 + n1

        sequence.append(n)

        n_terms -= 1

    return sequence


if __name__ == '__main__':

    unique_nums = generate_set_of_nums(x=50)

    print(generate_subsets(nums=unique_nums, i=1))

    print(fibonacci(n_terms=15))

    num = sum_digits(12345)
    num2 = sum_digits(1234567890)
    num3 = sum_digits(234989098712)

    print(num, num2, num3)

    assert count_zeros(100100010) == 6
    assert count_zeros(123) == 0
    assert count_zeros(10000000) == 7
    # technically any number that starts with a zero will be zero (if any number besides 0 python will throw an exception)
    assert count_zeros(00000) == 1

    print(count_zeros(100100010))

    print(compute_power(10, 3))

    word = 'racecar'
    word2 = 'orange'

    assert check_if_palindrome('racecar', 0, 6) == True
    assert check_if_palindrome('orange', 0, 5) == False

    print(check_if_palindrome('racecar', 0, 6))
    print(check_if_palindrome(word2, 0, len(word2) - 1))