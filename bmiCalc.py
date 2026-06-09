#create a class to show th BMI----------->
#weight=69
#height=1.72
#bmi=weight/(height*height)
# class BMI:
#     def getBMI(self,w,h):
#         return w/(h*h)
# #create instance of the class......
# bmi=BMI()
# output=bmi.getBMI(69,1.72)    
# print("my BMI is ----",output)



# #create a class to claculate the area of the square------->
# length=int(input("Enter the length of the square"))
# class Square:
#     def AreaOfSquare(k,length):
#         return length*length
# arr=Square()  
# output=arr.AreaOfSquare(length)    
# print("Area of square of this lenth is---",output)




#average calculation-------->
#average=sum of values /no of values....
class Calculateavg:
    def calcAvg(self,a,b,c):
        return (a+b+c)/3

avg=Calculateavg()
output=avg.calcAvg(4,5,6)    
print("Output is ",output)
