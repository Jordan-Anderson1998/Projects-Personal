#include <iostream>
#include <string>
#include <map>
#include <array>
#include <algorithm>
#include <cmath>
#include "numberSystemConverterModule.h"

/*

convertOctalToDecimal(number)

convert number of type int --> char (string) to iterate.

convert --> back to int

execute algorithm from right-to-left of number, add digits together to get decimal
equivalent.

example of how to convert octal to decimal

31232 = 3 * 4^4 +
        1 * 4^3 +
        2 * 4^2 +
        3 * 4^1 +
        2 * 4^0

// void printVariables(int i, int j, int stringNum){

//     printf("value of i: %d \n", i);
//     printf("Value of j: %d \n", j);
//     printf("Value of stringNum: %d \n", stringNum[stringNum.size() - j] - '0');


First algorithm attempt, reduced redundancy by eliminating second else clause, new
algorithm upholds the DRY principle better.

            // // if first digit in number
        // if(i == pow(4, stringNum.size())){

        //     total += i * (stringNum[stringNum.size() - j] - '0');
        //     j -= 1;

        // }else{

        //     total += i * (stringNum[stringNum.size() - j] - '0');
        //     j -= 1;
// }


Error handling + handling incorrect inputs

We need to handle improper inputs to the function, such as an incorrect data type
like a string, float, bool etc. The function must take an integer only.

We also need to make sure the correct formatting is applied as input to the function.
For example, Octal numbers cannot contain an 8, as Octal numbers only allow the digits 0-7.
If the user enters an incorrect number trying to convert to decimal, this must be handled.

We should also consider 0, and negative numbers.

0 is equivalent in every number system. [decimal, binary, octal, hexadecimal, quaternary]

For negative numbers we simply need to take the absolute value of the number and convert it
to the negative equivalent.

for(int i=0; i<=stringNum2.size(); i++){

    std::cout << stringNum2[i];
    if (stringNum2[i] >= 8 ){

        printf("%d: Incorrect Octal Number!", incorrectOctalNumber);
        // std::cout << "incorrect Octal Number!";
    }
}

Converting Binary to decimal

C++ long int types lets us enter an int argument up to 19 digits

this means that 1111111111111111111 is the maximum binary digit we can enter under this
algorithm. This is only equivalent to 542,287 in decimal. So perhaps we should divide the argument given to the
function into groups of 4, and add these results together instead of interpreting it as one very long number.

*/


int main()
{

    const int decimalToHexNum = 255;
    const int decimalToBinaryNum = 123456;
    const int octalNumber = 34567;
    const std::string binaryNum = "10001010101011";
    const std::string hexadecimalSequence = "DE56";
    const std::string incorrectHexadecimal = "ABNO90LPZYZ";

    // should be 0b1 1110 0010 0100 0000
    std::cout << convertDecimalToBinary(decimalToBinaryNum) << std::endl;

    // should be FFh
    std::cout << convertDecimalToHexaDecimal(decimalToHexNum) << std::endl;

    // should be 56,918 decimal
    std::cout << covertHexadecimalToDecimal(hexadecimalSequence) <<std::endl;

    // should be 14,711 decimal
    std::cout << convertOctalToDecimal(octalNumber) << std::endl;

    // should be 8,875 decimal
    std::cout << convertBinaryToDecimal(binaryNum) << std::endl;

    // should be 498,549 decimal
    std::cout << convertBinaryToDecimal("1111001101101110101") << std::endl;

    // should raise an exception, not a hexadecimal number
    std::cout << covertHexadecimalToDecimal(incorrectHexadecimal) << std::endl;

    // should raise an exception, not a valid binary digit
    // std::cout << convertBinaryToDecimal("23456789") << std::endl;

    return 0;
}

