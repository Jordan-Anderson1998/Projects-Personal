inline void testIfCorrectFormat(int testNumber, char type){

    // if octal number
    if(type == 'o'){

        std::string stringNum = std::to_string(testNumber);

        for(int i=0; i<=stringNum.size(); i++){

            if(stringNum[i] >= '8'){

                // printf("%d is an incorrect Octal number", number);
                throw std::runtime_error("Cannot compute non-octal number.");
        }
    }
    }

      // if quaternary number
    if(type == 'q'){

        std::string stringNum = std::to_string(testNumber);

        for(int i=0; i<=stringNum.size(); i++){

            if(stringNum[i] >= '4'){

                // printf("%d is an incorrect Octal number", number);
                throw std::runtime_error("Cannot compute non-quaternary number.");
        }
    }
    }

    // if binary number
    if(type == 'b'){

        std::string stringNum = std::to_string(testNumber);

        for(int i=0; i<=stringNum.size(); i++){

            if(stringNum[i] > '1'){

                throw std::runtime_error("Cannot compute non-binary number.");
            }

        }
    }
}

inline void testIfCorrectDataType(int number){

    if (typeid(number) != typeid(int)){

        throw std::invalid_argument("Arg: number must be of type int");
    }
}

inline int convertQuaternaryToDecimal(int number){

    testIfCorrectFormat(number, 'q');
    testIfCorrectDataType(number);

    bool isNegativeNumber = false;

    if(number < 0){

        isNegativeNumber = true;
        number = abs(number);
    }

    std::string stringNum = std::to_string(number);

    int total = 0;

    int j = stringNum.size();

    for(int i=pow(4, stringNum.size() - 1); i>=1; i/=4){

          total += i * (stringNum[stringNum.size() - j] - '0');
          j -= 1;

        }

      if (isNegativeNumber){

        return ~total + 1;
    }

    return total;
}


inline int convertOctalToDecimal(int number){

    testIfCorrectFormat(number, 'o');
    testIfCorrectDataType(number);

    bool isNegativeNumber = false;

     if(number < 0){

        isNegativeNumber = true;
        number = abs(number);
    }

    std::string stringNum = std::to_string(number);

    int total = 0;

    int j = stringNum.size();

    for(int i=pow(8, stringNum.size() - 1); i>=1; i/=8){

          total += i * (stringNum[stringNum.size() - j] - '0');
          j -= 1;

        }

        if (isNegativeNumber){

        return ~total + 1;
    }

        return total;

        }

inline long signed int convertBinaryToDecimal(long signed int number){

    // testIfCorrectFormat(number, 'b');

    bool isNegativeNumber = false;

    if(number < 0){

        isNegativeNumber = true;
        number = abs(number);
    }

    std::string stringNum = std::to_string(number);

    int total = 0;

    int j = 0;

    for(int i=pow(2, stringNum.size() - 1); i>=1; i/=2){

        total += i * (stringNum[j] - '0');
        j += 1;

    }

    if (isNegativeNumber){

        return ~total + 1;
    }

    return total;
}

inline std::string convertDecimalToBinary(long signed int number){

    int quotient = number;
    std::string binNum = "";

    while (quotient > 0) {

        int remainder = quotient % 2;
        quotient /= 2;

        binNum += std::to_string(remainder);

    }

    // reverse the order to be read as binary
    std::reverse(binNum.begin(), binNum.end());

    return "0b" + binNum;

}

void testIfHexidecimal(std::string number){
    
    bool match = false;
    int numOfMatches = 0;
    
     std::array<char, 16> hexDecimalCharacters = {'0', '1', '2', '3', '4', '5', '6',
                                                  '7', '8', '9', 'A', 'B', 'C', 'D',
                                                  'E', 'F'
                                                 };
   
   for(auto i: hexDecimalCharacters){
       
       for(auto j: number){
           
           if(i == j) numOfMatches +=1;
       }
   }
   
    if(numOfMatches == number.size()) match = true;
        
    if (not match){
        
        throw std::invalid_argument("Cannot compute non-HexiDecimal number");
    }
	
	return;
}

long int covertHexadecimalToDecimal(std::string sequence){
    
   testIfHexidecimal(sequence);
    
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