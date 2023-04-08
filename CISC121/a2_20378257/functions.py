'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email:  22bh17@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

def all_odd_or_even(args):
    """
 -------------------------------------------------------
Checks if the integers given are all odd or all even.
Also checks for some other minor conditions mentioned
in the assignment.
-------------------------------------------------------
Parameters:
      args - list with the arguments
Returns:
      Boolean True or False
-------------------------------------------------------
    """
    
    try:
        
        # If there are more than 0 integers it goes on
        if len(args)>0:
            
            check = 0

            # Checks every value and if it's EVEN it +1 to the check variable, if ODD than -1 to the check value
            # And after this it compares this variable with the length of the initials args list
            # If they are equal it means they are all either EVEN or ODD
            for arg in args:
                
                if (isinstance(arg,int)) and (arg%2==0):
                    check += 1
                elif (isinstance(arg,int)) and (arg%2!=0):
                    check -= 1
            
            if abs(check) == len(args):
                return True

            else:
                return False
        
        else:
            return False
    
    except:
        return False

def friends_to_dictionary():
    """
 -------------------------------------------------------
Assigns the data from the file to the dictionary.
-------------------------------------------------------
Parameters:
      None
Returns:
      dictionary
-------------------------------------------------------
    """
    dictionary = {}
    file = open('friendship.txt','r')
    
    # Splits every line to the key and value
    for line in file:
        (key,val) = line.split()
        dictionary[key] = val
    
    return dictionary

def all_my_friends(friend, dictionary):
    """
 -------------------------------------------------------
Prints all friends of the users' input friend
-------------------------------------------------------
Parameters:
      friend - users' input
      dictionary - data with connections
Returns:
      friendList - list with friends
-------------------------------------------------------
    """
    # Creating lists from the data for the more convenient work
    key_list = list(dictionary.keys())
    value_list = list(dictionary.values())
    friendList = []

    # Checks keys for the user input and adds values to the friendList
    for k in range(len(key_list)):
        if friend == key_list[k]:
            friendList.append(value_list[k])
    
    # Checks values and adds keys
    for b in range(len(value_list)):
        if friend == value_list[b]:
            friendList.append(key_list[b])

    return friendList

def friendship_degree(dictionary):
    """
 -------------------------------------------------------
Prints the number of friends each person from the
dictionary has.
-------------------------------------------------------
Parameters:
      dictionary - data
Returns:
      None
-------------------------------------------------------
    """
    # Creating lists from the data for the more convenient work
    key_list = list(dictionary.keys())
    value_list = list(dictionary.values())
    
    # Does the same thing as previous function but for each name
    for k in range(len(key_list)):
        friendList = []
        friendList.append(value_list[k])
        
        for b in range(len(value_list)):
            if key_list[k] == value_list[b]:
                friendList.append(key_list[b])
        
        print(str(key_list[k]), 'has', str(len(friendList)), 'friends:', ", ".join(friendList))

