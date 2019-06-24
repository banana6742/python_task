# boxs = ['lohit','rohit','mohit','ken']

# for box in boxs:
#     print('From this box', box)

# boxes = ['lohit','rohit','mohit','lohit','endo','chihiro']

# for box in boxes[1:4]:
#     if box == 'lohit':
#         print(f'{box}-say hello')

#     else:
#         print('just this',box)

# fruits = ['cherry','orange','melon','watermelon','lemon']

# for fruit in fruits:
#     if fruit == 'melon':
#         print(f'happy you with {fruit}')   
#     elif fruit == 'lemon':
#         print(f'happy you with {fruit}')
#     else:
#         print('good',fruit)

# for x in range(2,6):
#     print('this is only the range', x)

# for x in range(10,20,2):
#     print('this is only the range', x)
        
# for x in range(2,30,3):
#     print('this will print',x)

# for x in range(7):
#     print(x)
# else:
#     print("finally finished!")

# for x in range(9,-1,-1):
#     print(x)
# else:
#     print('test finished')

# susumu = ["lohit","susumu","chihiro","kojun"]
# php = ["python","programming","xyz","abc"]

# for name in susumu:
#     for brabra in php:
#         print(name, brabra)

# adjs = ['dark','big','rotten']
# nouns = ['fish','meat','vetetable','fruit']

# for adj in adjs:
#     for noun in nouns:
#         print(adj,noun)

# for i in range(3,16,3):
#     quotient = i /3
#     print(f"{i} divided by 3 is {int(quotient)}." )

# captains = ['Janeway','Picard','Sisko']

# for i in range(len(captains)):
#     print(captains[i])

# for i in reversed(range(5)):
#     print(i)

# for i in reversed(range(len(captains))):
#     print(captains[i])

# love = 21
# hate = 0

# while hate<love:
#     if hate % 2 ==0:
#         print(hate)
#     hate +=1

# count = 0
# while(count <3):
#     count = count + 1
#     print("hello Geek")
# else:
#     print("In those we can end the block else block")

# age = 20
# num = 0

# while num<age:
#     if num==0:
#         num+=1
#         continue

#     if num %2 ==0:
#         print(num)

#     if num>10:
#         break

#     num+=1

#     n = 10

#     sum =0
#     i = 1

#     while i <= n:
#         sum = sum + i
#         i = i + 1

#         print(sum)

#     n = 5

#     mul = 1
#     i = 1
#     while i <= n:
#         mul = mul * i
#         i = i + 1
#         print(mul)

#     xyz = 5
#     while xyz > 0:
#         xyz -= 1
#         print(xyz)

#     a = 10
#     while a > 0:
#         a = a - 1
#         print(a)
    
#     n = 6 
#     while n > 0:
#         n -=1
#         if n ==2:
#             continue
#         print(n)
#     print('loop ended')  

#     n = 7
#     while n > 0:
#         n -= 1
#         print(n)
#         if n % 4 ==0:
#             print('loop ended')
#             break
#         else:
#             print('looping')

#     def greet(name, time):
#         print(f'hello{name} what are you doing at this {time} time')
#         print('hello' ,name ,'what are you doing at this', time ,'time')
#     greet('lohit','morning')
        
# def greet(name, time):
#    print(f'good morning{name},hope your greet at this {time}')

# x = input('enter your name :')
# y = input('enter the  time :')

# greet(x,y)

def greet(name = "ryu", time = "morning"):
    print(f'Good morning {name},what are you doing in the {time}')

greet("lohit","noon")
greet("rk","afternoon")
greet()

def myFun(x,y = 50):
    print("x: ",x)
    print("y: ",y)


myFun(1,5)
myFun(30,39)

def radius(x = 4):
    print("radius: ",x)
    area = 3.14*x**2
    print("Area of circle:",area)
radius(5)

