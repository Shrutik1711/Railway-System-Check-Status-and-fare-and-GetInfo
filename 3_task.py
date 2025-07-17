# checking railway fare and and getInfo and stauts 
import random
class Railway:
    def __init__(self, TrainNo , FROM , TO):
        self.TrainNo = TrainNo
        self.FROM = FROM
        self.TO = TO
        
    def GetInfo(self):
        return f"Train No : {self.TrainNo} Destination {self.FROM} To {self.TO}"
    
    def status(self):
        return f"Train No : {self.TrainNo} is running on time"
    
    def Fare(self):
        return f"Train No : {self.TrainNo} fare is {random.randint(100,999)}"
    
RBI = Railway(15470 , "Delhi " , "Nagpur")
print(RBI.GetInfo())
print(RBI.status())
print(RBI.Fare())
        