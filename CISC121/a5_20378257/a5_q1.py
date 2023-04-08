from hotel_classes import *

'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''

if __name__ == '__main__':

    #Initializing
    
    Room1 = Room(1,True,0,'standart')
    Room2 = Room(2,True,0,'suit')
    Room3 = Room(3,True,0,'taylor')

    Guest1 = Guest('Andrew',27,50)
    Guest2 = Guest('Jordan',18,90)
    Guest3 = Guest('Amelia',20,30)

    print('Room number:',str(Room1.num),'| Available now:',str(Room1.avail),'| Date of checkout:', str(Room1.checkout))
    print('Room number:',str(Room2.num),'| Available now:',str(Room2.avail),'| Date of checkout:', str(Room2.checkout))
    print('Room number:',str(Room3.num),'| Available now:',str(Room3.avail),'| Date of checkout:', str(Room3.checkout))

    print()

    #Checking in Guests
    
    Room1.guest_check_in(Guest1)   
    Room2.guest_check_in(Guest2)    
    Room3.guest_check_in(Guest3)    

    print('Checking in the guests...')
    print()

    print('Room number:',str(Room1.num),'| Available now:',str(Room1.avail),'| Date of checkout:', str(Room1.checkout))
    print('Room number:',str(Room2.num),'| Available now:',str(Room2.avail),'| Date of checkout:', str(Room2.checkout))
    print('Room number:',str(Room3.num),'| Available now:',str(Room3.avail),'| Date of checkout:', str(Room3.checkout))


    #Adding services

    Guest1.add_service('Movies',100)    
    Guest1.add_service('Room service',500)

    print('Guest1 services:')
    print(Guest1.services)

    print('Guest1 total bill:')
    Guest1.send_bill()