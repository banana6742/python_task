numbers=[1,2,34,4,6]

double =[]

for number in numbers:
    double.append(number*2)
print(double)

print('-'*40)
double.append(number*2 for number in numbers)
print('this is the comparison way::',double)

print('-'*40)

numbers=[1,2,3,4,5,6,7,8,9]

square=[]

for number in numbers:
    if (number**2)%2==0:
        square.append(number**2)
print(square)
print('-'*40)

square = [number ** 2 for number in numbers if (number ** 2) % 2 == 0]
print("_",square)
print('-'*40)



numbers = [1,2,4,5,6,7,7]

square =[]

for number in numbers:
    if(number**2)%2==0:
        square.append(number**2)
print(square)

sqare = [number**2 for number in numbers if (number ** 2)%2 == 0]
print(square)


number = [13,45,21,4,5,1,3,5,63,2,23,4,5,6,7]

square = [number**2 for number in number if (number**2)%2==0]
print(square)


number = [1,2,3,4,5,6,6,7,8,9,10]

add = [num+1 for num in number if (num%2)==0]
print(add)
print('-'*40)

add = []

for num in number:
    if(num % 2)==0:
        add.append(num+1)
print(add)

print('-'*40)

numbers = [1,2,3,4,5,6,7,8,9,10]

div = [num for num in numbers if (num%2)==0]
print(div)

div = []

for num in numbers:
    if(num % 2)==0:
        div.append(num)
print(div)

print('-'*40)

#Filter program
#easy way to handle functions
grades = ['A','B','A','C','F','C','D']

def remove_F(grade):
    return grade!='F'

print(list(filter(remove_F,grades)))

#using for loop
filtered_grade=[]
for grade in grades:
    if grade !='A':
        filtered_grade.append(grade)
print(filtered_grade)

#using comprehesion
filtered_grade = [grade for grade in grades if grade != 'B']
print(filtered_grade)

# why use lambda functions?
# the power of lambda is better shown when you use them as an anonymous function inside another Function
# say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

x = lambda a:10+a
print(x(5))

print('-'*40)

x = lambda x,y:x**y
print(x(5,2))
print('-'*40)

x = lambda a:a + 10
print(x(19))
print('-'*40)

a=lambda x,y,z:x+y+z
print(a(10,20,30))
print('-'*40)


def myfunx(n):
    return lambda a:a*n

double=myfunx(2)
print(double(11))
print('-'*40)

def number(x):
    return lambda a:a*x

num1=number(2)
num3=number(3)

print(num1(2))
print(num3(2))
print('-'*40)
x = lambda a:a*2
print(x(2))

print('-'*40)
def num(x):
    return lambda a:a**x

num0 = num(2)
num2 = num(4)

print(num0(2))
print(num2(3))