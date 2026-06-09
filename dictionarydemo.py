# it is used to store the data in key value pairs.....
student={"name":"Muskan","Branch":"AIML","Age":21}
print(type(student))

student.update({"Branch":"CSE(AIML)"})
print(student)
student.pop("Branch")
print(student)


print(student.get("name"))