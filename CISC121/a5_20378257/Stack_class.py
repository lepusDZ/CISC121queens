'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        -------------------------------------------------------
        Returns:
            new Stack object
        -------------------------------------------------------
        """
        
        self.items = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return (self.items == [])

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack 
        Returns:
            None
        -------------------------------------------------------
        """
        self.items.append(value)

    def pop(self):
        """
        -------------------------------------------------------
        Pops the top of stack
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self.items.pop()


    def peek(self):
        """
        -------------------------------------------------------
        Return the copy of the last value in the stack
        -------------------------------------------------------
        Returns:
            a copy of the value at the top of stack
        -------------------------------------------------------
        """
        # If not empty, returns last value
        if not self.is_empty():
            return str(self.items[-1])

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # Initializing
        tempList = []
        
        # Adds values starting from the top of stack to the toplist
        while not self.is_empty():
            tempList.append(self.items.pop())

        # Assigns tempList to the stack, so values are reversed
        self.items = tempList


    def size(self):
        """
        -------------------------------------------------------
        Returns the length of the stack
        -------------------------------------------------------
        Returns:
            the length of the stack
        -------------------------------------------------------
        """
        return len(self.items)
    
    def __str__(self):
        """
        -------------------------------------------------------
        Make a string from the list
        -------------------------------------------------------
        Returns:
            a string (list)
        -------------------------------------------------------
        """
        return str(self.items)