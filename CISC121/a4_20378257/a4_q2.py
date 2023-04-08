'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

from functions import *

string1 = input('Enter the string: ')

# Checks for the conditions from the assignment
try:
    uppercase1 = string1.upper()

    if (' ' not in uppercase1) and (uppercase1 != ''):
       
       # Prints entered string and sorted prime list
        print('Entered string')
        print(uppercase1)
        print('Sorted list:')
        print(radix_sort(uppercase1))
            
    
    else:
        print('Please enter strings without spaces')

except:
    print('Please enter strings')
