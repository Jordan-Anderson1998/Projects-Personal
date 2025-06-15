inline int binaryChop(std::vector<int> vector, int target) {
    /*  Binary Searching Algorithm
     *  Performs at the ability of <O(logn)> Amount of time required to compute = logarithm
     *  This performs significantly better than linear search which performs at <O(n)>
     *  This algorithm requires a sorted array of elements in order to work properly.
     *
     *  Args:
     *      vector: vector object to attempt to find target
     *      target: int to be searched
     *  Return:
     *      Element if found, -1 if element not found in vector.
    */

    int numOfSearches { 0 };
    int left { 1 };
    // int index { };
    auto right {vector[vector.size()-1]};

    while (left <= right) {

        numOfSearches ++;
        // index ++;
        auto middle { (left + right) / 2  };

        // if (vector[])

        if (middle == target) {
            printf("Found target %d \n", target); // .at(middle) does not return the correct position
            printf("Number of searches: %d \n", numOfSearches);
            return target;
        }
        if (middle < target) {
            left = middle + 1;
        }else {
            right = middle - 1;
        }
    }
    printf("Target %d not found after %d number of searches \n", target, numOfSearches);
    return -1;
}

inline int linearSearch(std::vector<int> vector, int target) {
    /*
     *  Standard linear search algorithm that performs a sequential search by looping through each element until target
     *  is found. If target is not found return an error of -1.
     *
     *  Args:
     *      Vector: vector object
     *      target: int value to be searched for in the vector
     *  Return:
     *      Target if target is found, -1 if target is not found.
    */
    int numOfSearches {0};
    for (auto value: vector) {

        numOfSearches ++;
        if (value == target) {
            printf("Found Target %d after %d number of searches \n", target, numOfSearches);
            return target;
            // return vector.at(target);
        }
    }

    printf("Target %d Not found after %d number of searches \n", target, numOfSearches);
    return -1;

}