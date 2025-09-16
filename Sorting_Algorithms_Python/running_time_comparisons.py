from jordan_sort import jordan_sort
from bubble_sort import bubble_sort
from time import time
from random import randint
from ascending_sorting_algorithm import ascend_sort


def compute_time(array: list, sorting_algorithm) -> float:
    start_time = time()
    sorting_algorithm(array)
    end_time = time()

    return end_time - start_time

def make_unsorted_array(num_of_elements: int, range_of_nums: int) -> list:
    """

    :param range_of_nums: what number range to generate random int
    :param num_of_elements: how many random ints to generate
    :return: a list of random integers of size [num_of_elements]
    """

    array = []

    for i in range(num_of_elements):

        array.append(randint(0, range_of_nums))

    return array


if __name__ == '__main__':

    unsorted = make_unsorted_array(num_of_elements=50000, range_of_nums=150000)

    print(f"""
    
          jordan_sort compute time = {compute_time(array=unsorted, sorting_algorithm=jordan_sort)} \n
          bubble sort compute time = {compute_time(array=unsorted, sorting_algorithm=bubble_sort)} \n
          ascend sort compute time = {compute_time(array=unsorted, sorting_algorithm=ascend_sort)} \n

          """)