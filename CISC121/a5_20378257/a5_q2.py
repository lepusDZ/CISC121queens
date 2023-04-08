from Stack_class import *

'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

if __name__ == '__main__':
    # Initializing
    s = Stack()

    print('Our stack now:')
    print(s)

    # Checks if the stack is empty
    print('Stack is empty:')
    print(s.is_empty())

    # Pushing values
    print('Adding values...')
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(21)
    s.push(30)
    
    print('Our stack now:')
    print(s)
    

    # Popping two last values
    print('Doing two pops')
    s.pop()
    s.pop()
    
    print('Our stack now:')
    print(s)
    
    # Checks if the stack is empty
    print('Stack is empty:')
    print(s.is_empty())

    # Shows the top value of the stack
    print('Stack peek:')
    print(s.peek())

    # Shows the size of the stack
    print('Stack size:')
    print(s.size())

    # Reverses the stack
    print('Reversing the stack..')
    s.reverse()
    print('Our stack now:')
    print(s)

    # Reverses it again
    print('Reversing the stack..')
    s.reverse()
    print('Our stack now:')
    print(s)
