'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''


def char_prime(my_char):
    """                                                                      
    -------------------------------------------------------                  
    Converts an uppercase letter to a unique prime number                    
        Based on the conversion given in the footnote                        
    -------------------------------------------------------                  
    Parameters:                                                              
        my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)                
    Returns:                                                                 
        prime_int = a prime number unique to the letter                      
    -------------------------------------------------------
    """

    #Creates two list with letters and prime numbers
    charList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

    # Assigns entered letter index to the variable
    index = charList.index(my_char)

    # Finds the number with the same index in the second list
    prime_int = prime_list[index]

    return prime_int



def primeify(my_string,tempList=None): 
    """                                                                      
    -------------------------------------------------------                  
    RECURSIVELY gives the product of primes corresponding to the letters     
            in the string                                                  
    -------------------------------------------------------                    
    Parameters:                                                              
        my_string - any string (str)                                         
    Returns:                                                                 
        prime_product = the product of all primes for each letter            
    -------------------------------------------------------                  
    """
    
    # Creates an empty list only in the beginning of the function

    if tempList == None:
        tempList = []
    
    # When length of the word is 0 it returns prime product
    if len(my_string) == 0:
        prime_product = 1

        for k in range(len(tempList)):
            prime_product *= tempList[k]
        
        return prime_product
        
    # Finds a prime number for every letter and then deletes this letter from the word
    else:

        tempList.append(char_prime(my_string[0])) 
        
        new_string = my_string[1:]
        
        return primeify(new_string, tempList)



def is_anagram(string1,string2): 
    """                                                                      
    -------------------------------------------------------                  
    Determines if two strings are anagrams of each other                     
                                                                            
    -------------------------------------------------------                  
    Parameters:                                                              
        string1, string2 - any two strings (str)                             
    Returns:                                                                 
        is_anagram = whether or not they are anagrams (Boolean)              
    -------------------------------------------------------                  
    """
    # Checks if the words are anagrams
    return primeify(string1) == primeify(string2)


def radix_sort(word):
    """
    -------------------------------------------------------
    Turns string into list of primes and then sorts it.
    -------------------------------------------------------
    Parameters:
    word - string used
    Returns:
    arr - sorted list
    -------------------------------------------------------
    """

    arr = []
    for a in word:
        arr.append(char_prime(a))

    def countingSort(arr, exp1):
        """
        -------------------------------------------------------
        Helper function that sorts an element on decimal spaces.
        -------------------------------------------------------
        Parameters:
        arr - integers list
        exp1 - the significant place
        Returns:
        None
        -------------------------------------------------------
        """

        # Initializing
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        # Count of elements
        for i in range(0, n):
            indx = arr[i] // exp1
            count[indx % 10] += 1

        # Total
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Sorting the elemnts
        i = n - 1
        
        while i >= 0:
            indx = arr[i] // exp1
            output[count[indx % 10] - 1] = arr[i]
            count[indx % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    # Finds the max
    maxF = max(arr)
 
    # Uses countingSort to sort elements based on their significant figure.
    exp = 1
    while maxF / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    return arr

