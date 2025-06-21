function dartsGame() {
	
	// Initialize the score to 501 (standard starting score of a game of darts)
    let player1Score = 501;
    // let player2Score = 501;
	
	// If the player reaches a score of exactly 0 they win
    while((player1Score !== 0)){

        let player1FirstDart = parseInt(prompt('Player 1 throw your first dart'));
        let checkDart1 = prompt('Single, Double, Triple?');

        if(checkDart1 === 'double'){

            player1FirstDart *= 2;
        }

        if(checkDart1 === 'triple'){

            player1FirstDart *= 3;
        }

        player1Score -= player1FirstDart;

        if(player1Score < 0){

            console.log('bust!');
            player1Score += player1FirstDart;
        }

        console.log(`Player 1 first dart: ${player1FirstDart} New score for player1: ${player1Score + player1FirstDart} - ${player1FirstDart} = 
                    ${player1Score}`)
        
        
        let player1SecondDart = parseInt(prompt('Player 1 throw your second dart'));
        
        let checkDart2 = prompt('Single, Double, Triple?');
        
        if(checkDart2 === 'double'){

            player1SecondDart *= 2;
        }

        if(checkDart2 === 'triple'){

            player1SecondDart *= 3;
        }

        player1Score -= player1SecondDart;

        if(player1Score < 0){

            console.log('bust!');
            player1Score += player1SecondDart;
        }

        console.log(`Player 1 Second dart: ${player1SecondDart} New score for player1: ${player1Score + player1SecondDart} - ${player1SecondDart} = 
                    ${player1Score}`)
        
        let player1ThirdDart = parseInt(prompt('Player 1 throw your third dart'));

        let checkDart3 = prompt('Single, Double, Triple?');
        
        if(checkDart3 === 'double'){

            player1ThirdDart *= 2;
        }

        if(checkDart3 === 'triple'){

            player1ThirdDart *= 3;
        }

        player1Score -= player1ThirdDart;

        if(player1Score < 0){

            console.log('bust!');
            player1Score += player1ThirdDart;
        }

        console.log(`Player 1 Third dart: ${player1ThirdDart} New score for player1: ${player1Score + player1ThirdDart} - ${player1ThirdDart} = 
                    ${player1Score}`)
           
    }

    console.log('You won!');
    
}