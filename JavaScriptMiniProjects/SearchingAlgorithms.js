// Prints out the number of searches required to find the target as well

function binarySearchAlgorithm(array, target) {
	
	/* Given an array of numbers search for a target. Note that the array must be SORTED in order for this algorithm to work properly.
	
		Args:
			array: array of numbers to search
			target[int]: the number to search for

	
	*/

    let left = 0;
    let right = array.length - 1;
    let numOfSearches = 1;
    
    while (left <= right){
        let middle = Math.floor((left + right) / 2);
        let middleIndex = array[Math.round(middle)];
    
        console.log(`left:${left}, right:${right}, middle:${middle}, middle value:${middleIndex}`);
    
        if(target === middleIndex) {
            
            console.log(`Found Match ---> Index: ${array.indexOf(target)}, Value: ${array[array.indexOf(target)]}`);
            console.log(`Number of searches required: ${numOfSearches}`)
            break;
        
        }
    
        // if target is less than the number at middle index; shift the right-most index 
        else if (target < middleIndex){
            
            right = (middle - 1);
            numOfSearches += 1;}
    
        // if target is greater than number at middle index; shift the left-most index to the middle of the array
        else {
            left = (middle + 1)
            numOfSearches += 1;;
        }
     }
}

function linearSearchAlgorithm(array, target) {

    let numberOfSearches = 1;

    for(let ii of array){
        
        numberOfSearches += 1;
        if(ii === target){ 
            
            console.log(`Found: ${ii}, at index: ${arr.indexOf(ii)}`);
            console.log(`Number of searhces required: ${numberOfSearches}`);
        
        }

    }

}