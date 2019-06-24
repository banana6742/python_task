class Employee:
    pass

emp=Employee()
em2=Employee()
emp='lohit'
em2='susumu'

print(emp)
print(em2)

print('-'*50)

class Person:
    pass

name=Person()
email=Person()
address=Person()
phone=Person()

name='New'
email='New@'
address='New-new'
phone='98324151'
print(name)
print(email)
print(address)
print(phone)
print('-'*50)

class MyClass:
    x = 5

print(MyClass())

print('-'*50)

class MyClass:
    x = 5

print(MyClass().x)
print('-'*50)

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
print('-'*50)

class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    
print('-'*50)

class Office:
    def __init__(self,name,address,price):
        self.name = name
        self.address = address
        self.price = price

p1 = Office("spiceup",'koramangara',50000)


print(p1.name)
print(p1.address)
print(p1.price)

print('-'*50)

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+ self.name, "and I am", self.age)

p1 = Person("John",36)
p1.myfunc()

print('-'*50)
class Good:
    def __init__(self,dress,bad):
        self.name = name
        self.age = bad

    def myfunc(self):
        print("Hello my name is "+ self.name, "and I am",self.age)

lohit = Good("new dress", "wearing")
lohit.myfunc()
print('-'*50)

class Person1:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abcd):
        print("Hello my name is " + abcd.name, "and I am", abcd.age)

p1 = Person1("John",36)
p1.myfunc()

print('-'*50)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! my name is ", self.name,"and I am ", self.age, "years old.")

p1 = Person("John",36)

# p1.age = 40
# print("I am", p1.name)
# print("I am", p1.age)

p1.myfunc()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! my name is ",self.name, "and I am ",self.age, "years.")

p1 = Person("Jenny",35)
p1.myfunc()

print('-'*50)


class Planet:
    fun = 'happy'
    def __init__(self,name,age,game,system):
        self.name = name
        self.age = age
        self.game = game
        self.system = system

    def orbit(self):
        return f'{self.name} is {self.system}.'

lohit = Planet('lohit',23,'coubter strike','windows')

print(f'name is : {lohit.name}')
print(f'name is : {lohit.age}')
print(f'name is : {lohit.game}')
print(f'name is : {lohit.system}')
print(lohit.orbit())
print(f'name is {lohit.name} ,and age is {lohit.age}, and I like {lohit.game} , I usually use {lohit.system}')

class Employee:
    id = 10
    name = "ayush"
    def display(self):
        print("ID: %d \nName: %s" %(self.id,self.name))
emp = Employee()
emp.display()

class Employee:
    def __init__(self,first,last,sal,bonus):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.bon = bonus
        self.email = first + '.' + last + '@company.com'

emp1 = Employee('aayushi','johari',340000,500000)
emp2 = Employee('aai','johi',34000,50000)
print(emp1.email,"",emp2.email)
print(emp1.sal+emp2.sal)
print(emp1.bon+emp2.bon)

class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count+1
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
print("The number of students:",Student.count)

class Time:
    def __init__(self,hr,min):
        self.hr = hr
        self.min = min

    def myfunc(self):
        print(self.hr*60+self.min)    
 
    # def myfuc(x,y):  
    #     x = int(input('enter the hour'))
    #     y = int(input('enter the minute'))
# time1 = Time(int(input('enter the hour')),int(input('enter the minute')))
# time2 = Time(int(input('enter the hour'),int(input('enter the minute')))

time = Time(2,50)
time2 = Time(1,40)

time.myfunc()
time2.myfunc()

class Calculation1:
    def addition(self,a,b):
        return a+b
class Calculation2:
    def addition(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def addition(self,a,b):
        return a/b
d = Derived()
print(d.addition(10,20))


class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d, \nName : %s"%(self.id,self.name))
emp1 = Employee(19,"Joe")
emp2 = Employee(20,"yoshi")

emp1.display()
emp2.display()

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

class Student():
    def __init__(self,name,age,marks):
       self.name = name
       self.age = age
       self.marks = marks

    def display(self):
        return f'The student name is {self.name}, age is {self.age},his mark is {self.marks}'
    
student = Student('ryota',28,"A")
print(student.display())