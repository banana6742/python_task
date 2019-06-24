class Employee:
    pass

emp=Employee()
em2=Employee()
emp='lohit'
em2='susumu'

print(emp)
print(em2)


print('---------------')
class Person:
    pass

name=Person()
email=Person()
address=Person()
phone=Person()

name='New'
email='New@'
address='New-new'
phone='96246262'
print(name)
print(email)
print(address)
print(phone)

print('--------------')

class MyClass:
    x = 5
 
print(MyClass())

print('--------------')

class MyClass:
    x = 5
 
print(MyClass().x)

print('-------------------')

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

print('-------------------')

class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

p1 = Person("John",36,'lohit2013@gmail.com')

print(p1.name)
print(p1.age)
print(p1.email)

print('-------------------------')

class Office:
    def __init__(self,name, address, price):
        self.name = name
        self.address = address
        self.price = price

p1 = Office("spiceup",'koramangara',50000)

print(p1.name)
print(p1.address)
print(p1.price)


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is "+ self.name, "and I am" ,self.age)

p1 = Person("John",36)
p1.myfunc()

print('----------------')

class Good:
    def __init__(self,dress,bad):
        self.name = dress
        self.age = bad
    
    def myfunc(self):
        print("Hello my name is "+ self.name, "and I am",self.age)

lohit = Good("new dresss", "I'm wearing")
lohit.myfunc()

print('------------------')
class Person1:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name #(mysillyobject,name,age)右とinitが一致すること
        mysillyobject.age = age
        
    def myfunc(abcd):
        print("Hello my name is " + abcd.name, "and I am ",abcd.age)

p1 = Person1("John",36)
p1.myfunc()

# Modify Object all_properties()
# You can modify properties on objects like this:

class Person: # Person is Object
    #instantiating the programs instances which holds the characters
    #property that person will contain
    def __init__(self,name,age): #method, def si method,  
       # these self,name,age are property
        self.name = name
        self.age = age

#enable the new method
#hand
    def myfunc(self): #method
        print("Hello my name is " + self.name)

#tasks
p1 = Person("John",36) #p1 is instance

#I'm assigning the new value to the age
p1.age = 40

print("I am",p1.age)


#Delete Object Properties
#You can delete properties on objects by using the del keyword:
class Person2:

    #property that person will contain
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person2("John",32)

# del p1.age

print(p1.age)#due to deletion, no age will appear

# del p1

# print(p1)#due to deletion, no age will appear

class Planet:

    fun = 'happy'
    def __init__(self,name,age,game,system):
        self.name = name
        self.age = age
        self.game = game
        self.system = system
    
    def orbit(self):
        return f'{self.name} is ----------> {self.system}'

lohit= Planet('lohit',23,'counter strike', 'windows')

print(f'name is : {lohit.name}')
print(f'name is : {lohit.age}')
print(f'name is : {lohit.game}')
# print(f'name is : {lohit.system}')
print(lohit.orbit())

naboo = Planet('melon',34,'game of thrones','Mac OS')
print(f'name is : {naboo.name}')
print(f'name is : {naboo.age}')
print(f'name is : {naboo.game}')
# print(f'name is : {lohit.system}')
print(naboo.orbit())

takuma = Planet('takuma',24, 'Sony' ,'Android')
print(f'name is : {takuma.name}')
print(f'name is : {takuma.age}')
print(f'name is : {takuma.game}')
print(takuma.orbit())

endo = Planet("endo",21,'nintendo','Php')
print(f'name is : {endo.name}')
print(f'name is : {endo.age}')
print(f'name is : {endo.game}')
print(endo.orbit())
print('hellos guys and planets ',Planet.fun)



class Future:
    
    def __init__(self,name,age,game,system):
        self.name = name
        self.age = age
        self.game = game
        self.system = system

    def orbit(self):
        return f'{self.name} is -------> {self.system}'

lohit = Future("lohit",23,'game of throne','Asus')
print(f'name is : {lohit.name}')
print(f'name is : {lohit.age}')
print(f'name is : {lohit.game}')
print(lohit.orbit())

rekha = Future("rekha",22,'game of throne','lenovo')
print(f'name is : {rekha.name}')
print(f'name is : {rekha.age}')
print(f'name is : {rekha.game}')
print(rekha.orbit())


class Future:
    
    happy = 'happy'
    def __init__(self,name,age,game,system):
        self.name = name
        self.age = age
        self.game = game
        self.system = system

    def orbit(self):
        return f'{self,name} is ------->{self.system}'

padma = Future('padma',29,'wandara','Windows10')
print(f'name is : {padma.name}')
print(f'name is : {padma.age}')
print(f'name is : {padma.game}')
print(padma.orbit)

sumit = Future('sumit',24,'wandara','Windows10')
print(f'name is : {sumit.name}')
print(f'name is : {sumit.age}')
print(f'name is : {sumit.game}')
print(sumit.orbit)
print('happy happy happy! ', Future.happy)
    
#class with instance
class Employee:
    id = 10
    name = "ayush"
    def display(self):
        print("ID: %d \nName: %s" %(self.id,self.name))#just declaring class.
emp = Employee()
emp.display()

class Employee:
    def __init__(self,first,last,sal,bonus):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.bon = bonus
        self.email = first + '.' + last + '@company.com'

emp1 = Employee('aayushi','johari',350000,40000)
emp2 = Employee('test','rest',100000,30000)
print(emp1.email)
print(emp2.email)
print(emp1.sal)
print(emp2.sal)
print(emp1.bon)
print(emp2.bon)

class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count +1 
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
print("The number of students:",Student.count)

class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d \nName: %s"%(self.id,self.name))
emp1 = Employee("John",101)
emp2 = Employee("David",102)

emp1.display()
emp2.display()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print("ID :%d \n Name: %s"%(self.id,self.name))
emp1 = Employee("John",101)
emp2 = Employee("Naoya",102)

emp1.display()
emp2.display()

#constructor init function
class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d, \n Name : %s"%(self.id,self.name))
emp1 = Employee(19,"Joe")
emp2 = Employee(20,"yoshi")

emp1.display()
emp2.display()


#constructor parameterized
class Student:
    def __init__(self,name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
student = Student("John")
student.show()

#constructor non parameterized
class Student:
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)
student = Student()
student.show("John")

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

# myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yachety"

print(myobjectx.variable)
print(myobjecty.variable)


#we have a class defined for vehicles.create two new vehicles called car1 and car2
# set car1 to be a red convertible worth $60,000.00 with a name of fer, and car2 to be a blue van
# named Jump worth $10,000.00
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name,self.color,self.kind,self.value)
        return desc_str

car1 = Vehicle()

# print(car1.description())
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())

class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
#creats the object of the class Student
s = Student("John",101,22)

#prints the attribute name of the object s
print(getattr(s,'name'))

#reset the value of attribute age to 23
setattr(s,"age",23)

#prints the modified value of age
print(getattr(s,'age'))

#prints true if the student contains the attribute with name id
print(hasattr(s,'id'))

#deletes the attribute age 
delattr(s,'age')

#this will give an error since the attribute age has been deleted
#print(s.age)


class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:',getattr(person,"age"))
print('The age is:',person.age)


class planet:
    shape = 'round'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def orbit(self):
        return f'{self.name} age is {self.age}'

    @classmethod
    def commons(cls):
        return f'All the planets are {cls.shape}'

naboo =planet('naboo',400)

print(planet.shape)
print(naboo.orbit())
print(planet.commons())


print('-'*200)
class planet:

    shape = 'round'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def orbit(self):
        return f'{self.name} age is {self.age} '

    def lohitmethod(self):
        return f'{self.name}ith'

    @staticmethod
    def spin(speed='200 m/s speed'):
        return f'earth speed is {speed}'

naboo = planet('yahoo',23)
print(planet.spin())
print(naboo.orbit())
print(planet.spin('i can run more fast'))

print('-'*200)

class planet:
    shape = 'round'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def orbit(self):
        return f'{self.name} age is {self.age}'


    @classmethod
    def commons(cls):
        return f'All the planets are {cls.shape}'


naboo = planet('naboo',400)

print(planet.shape)
print(planet.commons())
print(naboo.orbit())

print('-'*50)
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()

print('-'*40)

class planet:
    shape = 'round'
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def orbit(self):
        return f'{self.name} age is {self.age}'
    @classmethod
    def commons(cls):
        return f'All the planet is {cls.shape}'

naboo = planet('naboo',400)
print(planet.shape)
print(naboo.orbit())
print(planet.commons())

#increment salary
class Employee:
    def __init__(self,pay,name,age):
        self.pay = pay
        self.name = name
        self.age = age

    def fullname(self):
        return '{} {}'.format(self.name,self.age)

    def salary_hike(self):
        self.pay=int(self.pay*2.0)

lohit = Employee(2,'lohit',21)
rekha = Employee(3,'lohit',23)

print(lohit.pay)
lohit.salary_hike()
print(lohit.pay)
lohit.fullname()

print('-'*50)

class Employee: 
    def __init__(self,name,age,pay):
        self.name = name
        self.age = age
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.name,self.age)

    def salary_hike(self):
        self.pay = int(self.pay*2.0)
 
lohit = Employee('lohit',21,3)
rekha = Employee('rekha',24,2)

print(lohit.pay,lohit.name,lohit.age)
lohit.salary_hike()
print(lohit.pay,lohit.name,lohit.age)

print('-'*50)

class Calculation1:
    def addition(self,a,b):
        return a+b
class Calculation2:
    def multiplication(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def division(self,a,b):
        return a/b
d = Derived()
print(d.addition(10,20))
print(d.multiplication(10,20))
print(d.division(10,20))

print('-'*50)

class Calculation1:
    def sum(self,x,y):
        return x+y

class Cal2:
    def mul(self,x,y): 
        return x*y

class Cal3(Calculation1,Cal2):
    def div(self,x,y):
        return x/y
    
d = Cal3()

print(d.sum(10,209))
print(d.mul(10,209))
print(d.div(10,209))

#overriding
class Animal:
    def speak(self):
        print("Speaking")
class Dog(Animal):
    def speak(self):
        print("Speaking")
d = Dog()
d.speak()

print('-'*50)

class Calculation1:
    def sum(self,x,y):
        return x+y
class Calculation2:
    def mul(self,x,y):
        return x*y
class Derived(Calculation1,Calculation2):
    def div(self,x,y):
        return x/y
d = Derived()
print(issubclass(Derived,Calculation1))
print(issubclass(Calculation1,Calculation2))

class Employee:
    increase=2
    def __init__(self,pay,name,age):
        self.pay = pay
        self.name = name
        self.age = age

    def fullname(self):
        return '{} {}'.format(self.name,self.age)

    def salary_hike(self):
        self.pay = int(self.pay * Employee.increase)

lohit=Employee(2,'lohit',21)
rekha=Employee(3,'rekha',23)

print(lohit.pay)
lohit.salary_hike()
print(lohit.pay)
print(lohit.__dict__)

lohit.increase=10

print(lohit.__dict__)

print(lohit.increase)
print(lohit.name)


class Animal:
    def dog(self):
        print('Dog is barking')

class Dog(Animal):
    def bark(self):
        print('dog stopped barking')

class Eat(Dog):
    def eat(self):
        print('dog is eating')

instance = Eat()

instance.eat()
instance.bark()
instance.dog()

print('-'*50)

class Animal:
    def speak(self):
        print("Animal speaking")

class Cat(Animal):
    def roar(self):
        print("cat roaring")

class Catson(Cat):
    def milk(self):
        print("cat's sons are drinking milk")

instance = Catson()
instance.speak()
instance.roar()
instance.milk()


class employee:
    add_emp=0
    increase=2
    def __init__(self,pay,name,age):
        self.pay = pay
        self.name= name
        self.age = age
        
        employee.add_emp+=1
    def fullname(self):
        return '{} {}'.format(self.name,self.age)

    def salary_hike(self):
        self.pay = int(self.pay*self.increase)


print(employee.add_emp)

lohit=employee(2,'lohit',21)
print(employee.add_emp)

rekha=employee(3,'rekha',23)
print(employee.add_emp)

lohit =employee(5,'lohit',43)

print(employee.add_emp)
print(lohit.name)
print(lohit.age)
print(lohit.pay)
print(rekha.pay)

