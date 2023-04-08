'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email:  22bh17@queensu.ca
Date: 2023-01-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''
import random

def addMyself(file):        # Adds myself to the file
    file.write("Dmytro Zaichenko \n")
    file.write("18 \n")
    file.write("orange \n")
    file.write("- \n")


def addUser(file):      # Adds a user input to the list
    colors = ['green','red','yellow','pink','blue','orange']
    
    name = input('Please enter a name you want to add: ')
    age = random.randint(18,22)     #Random age
    color = colors[random.randint(0,5)]     #Random color


    file.write(name + "\n")
    file.write(str(age) +'\n')
    file.write(color +'\n')
    file.write("- \n")

def main():
    file = open("myspace_profiles.txt", "a")
    
    addMyself(file)
    addUser(file)
    
    file.close()
    
    file = open("myspace_profiles.txt", "r")
    print(file.read())
    

main()