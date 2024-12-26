class houses:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def intro(self):
        print("my house is ",self.name)
house=houses("large","blue")
print(house.intro())    
           
    