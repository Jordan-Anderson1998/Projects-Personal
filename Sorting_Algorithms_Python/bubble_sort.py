"""
Sort through an array of elements using the bubble sort algorithm.

Bubble sort uses multiple passes (iterations) putting the largest element in it's proper position, then the second
largest, then the third largest and so forth.

"""
def bubble_sort(array: list) -> list:
    """

    One of the simpler sorting algorithms, useful for small data sets but improper for larger data sets as the computational
    time needed increases substantially.

    :param array: a list of elements to be sorted
    :return: a sorted list of elements
    """
    num_of_elements = len(array)
    _temp_array = array[::]
    sorted_array = array[::]
    swap_index = len(array) - 1

    while num_of_elements > 0:

        max_value_index = _temp_array.index(max(_temp_array))
        max_value_index_value = _temp_array[_temp_array.index(max(_temp_array))]
        sorted_array[swap_index] = max_value_index_value
        sorted_array[max_value_index] = _temp_array[swap_index]

        # remove current max number so that the next highest will be the max
        _temp_array.pop(_temp_array.index(max(_temp_array)))

        num_of_elements -= 1
        swap_index -= 1

    return sorted_array

if __name__ == '__main__':

    test_array = [1, 7, 3, 9, 4, 13, 8, 0]

    print(bubble_sort(test_array))

