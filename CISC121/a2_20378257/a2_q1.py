'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email:  22bh17@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

import functions


def main():
    # Asks for users' input and creates an empty list
    answer = input('Do you want to participate in the activity? ("Y" or "y" to continue): ')
    intList = []
    
    # While answer is yes keeps the program going, each time asks for a new integer. 
    # If answer is something that is not yes stops the program.
    while answer=='y' or answer=='Y':
        try:
            intList.append(int(input('What integer do you want to add?: ')))
            answer = input('Do you want to keep going? ("Y" or "y" to continue): ')
        except:
            print('ERROR! Enter an integer.')
            answer='n'
        


    # Checks if the integers are odd or even
    print(functions.all_odd_or_even(intList))

main()