#include <iostream>
#include <vector>
#include "SearchAndSort.h"

auto makeNumVector(const int num, const int step=1, const bool showVectorContents=false) {

    /*
     *  Construct a vector object to hold a (linear) sequence of integers.
     *  Vectors have the ability to access elements with indexing [], which is the reason why vector is the choice object
     *  for this task. Other dynamic objects such as list have the ability to sort the elements, but can't index like vector.
     *
     *  Args:
     *      num: Number of int elements to be added to the vector.
     *      step: Increment of every element.
     *      showVectorContents: Whether to print the vector contents or not.
     *  Return:
     *      Vector object
    */
    std::vector<int> vector;

    for (int i=0; i<=num; i+=step) {

        vector.push_back(i);
    }

    if (showVectorContents) {

        for (auto value: vector) {
            std::cout << value << " ";
        }
    }
    return vector;
}

int main(int argc, char *argv[]) {

    std::vector<int> vector;
    std::vector<int> vector2;
    std::vector<int> bigVec;

    vector = makeNumVector(100, 1, true);
    vector2 = makeNumVector(10000, 2, false);
    bigVec = makeNumVector(75000, 5, false);

    std::cout << std::endl;
    binaryChop(vector, 2);

    std::cout << std::endl;
    binaryChop(vector, 75);

    std::cout << std::endl;
    // search for a target that doesn't exist
    binaryChop(vector2, -1);

    std::cout << std::endl;
    binaryChop(vector2, 1200);

    std::cout << std::endl;
    linearSearch(vector, 75); // Expecting 76 searches

    std::cout << std::endl;
    linearSearch(vector2, 1200);

    std::cout << std::endl;
    binaryChop(bigVec, 65000);

    std::cout << std::endl;
    linearSearch(bigVec, 65000);

    std::cout << std::endl;
    linearSearch(bigVec, -60);
    
    return 0;
}
