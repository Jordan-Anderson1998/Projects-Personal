function lottoGame(cheat=false) {

    let numOfGuesses = 0;
    let generatedNumbers = [];
    let userGuesses = [];

    while (numOfGuesses <= 6) {

        let randomNum = Math.floor(Math.random()* 50) + 1;
        if(cheat) console.log(randomNum);
        let guess = parseInt(prompt('Enter your guess between 1 and 50'));

        if((guess <= 0) || (guess > 50)) {
            
            console.error('Number Guess must be in the range [1, 50]');
            break;

        }

        console.log(`Computer Generated Random Number: ${randomNum} |  User guess: ${guess}`);

        generatedNumbers.push(randomNum);
        userGuesses.push(guess);

        numOfGuesses += 1;
    }
    // Set to -1 to compensate for undefined being compared and returning true, thus adding 1 to correctGuesses
    let correctGuesses = -1;


    for(let i = 0; i <= userGuesses.length; i++){

        if(userGuesses[i] === generatedNumbers[i]){

            correctGuesses += 1
        }
    }
    // for(let i of generatedNumbers){

    //     for(let j of userGuesses){

    //         if(j === i){

    //             correctGuesses += 1;
    //         }
            
    //     }
    // }

    if(correctGuesses === 0){
        
        console.log(`Sorry, you got 0 of 7 numbers correct`);

        return null;
    
    }

    else if ((correctGuesses === 1) || (correctGuesses === 2)) {
        
        console.log(`You got ${correctGuesses} numbers correct. You get a free play`);

        return 'Free Play';

    }

    else if (correctGuesses === 3){

        console.log('You got 3 guesses correct. You get a free play + $10 dollars');
        
        return 'Free Play + $10';
    }

    else if (correctGuesses === 4){

        console.log('You got 4 guesses. You won $100!');
        
        return 100;
    }

    else if ((correctGuesses === 5) || (correctGuesses === 6)){

        console.log(`Congratulations! You got ${correctGuesses} numbers correct out of 7. You get $100,000!`);

        return 100000;
    }

    else {

        console.log('You won the jackpot! You get 50,000,000!');
        return 50000000;
    }
    
}