"""
A sorting algorithm pulled out of my butt.

"""
def jordan_sort(array: list) -> list:

    passes = len(array)
    sorted_array = []
    index = 0

    while passes > 0:

        max_value = array.pop(array.index(max(array)))
        sorted_array.append(max_value)
        passes -= 1
        index += 1

    sorted_array.reverse()

    return sorted_array


if __name__ == '__main__':

    array = [1, 6, 3, 5, 4, 7]

    sorted_array = jordan_sort(array=array)
    print(sorted_array)