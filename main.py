
import pandas as pd
import numpy as np
import random
#import csv




# table.py ________________________________________________________________________________________
#__________________________________________________________________________________________________

class Seat:

    def __init__(self,free,occupant):
        self.free = True
        self.occupant = names    # names is the list of names in the begining 

    def set_occupant(self,name):    #which allows the program to assign someone a seat if it's free
        if counter_empty_seat>0:
            # assign someone a seat   <<<<==== write a code
            counter_empty_seat -= 1
        else:
            print("there is no empty seat!")    

    def remove_occupant(self):  #which  remove someone from a seat and return the name of the person occupying the seat before
        pass


class Table:
    def __init__(self,capacity,seats):
        self.capacity =   #?   #which is an integer
        self.seats = ""     #a list of `Seat` objects (size = `capacity`)
    def has_free_spot(self):    #that returns a boolean (True if a spot is available)
        if counter_empty_seat>0:
            True
    def assign_seat(self,name): # that places someone at the table
        pass
    def left_capacity(self):    
        print(counter_empty_seat)  # the rest of empty seats




# openspace.py ____________________________________________________________________________________
#__________________________________________________________________________________________________

class Openspace:
    def __init__(self,tables,number_of_tables):
        self.tables = names = ['table_1', 'Basma', 'Dhrisya', 'Ihor', 
         'Izabela', 'Kelli']  # is a list of `Table`. _(you will need to import `Table` from `table.py`

        self.number_of_tables = 6   # len(list...) 
    
    def organize(self,name):    #**randomly** assign people to `Seat` objects in the different `Table` objects.
                
        """
        array_test_3 = np.full((table_numbers,seat_numbers),0)
        array_occu_buffer = np.full((occupant_numbers),0)
        Counter_occu = 0
        for i in range(table_numbers):
          for j in range(seat_numbers):    
              array_test_3[i,j] = array_occu_buffer[Counter_occu] = random.randint(1,occupant_numbers)
              #if repeat(array_occu_buffer[Counter_occu], array_occu_buffer):
              #print("repeat")
              Counter_occu+=1
            """
    
    def display(self):  #display the different tables and there occupants in a nice and readable way
        pass

    def store(self,filename):   #store the repartition in an excel file
        pass



# main.py _________________________________________________________________________________________
#__________________________________________________________________________________________________

seat_array = np.full((6,4),"empty")   # row & column should be input by user
#print (seat_array)
counter_empty_seat = 24   # can input by user / in the begining all thee seats are empty

#names = pd.read_csv('./address of csv file')
names = ['Anastasiia', 'Basma', 'Dhrisya', 'Ihor', 
         'Izabela', 'Kelli', 'Kevin', 'Levin', 
         'Maarten', 'Minh', 'Moustafa', 'Muntadher', 
         'Nicollas', 'Petra', 'Rasmita', 'Rik', 
         'Tom', 'Ursonc', 'Veena', 'Veena', 
         'Wouter', 'Yeliz', 'Yusra', 'Zelim']


organize_plan = Table()
organize_plan.__init__(24,)









"""
- Launch the organizer. Display the results


list_seats = []
for name in names:
    seat = Seat()
    seat.set_occupant(name)
    list_seats.append(seat)
"""