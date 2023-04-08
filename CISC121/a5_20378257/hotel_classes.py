'''
CISC-121 2023W
Name: Dmytro Zaichenko
Student Number: 20378257
Email: 22bh17@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''


class Room:
    def __init__(self, num, avail, date, roomType):
        self.num = num
        self.avail = bool(avail)
        self.checkout = date
        self.roomType = roomType
        

    def guest_check_in(self,some_guest):
        """                                                                      
        -------------------------------------------------------                  
        Checks a guest into a room and updates availability                      
                                                                                
        -------------------------------------------------------                  
        Parameters:                                                              
            Some_guest – the guest checking in (guest object)                    
        Returns:                                                                 
            None                                                                 
        ------------------------------------------------------- 
        """
        self.avail = False
        tmp = some_guest
        tmp2 = roomType()
        #Adds to the checkout date the time to clean the room
        self.checkout = (int(tmp.checkoutDate) + int(tmp2.typed(self.roomType)))
        

class roomType:
    def __init__(self):
        self.roomT = {'standart':0,'suit':1,'taylor':2}
    
    #Returns number of days to clean the room
    def typed(self,room):
        return self.roomT[room]


class Service:
    def __init__(self):
        self.services = ['Room service', "Movies"]

class Guest:
    def __init__(self,name,date,bill):
        self.guestName = name
        self.checkoutDate = date
        self.finalBill = bill
        self.services = []

    def add_service(self, service_name, service_cost): 
        """                                                                      
        -------------------------------------------------------                  
        Adds a service to the bill of a guest                                    
                                                                                
        -------------------------------------------------------                  
        Parameters:                                                              
            Service name – name of service (str)                                 
            Service_cost - cost of the service (int)                             
        Returns:   None                                                          
        -------------------------------------------------------                 
        """
        self.services.append(service_name)
        self.finalBill += service_cost

    
    def send_bill(self):
        """
        -------------------------------------------------------                  
        Based on the total services and bill total provides a                    
            Printed statement of all services with the total cost                
        -------------------------------------------------------                  
        Parameters:     None                                                     
        Returns:        None                                                     
        -------------------------------------------------------                  
        """
        print(self.finalBill)




