class cars:
   def __init__(self,name,color):
       self.name=name
       self.color=color
   def intro(self):
       print("my car is ",self.name)
car=cars("ferrari","red")
print(car.intro())           