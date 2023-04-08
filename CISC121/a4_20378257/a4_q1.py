'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''


from functions import *


string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

# Checks for every condition mentioned in the assignment
try:
    uppercase1, uppercase2 = string1.upper(), string2.upper()

    if (' ' not in uppercase1) and (' ' not in uppercase2) and (uppercase1 != '' and uppercase2 != ''):
        
        # Prints the statement depending on the result
        if is_anagram(uppercase1,uppercase2) == True:
            print("It is an anagram!")
        else:
            print('It is not an anagram!')
    
    else:
        print('Please enter strings without spaces')

except:
    print('Please enter strings')

