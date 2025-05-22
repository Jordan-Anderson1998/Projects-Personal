#include <cstdio>
#include <iostream>
#include <string>
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

*/


int main()
{
    // should be 878
    std::cout << convertQuaternaryToDecimal(31232) << "\n";

    //should be 2005
    std::cout << convertOctalToDecimal(3725) << "\n";

    // should be 0
    std::cout << convertOctalToDecimal(0) << "\n";
    std::cout << convertQuaternaryToDecimal(0) << "\n";

    // should be -469 decimal
    std::cout << convertOctalToDecimal(-725) << "\n";

    // should raise an error
    // std::cout << convertOctalToDecimal(889889);

    return 0;

}
