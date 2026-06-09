#file handling will apply curd operations on file...
#create a file with name trainer.txt

# trainer = open("trainerfile.txt",'w')
# trainer.write("My name is Muskan Singh and I am pursuing Engineering")
# trainer.close()


# readfile = open("trainerfile.txt",'a')
# print(readfile.write("    \n  I am currently residing in Lucknow..."))

readmyfile = open("trainerfile.txt",'r')
mydata = readmyfile.read()
mynewdata = readmyfile.read()



#check whether muskan singh exist or not....
if "Muskan Singh" in mynewdata:
    print("exists")
else:
    print("not found")
