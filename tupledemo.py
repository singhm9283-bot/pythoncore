# tuple is immutable....
myFriends=("Rim","Anika","sonal","charu","Amita","Kartikey")
print(type(myFriends))

#to access values from the tuple....
for i in myFriends:
    print(i)
    
newl=list(myFriends)
newl.remove("Anika")

for j in newl:
    print(j)
index=newl.index("charu")
newl[index]="Charu jazz"
for k in newl:
    print(k)