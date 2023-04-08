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
    # Assigns the dictionary to the variable
    dictionary = functions.friends_to_dictionary()
    
    # Asks for users' input of a name
    friend = str(input('Enter the name: '))
    
    # Prints all friends of users' imput
    print(functions.all_my_friends(friend, dictionary))
    
    # Prints the number of friends each person has
    functions.friendship_degree(dictionary)

main()

