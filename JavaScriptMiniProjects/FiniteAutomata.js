function finiteAutomata(sequence) {

    /*

    Automaton that recieves an input of 0's and 1's, the output is either accept(true) or reject(false)
	
	The determination for whether the automaton accepts the input is based on a 3 - component system with the ACCEPT state being the second.

    Args: 
        Sequence[string]: A string of 0's and 1's

    Return:
        True if sequence ends with 1, or if sequence ends with even number of 0's following the last 1

    */

    // Check to make sure sequence is a string of only 0 or 1

    let numOf0s = 0;
    let numOf1s = 0;
    let numOfElse = 0;

    try {
        
    for(let i of sequence){

        if(i === '0') numOf0s += 1;
        else if (i === '1') numOf1s += 1;
        else numOfElse += 1;
        
    }
        
    } catch (error) {

        console.error(`Type of Arg: ${typeof(sequence)} is not iterable. Must be of type string`);
        return null;
        
    }
   
    // If user tries to pass an array or other object
    if (typeof(sequence) === 'object'){

        console.error('Arg: sequence must be of type [string] not type [object]');
        return null;
    }

    if (numOfElse > 0){

        console.error('Arg: sequence must contain only 0 and 1');
        return null;
    }

    let lastIndexOf1 = sequence.lastIndexOf('1');
    let numOfZeros = sequence.slice(lastIndexOf1 +1).length;

    // check if the last character is a 1
    if(sequence[sequence.length - 1] === '1') return 'accept';

    // If even number of 0's following the last 1 found in the sequence
    else if (numOfZeros % 2 === 0) return 'accept';

    else return 'reject';

}