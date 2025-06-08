inline void testIfCorrectFormat(int testNumber, char type){

    // if octal number
    if(type == 'o'){

        std::string stringNum = std::to_string(testNumber);

        for(int i=0; i<=stringNum.size(); i++){

            if(stringNum[i] >= '8'){

                // printf("%d is an incorrect Octal number", number);
                throw std::runtime_error("Cannot compute non-octal number. Valid Octal numbers have digits [0-7]");
        }
    }
    }

      // if quaternary number
    if(type == 'q'){

        std::string stringNum = std::to_string(testNumber);

        for(int i=0; i<=stringNum.size(); i++){

            if(stringNum[i] >= '4'){

                // printf("%d is an incorrect Octal number", number);
                throw std::runtime_error("Cannot compute non-quaternary number. Valid  quaternary numbers have digits [0-3]");
        }
    }
    }

}


inline int convertQuaternaryToDecimal(int number){
	
	/*
	
	Convert quaternary number to decimal equivalent. Valid quaternary numbers have digits [0-3].
	
	Args:
		number: quaternary number. Will raise error if digit is not a valid quaternary number.
	
	Return:
		Decimal number.
	
	*/

    testIfCorrectFormat(number, 'q');

    bool isNegativeNumber = false;

    if(number < 0){

        isNegativeNumber = true;
        number = abs(number);
    }

    std::string stringNum = std::to_string(number);

    long signed int total = 0;
    int j {static_cast<int>(stringNum.size())};

    for(int i=pow(4, stringNum.size() - 1); i>=1; i/=4){

          total += i * (stringNum[stringNum.size() - j] - '0');
          j -= 1;

        }

      if (isNegativeNumber){

        return ~total + 1;
    }

    return total;
}


inline long signed int convertOctalToDecimal(long signed int number){
	
	/*
	
	Convert Octal number to decimal equivalent. Valid octal numbers have digits [0-7].
	
	Args:
		number: Octal number. Will raise error if digit is not a valid octal number.
	
	Return:
		Decimal number.
	
	*/

    testIfCorrectFormat(number, 'o');

    bool isNegativeNumber = false;

     if(number < 0){

        isNegativeNumber = true;
        number = abs(number);
    }

    std::string stringNum = std::to_string(number);

    long signed int total = 0;
    int j {static_cast<int>(stringNum.size())};

    for(int i=pow(8, stringNum.size() - 1); i>=1; i/=8){

          total += i * (stringNum[stringNum.size() - j] - '0');
          j -= 1;

        }

        if (isNegativeNumber){

        return ~total + 1;
    }

        return total;

        }

inline void testIfBinary(std::string str){

    /*

    Test if string meets the criteria for a valid binary digit.
    Valid binary digits are [0, 1]

    Args:
        str: string to be evaluated for validity.

    */

    bool match = false;
    int numOfMatches = 0;

    constexpr std::array<char, 16> binaryChar {{'0', '1'}};

    for(auto i: binaryChar){

        for(auto j: str){

            if(i == j) numOfMatches +=1;
        }
    }

    if(numOfMatches == str.size()) match = true;

    if (not match){

        throw std::invalid_argument("Non-binary number passed");
    }
}

inline long signed int convertBinaryToDecimal(std::string bin){

    /*

    Converts binary number to decimal equivalent.

    Args:
        number: string number representing binary digit to be converted to decimal.

    Return:
        Decimal number.
    */

    testIfBinary(bin);

    int total = 0;
    int j = 0;

    for(int i=pow(2, bin.size() - 1); i>=1; i/=2){

        total += i * (bin[j] - '0');
        j += 1;

    }

    return total;
}


inline std::string convertDecimalToBinary(long signed int number){
	
	/*
	
	Converts an int to the decimal equivalent.
	
	Args:
		number: long int number to be evaluated.
		
	Return: string of a binary number, denoted with '0b' at the beginning to ensure the output is read correctly as a binary number. 
	
	*/

    int quotient = number;
    std::string binNum;

    while (quotient > 0) {

        int remainder {quotient % 2};
        quotient /= 2;

        binNum += std::to_string(remainder);

    }

    // reverse the order to be read as binary
    std::reverse(binNum.begin(), binNum.end());

    return "0b" + binNum;

}

inline void testIfHexadecimal(std::string number){
	
	/*
	
	Test if string meets the criteria for a valid hexadecimal digit.
	
	Args:
		number: string to be evaluated for validity. 
	
	*/
    
    bool match {false};
    int numOfMatches { 0 };
    
    constexpr std::array<char, 16> hexDecimalCharacters { {
                                                              '0', '1', '2', '3', '4', '5', '6',
                                                              '7', '8', '9', 'A', 'B', 'C', 'D',
                                                              'E', 'F'
                                                            }
                                                        };
   
   for(auto i: hexDecimalCharacters){
       
       for(auto j: number){
           
           if(i == j) numOfMatches +=1;
       }
   }
   
    if(numOfMatches == number.size()) match = true;
        
    if (not match){
        
        throw std::invalid_argument("Non-hexadecimal number passed");
    }
}

inline long int covertHexadecimalToDecimal(std::string sequence){
	
	/*
	
	Converts a hexadecimal string to the decimal equivalent.
	
	Args:
		sequence: hexadecimal string to be converted to decimal. If not a valid hexadecimal digit, will raise argument error.
	
	Return:
		long int.
	
	*/
    
   testIfHexadecimal(sequence);
    
    std::map<char, int>charMap;
    
    charMap['A'] = 10;
    charMap['B'] = 11;
    charMap['C'] = 12;
    charMap['D'] = 13;
    charMap['E'] = 14;
    charMap['F'] = 15;
    
    int j, total;
    
    j = 0;
    total = 0;
    
    for(int i=pow(16, sequence.size() - 1); i>=1; i/=16){
    
        if(sequence[j] == 'A'){
        
            total += i * charMap['A'];
            j += 1;
            
        }else if (sequence[j] == 'B'){
            
            total += i * charMap['B'];
            j += 1;
            
        }else if (sequence[j] == 'C'){
            
            total += i * charMap['C'];
            j += 1;
            
        }else if (sequence[j] == 'D'){
            
            total += i * charMap['D'];
            j += 1;
            
        }else if (sequence[j] == 'E'){
            
            total += i * charMap['E'];
            j += 1;
            
        }else if (sequence[j] == 'F'){
            
            total += i * charMap['F'];
            j += 1;
            
        }else{
            
            total += i * (sequence[j] - '0');
            j += 1;
        }
}

    return total;
}

inline std::string convertDecimalToHexaDecimal(long signed int number){
    
    /*
    
    Converts standard decimal number to a hexadecimal equivalent. 
    
    Args: 
        number: a decimal number to be converted to hexadecimal.
    
    Return:
        string formatted with an 'h' at the end to make sure the output is 
        differentiated from another number system. 
    
    */
    
    int quotient = number;
    std::string hexNum;
    
    while (quotient > 0) {

        int remainder = quotient % 16;
        quotient /= 16;
        
        if(remainder == 10) hexNum += 'A';
        else if (remainder == 11) hexNum += 'B';
        else if (remainder == 12) hexNum += 'C';
        else if (remainder == 13) hexNum += 'D';
        else if (remainder == 14) hexNum += 'E';
        else if (remainder == 15) hexNum += 'F';
        else hexNum += std::to_string(remainder);

    }

    // reverse the order to be read as hexadecimal
    std::reverse(hexNum.begin(), hexNum.end());
    
    return hexNum + 'h';
}