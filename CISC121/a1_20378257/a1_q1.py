'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email:  22bh17@queensu.ca
Date: 2023-01-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''
import random

def generate():     # Generates 2 random numbers unless one of them (t) is larger
    t=0
    k=1
    
    while t<k:
        t = random.randint(0,100)
        k = random.randint(0,100)
    
    return t,k


def checkValidity(t,k):     # Checks if the given conditions were met
    check = True
    print("Two randomly generated integer numbers are " + str(k) + " and " + str(t))
    
    while check:
            if (t-k)<10:
                print("This pair of integers is invalid")
                t=t*2
                print("Larger number was replaced with "+str(t))

            elif (t-k)>50:
                print("This pair of integers is invalid")
                t=int(t/3)+(t%3>0)                                  # Rounds UP
                print("Larger number was replaced with "+str(t))
 
            else:
                print("This pair of integers is valid")
                check = False
    
    return t,k

def output(t,k):        
    print('Output for the valid numbers ' + str(k) + ',' + str(t) + ':')
    
    while k != t+1:
        result = []     # Creates a list for the words
        
        if (k%5)==0:                # If a multiply of 5
            result.append('apple')
        if (k%7)==0:                # If a multiply of 7
            result.append('pen')
        if ('3' in str(k)):         # If there is 3 in the number
            result.append('pineapple')

        if len(result)>0:           # If there are any words in the list it the list, putting spaces between them
            print(" ".join(result))
            k=k+1
        
        else:
            print(k)                # If none of conditions is met then just prints a number
            k=k+1

        


def main():
    numbers = generate()
    t,k = numbers[0],numbers[1]     # Numbers before ValidityCheck
    
    goodNumbers = checkValidity(t,k)        # Numbers that are good 
    t,k = goodNumbers[0],goodNumbers[1]
    
    output(t,k)


main()