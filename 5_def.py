
# def greet(name,time):
#     print(f'Hello {name} what are you doing at this {time} time')
#     print('Hello',name,'what are you doing at this', time ,'time' )

# greet('lohit','morning')


# def greet(name, time):
#     print(f'good morning{name},hope your greate at this {time}')

# x = input('enter your name :')
# y = input('enter the time :')

# greet(x,y)


def greet(name ="ryu", time ="morning"):
    print(f'Good morning {name}, what are you doing in the {time}')

greet("loht","noon")
greet("rk","afternoon")
greet()
    
def myFun(x,y=50):
    print("x: ",x)
    print("y: ",y)

myFun(1,5)
myFun(30,39)

def radius(x = 4):
    print("radius: ",x)
    area = 3.14 * x**2

    print("Area of circle :" ,area)
radius(5)
        
# def area(radius):
#     print(3.14*radius*radius)
# area(4)

# pass by reference 
# here x is a new reference to same list
def myFun(x):
    x[0] = 20

# driver code(note that list is modified)
# after function call
lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)

def myFun2(x):
    # after below line link  of x with previous
    # object gets broken A new object is assignedto x

    x = [20,30,40]


lst = [10,11,12,13,14,15]
myFun2(lst)
print(lst)

def myFun(x):
    x = 20

    # after below line link of x with previous
    # object gets broken A new object is assigned to x

# driver code(note that lst is not modified)
# after function call
x= 10
myFun(x)
print(x)


# variable length arguments:
# we can have both normal and keyword variable number of arguments please see this for details

# python program to illustrate
# *args for variable number of arguments

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello','welcome','to','spiceup')


# def swap(x,y):ミス
#     x = 2
#     y = 3

#     temp = x
#     x = y
#     y = temp

# swap(x,y)
# print(x)
# print(y)

# print('_______________caluculation of volume_______________')
    
# def area(radius):
#     return 3.14 * radius * radius

# def volume(area,length):
#     print(area * length)

# radius = int(input('enter the value for the radius'))
# length = int(input('enter the value for the height'))

# volume(area(radius),length)


# #defining the function
# def change_string(str):
#     str = str + " how are you";
#     print("printing the string inside furenction :",str)

# string1 = "Hi I'm lohit"

# #calling the function
# change_string(string1)

# print("printing the string outside function :",string1)

# #defining the function
# def change_list(list1):
#     list1.append(20)
#     list1.append(30)
#     print("list inside function = ",list1)

# #defining the list
# list1 = [10,30,40,50]


# #calling the function
# change_list(list1)
# print("list outside function = ",list1)

# #immutable function


# #the argument name is the required argument to the funtcion func
# def func(name):
#     message = "HI " + name
#     return message
# name = input("Enter the name :")
# print(func(name))


# for i in [1,2,3,4,5]:
#         if i == 3:
#                 pass 
#                 print("Pass when value is", i)
#         print(i)
        
# list = [1,2,3,4,5]
# flag = 0
# for i in list:
#         print("Current element:", i , end=" ");
#         if i == 3:
#                 pass
#                 print("\nWe are inside pass block\n")
#                 flag = 1
#         if flag ==1:
#                 print("\nCame out of pass\n")
#                 flag = 0
                

# def printme(name, age=22):
#         print("My name is",name,"and age is",age)
# printme(name= "john")
# printme(age =10, name="David")

# def func(name,message):
#         print("printing the message with",name, "and", message)
# func(name ="John",message="hello")


# def printme(*names):
#         print("type of passed argument is ", type(names))
#         print("printing the passed arguments...")
#         for name in names:
#                 print(name)
# printme("john","David","smith","nick")

# def func(name):
#         print("Hi ",name)

# func("Ayush")

# def sum(a,b):
#         return a+b

# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

# print("Sum = ",sum(a,b))

# name = 'lohit'

# def lohit_lohit():
#         global name
#         name = "lohit badiger"
#         print('the name is ', name)

# lohit_lohit()
# print('global name is', name)
# print('global name is', name)

# print('______________________________')

# number = 20

# def numnum():
#         global number
      
#         print('the number is ', number)

# numnum()
# print('global name is',number)

# def lohit(dictionary):
#         for key, val in dictionary.items():

#                 print(f'I know this a {key} programing and this is {val}, a framework of {key}')

# lohit_items = {}

# while True:
#         lohit_program = input ('enter name of programming:')
#         lohit_frame = input('enter the name of frame work:')
#         lohit_items[lohit_program]=[lohit_frame]

#         another=input('add another program?(y/n)')
#         if another =='y':
#                 continue
#         else:
#                 break

# lohit(lohit_items)

# def supermarket(fruit):
#         for variety, price in fruit.items():
#                 print(f'This product is {variety} and price is {price}')

# supermarket_items = {}

# while True:
#         supermarket_variety = input('enter the name of fruit :')
#         supermarket_price = input('enter the price of that fruit :')
#         supermarket_items[supermarket_variety]=[supermarket_price]

#         another= input('add another fruit? (y/n)')
#         if another == 'y':
#                 continue
#         else:
#                 break
# supermarket(supermarket_items)


def person(dictionary):
        belts = list(dictionary.values())
        for belt in belts:
                num = belts.count(belt)
                print(f'there are {num} {belt} belts')

lohit_items = {}

while True:
        lohit_program = input('enter name of belt : ')
        lohit_frame = input('enter the name of belt color : ')
        lohit_items[lohit_program] = [lohit_frame]

        another = input('add another program? (y/n)')
        if another == 'y':
                continue
        else:
                break

person(lohit_items)

print('---------------------')

def f_r(x):
        return x+3

def f_p(x):
        print(x+3)

f_r(2)
f_p(2)

xyz=f_r(2)
xzy=f_p(2)
print(xyz,xzy)

print(f_r(3)*2)