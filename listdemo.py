#list is a collection of different types of datasets----->>>
myFriends=["Muskan","anika","Sonal","Rimjhim","Kartikey"]
print(type(myFriends))


print(myFriends)
#to  iterate the data items from the list.....
for i in myFriends:
    print(i)
    
    
#append new friend into the list.....
myFriends.append("Aashish")

#to add the friend at the specific location.....
myFriends.insert(0,"Khushi")

#removing element from the list....
myFriends.remove("Khushi")



#to check over a friend..........
if "Aashish" in myFriends:
    print("Aashish is my friend.....")
else:
    pass

#check for pawan...if present then remove and if not present then append in the list....
if "Pawan" in myFriends:
    myFriends.remove("Pawan")
else:
    myFriends.append("Pawan")  
    
     
#to identify the index......  
output=myFriends.index("Pawan")
print(output)
 
#print the final list.....
for i in myFriends:
    print(i)    
    
    

#update the name when value is duplicate ......
myFriends.clear()
print(myFriends)

#create a list of hotel using class and function
#add, delete, update, access, sort the hotel follow SRP

