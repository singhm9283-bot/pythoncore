# It is used to call the method when class instance is created.....
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
        
student=Student("Alice")        
