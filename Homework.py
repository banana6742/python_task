#1
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

    def circumstance(self):
        return 2*3.14*self.radius

C = Circle(int(input("Enter the radius :")))
print(C.area())
print(C.circumstance())

#2
class Cel():
    def __init__(self,celsius):
        self.celsius = celsius

    def convertC(self):
        return (self.celsius*1.8)+32

cel = Cel(int(input("Enter the temperature in celcius:")))
# f = (celsius*1.8)+32
print("Temperature in farenheit is :" ,cel.convertC())

class Faf():
    def __init__(self,farenhiet):
        self.farenhiet = farenhiet

    def convertF(self):
        return (self.farenhiet-32)*1.8

Faf = Faf(int(input("Enter the temperature in farenhiet:")))

print("Temperature in farenheit is :" ,Faf.convertF())

#3
class Student():
    def __init__(self,name,age,marks):
       self.name = name
       self.age = age
       self.marks = marks

    def display(self):
        return f'The student name is {self.name}, age is {self.age},his mark is {self.marks}'
    
student = Student('ryota',28,"A")
print(student.display())

#4
class Time():
    def __init__(self,hours,mins):
        self.hours = hours
        self.mins = mins
    
    def addTime(t1,t2):
        t3 = Time(0,0)
        if t1.mins+t2.mins>60:
            t3.hours =round((t1.mins+t2.mins)/60)
        t3.hours = t3.hours+t1.hours+t2.hours
        t3.mins = (t1.mins+t2.mins)+(t1.hours+t2.hours)*60-t3.hours*60
        return t3

    def displayTime(self):
            print("Time is", self.hours, "hours and", self.mins, "minutes.")
        
    def displayMinute(self):
            print(self.hours*60+self.mins)

# a = Time(int(input("Enter the hrs :")),50)
# b = Time(int(input("Enter the hrs :")),20)
# b = Time(int(input("Enter the hrs :")),int(input("Enter the minutes :"))

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
