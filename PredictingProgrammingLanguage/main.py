import re

"""
Using Regular Expressions, make a function that takes a string as input and outputs the type of programming language our program predicts the input is,
based on specific syntax and keywords of different programming languages. 

"""

def python_regex_queries(keyword_1: str, keyword_2: str, keyword_3: str, keyword_4: str):

    """

    Args:
        keyword[1-4]
        Each keyword arg takes a regular expression string that represents a unique keyword or statement to the python language.
    Returns:
        A list of compiled regex expressions. 
    
    """
    a = re.compile(keyword_1)
    b = re.compile(keyword_2)
    c = re.compile(keyword_3)
    d = re.compile(keyword_4)
    python_query_searches = [a, b, c, d]

    return python_query_searches

def javascript_regex_queries(keyword_1: str, keyword_2: str, keyword_3: str, keyword_4: str):

    """

    Args:
        keyword[1-4]
        Each keyword arg takes a regular expression string that represents a unique keyword or statement to the javascript language.
    Returns:
        A list of compiled regex expressions. 
    
    """
    e = re.compile(keyword_1)
    f = re.compile(keyword_2)
    g = re.compile(keyword_3)
    h = re.compile(keyword_4)
    javascript_query_searches = [e, f, g, h]

    return javascript_query_searches

def search_for_regex(query: str, list_of_regex, show_matches: bool=False):

    """

    Args:
        query:
        string query to search through attempting to find a regex match
        
        list_of_regex:
        a list of regular expression queries (specific to the python language)

        show_matches:
        if True print out the matches, and their corresponding positions in the query. 

    Returns[int]:

        The number of regular expression matches found.

        
    """
    
    num_of_matches = 0
    
    for i in list_of_regex:
        if show_matches:
                       
             print(i)
             print(i.search(query))
             print(i.findall(query))
             print(len(i.findall(query)))
                       
        if(len(i.findall(query))) > 0:
            num_of_matches +=1
                       
    return num_of_matches

def c_cpp_regex_queries(keyword_1: str, keyword_2: str, keyword_3: str, keyword_4: str):

    """

    Args:
        keyword[1-4]
        Each keyword arg takes a regular expression string that represents a unique keyword or statement to the C/C++ language(s).
    Returns:
        A list of compiled regex expressions. 
    
    """
    i = re.compile(keyword_1)
    j = re.compile(keyword_2)
    k = re.compile(keyword_3)
    l = re.compile(keyword_4)
    c_cpp_query_searches = [i, j, k, l]
    return c_cpp_query_searches

def determine_programming_language(query: str):

    """

    Using Regular Expressions, make a function that takes a string as input and outputs the type of programming language our program predicts the input is,
    based on specific syntax and keywords of different programming languages. 

    Args:
        query - a string to search to determine type of programming language.

    Returns:
        string of [python, javascript, c/c++] based on the prediction function makes.

    
    """

    # Declare regular expression queries
    python_regex_list = python_regex_queries('def', 'import', 'print', '#[a-z]')
    javascript_regex_list = javascript_regex_queries('function', 'let', 'console.log', 'for.let')
    c_cpp_regex_list = c_cpp_regex_queries('include<', 'using namespace', 'std', 'cout')

    # Get the number of matches 
    num_of_python_matches = search_for_regex(query, python_regex_list, False)
    num_of_javascript_matches = search_for_regex(query, javascript_regex_list, False)
    num_of_cpp_matches =search_for_regex(query, c_cpp_regex_list, False)
    
    if num_of_python_matches > num_of_javascript_matches and num_of_python_matches > num_of_cpp_matches:
        return 'Python'
    elif num_of_javascript_matches > num_of_python_matches and num_of_javascript_matches > num_of_cpp_matches:
        return 'JavaScript'
    elif num_of_cpp_matches > num_of_python_matches and num_of_cpp_matches > num_of_javascript_matches:
        return 'C/C++'
    else:
        return 'Cannot determine the programming language'

if __name__ == '__main__':

    python_string = """

                import random
                from numpy import array

                # This is a python comment!
                def hello_world():
                    
                    print('Hello World')

                
                random_num = random.random()

                numpy_array = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


                    """
    
    javascript_string = """

                        function finiteAutomata(sequence) {

                        /*

                        Automaton that receives an input of 0's and 1's, the output is either accept(true) or reject(false)

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

                            console.error('Type of Arg: Sequence is not iterable. Must be of type string');
                            
                        }
                    
                        
                        if (typeof(sequence) !== 'string'){

                            console.error('Arg: sequence must be of type string');
                        }

                        if (numOfElse > 0){

                            console.error('Arg: sequence must contain only 0 and 1');
                        }

                        let lastIndexOf1 = sequence.lastIndexOf('1');
                        let numOfZeros = sequence.slice(lastIndexOf1 +1).length;

                        // check if the last character is a 1
                        if(sequence[sequence.length - 1] === '1') return 'accept';

                        // If even number of 0's following the last 1 found in the sequence
                        else if (numOfZeros % 2 === 0) return 'accept';

                        else return 'reject';

                    }

                        console.error('Error')
                        console.log('Log')



                        """
    
    cpp_string = """

            #include <iostream>
            #include <string>

            using namespace std;

            int calculateSquare (int x){

                int result = x * x;

                return result;

            }

            int addition (int x, int y){

                int r = x + y;
                return r;
            }

            int main(int argc, char const *argv[])
            {
                /* code */

                int x = 10;
                int y = 20;

                if (x < y)
                {
                    cout << x <<" Is less than " << y << endl;
                }
                else cout << x << " Is not less than " << y << endl;

                int n = 0;

                while (n < 50)
                {
                    /* code */
                    cout << n <<",";
                    n += 1;
                }

                cout << "\n";
                // int arr [5] = {1, 2, 3, 4, 5};

                int calculate = calculateSquare(10);

                cout <<"The result Is: \n"<< calculate;

                int z = addition(100, 100);

                cout << "\nThe result is: \n" <<z;

            
                string str = "\nthis is a string";

                cout << str <<endl;

                string alphabet = "\nabcdefghi";

                cout << alphabet <<endl;

                string chars = "jklmnopqrstuvwxyz";

                alphabet.append(chars);

                cout << chars;

                cout << "\nAppended string: "<< alphabet << endl;


                // Get the square root of numbers from 1 - 100
                for(int i = 1; i < 100; i++){

                    cout << calculateSquare(i) << endl;

                }

                return 0;
            }



                """
    print(determine_programming_language(query=python_string))
    print(determine_programming_language(query=javascript_string))
    print(determine_programming_language(query=cpp_string))