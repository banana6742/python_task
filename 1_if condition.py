age = int(input('enter the age'))
if age<10:
    print('you are kid' + ' and your age is ', age)

elif age>10 and age<20:
    print('he is teenager' , age)

else:
    print('youre adult', age)



food= input('do you eat meat? xyz :')

if food =='y':
    print('He is a non vegetarian')
    
else:
    print('veg man')


num = int(input('enter the number'))
if num > 0:
    print('the number is', num ,' and the number is positive')
elif num ==0:
    print('the number is', num ,' and the number is zero')
else:
   print('the number is', num ,' and the number is negative')

num = int(input("Enter a number: "))
if(num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))