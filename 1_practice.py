print('he\'s a mad man')

greet = 'hello world'
print(greet[0])

print(greet)

print(greet[1:-3])
greet = greet[0:3]
print(greet)

add = "hello"
person = "lohit"

print(add+person)
print(add+' '+person)

amount =20
new = 23
total=amount + new
print(total)

# name = input('tell me your name :')
# age = input ('and your age is :')
# print("hello there " + name , "and your age is ", age, 'this')

radius = input('enter the radius of circle(m):')
print(radius)
area=3.142 * int(radius)**2
print('the area of circle is', area)

num1 = 3.1212
num2 = 2.23232222
lo= 10.83328238
loh = 29.28928

print('this is the first num1 {0} this is num2 is {1} this is loht {2:.5}, last number,{3:.3f}'.format(num1,num2,lo,loh))

print(f'this is the first num1 {num1} and this is a value of num2 {num2} and this is lo {lo} and this is loh {loh}')

print(f'this is the first num1 {num1:.2} and this is a value of num2 {num2:.3} and this is lo {lo:.4} and this is loh {loh:.2f}')

b = input('input the broadth of triangle :')
h = input('input the height of triangle :')
print("broadth is: ",b )
print("height is: ",h )
Area = (int(b)*int(h))/2
print('the area of triangle is ',Area)


Height = int(input('Enter Height :'))
Base = int(input('Enter Base :'))

print(Height)
print(Base)

area = 0.5*int(Height*Base)
print('area of the triangle is ', area)