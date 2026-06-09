#numpy is a collection of array set with high order function...
import numpy as np 
salary=np.array([8000,9000,7000,6000])
print(type(salary))
print(salary)

for data in salary:
    print(data)
    
print(salary.max())
 
print("     ")
for i in salary[2:0:-1]:
    print(i)
 #da=np.random.rand(100).reshape(10,10)

print(data)

newd=np.random.uniform(0,9,10).reshape(2,5)
print(newd[-1:-2,0:3])

#create a uniform dataset and take 100 number of elements with 10 /10 shape .....find top  row 
#elements and second last row element and the maximum values from the dataset--->>>>