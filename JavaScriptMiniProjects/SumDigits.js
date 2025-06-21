function sumDigits(digits) {

    // convert the argument digits to string format so that we can iterate and add to array

    const strDigits = digits.toString();

    const strArr = [];

    for(let ii of strDigits){

        strArr.push(ii);
    }

    // convert the strings back to numbers so we can sum the numbers

    const numArr = [];

    for(let ii of strArr){

    numArr.push(parseInt(ii))
    
    }

    const sumValues = numArr.reduce((x, y) => x + y);

    return sumValues;

    
}