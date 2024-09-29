import numpy as np
import random

class seat:
    def __init__(self,seat,table,names):
        self.names = names
        self.names_number = len(names)
        self.sest = seat
        self.table = table
        self.array_plan = np.full((self.table,self.sest),"empty")
        self.array_counter = names.copy()
       
    def Openspace(self):
        for i in range(self.table):
            for j in range(self.sest): 
                k = 0  
                while k == 0:            
                    counter = random.randint(0,self.names_number-1)
                    buffer = self.array_counter[counter]
                    if buffer != "empty":
                        self.array_plan[i,j] = buffer
                        self.array_counter[counter] = "empty"
                        k = 1
                    
    def display(self):
       print(self.array_plan)
       print("\nteam leaders:\n",self.array_plan[:,0])
       
names =['Anastasiia', 'Basma', 'Dhrisya', 'Ihor', 
        'Izabela', 'Kelli', 'Kevin', 'Levin', 
        'Maarten', 'Minh', 'Moustafa', 'Muntadher', 
        'Nicollas', 'Petra', 'Rasmita', 'Rik', 
        'Tom', 'Ursonc', 'Veena', 'Veena', 
        'Wouter', 'Yeliz', 'Yusra', 'Zelim']
        
seat_plan = seat(4,6,names)
seat_plan.Openspace()
seat_plan.display()
