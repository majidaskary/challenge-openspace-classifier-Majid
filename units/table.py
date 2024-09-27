#

class Seat:

    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self,name):    ##which allows the program to assign someone a seat if it's free
        self.free = False 
        self.occupant = name

    def remove_occupant(self):  #which  remove someone from a seat and return the name of the person occupying the seat before
        self.free = True
        self.occupant = ""


class Table:
    def __init__(self):
        self.capacity = True  #which is an integer
        self.seats = ""     #a list of `Seat` objects (size = `capacity`)

    def has_free_spot(self):    #that returns a boolean (True if a spot is available)
        pass
    
    def assign_seat(self,name): # that places someone at the table
        pass

    def left_capacity(self):    # that returns an integer
        pass


