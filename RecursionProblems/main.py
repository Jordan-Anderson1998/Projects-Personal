"""
Recursion Problems

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