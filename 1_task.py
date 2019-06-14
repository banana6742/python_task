# Answer of 1&3
def customer(name = "ryu", address = "vancuver" ,phone = "953591061", email = "gaoi@gmail.com"):
    print(f'name:{name},address:{address},contact:{phone},{email}')

customer("lohit","bengaluru","851061542","lohilohi@gmail.com")
customer("padma","chennai","85137085","padpad@gmail.com")
customer("sumit","kolkata","853137085","sumisumi@gmail.com")
customer("rekha","bengaluru","855137085","rekhhhhhhhha!@gmail.com")
customer()






#2 I gave up I dont know the answer

# def customer(customer):
#     for name,address in customer.id():
#         print(f'name:{name},address:{address}')
#         # ,contact:{phone}')
    
# customer_id = {}

# while True:
#     customer_name = input('enter customer\'s name :')
#     customer_address = input('enter customer\'s address :')
#     # customer_phone = input('enter customer\'s phone :')
#     # customer_email = input('enter customer\'s email :')
#     customer_id[customer_name]=[customer_address]
#     # =[customer_phone]=[customer_email]

#     another = input('add another customer? (y/n) :')
#     if another == 'y':
#         continue
#     else:
#         break

# customer(customer_id)


# def user(user):
#         for name, address in user.items():
#                 print(f'Username is {name} and address is {address} ')

# user_items = {}

# while True:
#         user_name = input('enter the username :')
#         user_address = input('enter the address of that user :')
#         # user_phonenumber = input('enter the phonenumber of that user :')
#         user_items[user_name]=[user_address]

#         another= input('add another fruit? (y/n)')
#         if another == 'y':
#                 continue
#         else:
#                 break
# user(user_items)

# i gave up the problem

print('---------------------------')


#4

def Fib(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
# print([Fib(n) for n in range(1,20)])
print(Fib(20))

# def Fib(n):
#     a,b = 0,1
#     if n == 1:
#         return a
#     elif n == 2:
#         return b
#     else:
#         for i in range(n-2):
#             a, b = b, a + b
#         return b

# print([Fib(n) for n in range(1,21)])
print('---------------------------')


#5
def evenodd(x):
    return x % 2

x = int(input('enter the number :'))

if x % 2 ==0 :
      print("the number",x , "is even")
else:
      print("the number",x , "is odd")


print('---------------------------')

#6
def output(number):
    return print(number)

number = int(input('enter the number'))
for number in range(number,-1,-1):
    print('countdown',number)
# else:
#     print("finally finished!")



print('---------------------------')
#8
intrst = input('Type the interest :%')
time = input('how many years are you going to save? :')
sav1 = int(input('how much do you save in the account? :'))

sav2= (int(sav1)*(1+int(intrst)/100)**int(time))

print("your saving in", time,  "years will be", sav2)



print('---------------------------')

def sav(intrst,time,sav1):
    return int(sav1)*(1+int(intrst)/100)**int(time)
    print('your saving will be',int(sav1)*(1+int(intrst)/100)**int(time))

intrst = float(input('Type the interest :%'))
time = float(input('how many years are you going to save? :'))
sav1 = int(input('how much do you save in the account? :'))

print("your saving in", time,  "years will be", sav(intrst,time,sav1))

   
#9~11
def area(circle):
    return 3.14*radius**2

radius = int(input('enter the radius: '))

print('The area of cirlce is',3.14*radius*radius)

print('--------------------------------')

def area(triangle):
    return height * base / 2

height = int(input('enter the height: '))
base   = int(input('enter the base: '))

print('The area of triangle is', height * base / 2)


print('--------------------------------')

def area(parallelogram):
    return height * broadth

height = int(input('enter the height: '))
broadth = int(input('enter the broadth: '))

print('The area of parallelogram is', height * broadth)


print('--------------------------------')


def get_area(base,height):
    return 0.5 *base*height

print('The area is',get_area(10,20))


print('--------------------------------')


def paral_area(broadth,height):
    return broadth*height

broadth = int(input('enter the value for the broadth :'))
height = int(input('enter the value for the height :'))

print('The area of parallelogram is',paral_area(broadth,height))


print('--------------------------------')

def area(radius):
    return 3.14 * radius * radius

radius = int(input('enter the value for the radius :'))
print('The area of circle is', area(radius))


print('--------------------------------')

def area(height,base):
    return 0.5*height*base

height = int(input('Enter the height of triangle :'))
base = int(input('Enter the base of triangle :'))

print('The area of triangle is', area(height,base))

print('--------------------------------')


def area(radius):
    return 3.14*radius**2

def volume(area,length):
    print(area * length)

radius = int(input('enter the value for the radius :'))
length = int(input('enter the value for the height :'))

volume(area(radius),length)


#12
number = int(input('enter any number you like :'))

def numnum():
        global number
      
        print('the number is ', number)

numnum()






