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
    // else throw std::invalid_argument("arg: type must be ['o (octal)', 'q(quaternary)']");
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