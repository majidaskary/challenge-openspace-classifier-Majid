#
class Openspace:
    def __init__(self):
        self.tables = ""  # is a list of `Table`. _(you will need to import `Table` from `table.py`)
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

