#it is a process to inherit the properties from one class to another class
class simpleCalc:
    def add(self,a,b):
        return a+b
    
    
class complexCalc(simpleCalc):
    print("Use  of inheritence")
    
    
#create an instance of ComplexCalc
calc=complexCalc()
print(calc.add(3,5))

#create a class simplecalc --->add, sub, mul, div
#inherit the simplecalc in complexcalc-----mod ,power ,sqroot, percentage, fact

class simpleCalc:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    
        
    
    