# age = int(input('enter the age'))
# if age<10:
#     print('you are kid' + ' and your age is ', age)
# elif age == 10:
#     print('you are kid' + ' and your age is ', age)

# elif age>10 and age <20:
#     print('youre teenager', age)

# else:
#     print('youre adult', age)

# food = input('do you eat meat? xyz :')

# if food =='y':
#     print('He is a non vegetarian') 
# elif food =='z':
#     print('He is a non vegetarian') 
# elif food =='a':
#     print('He is a non vegetarian')   
# elif food =='b':
#     print('He is a non vegetarian')       
# else:
#     print('veg man')

# num = int(input('enter the number'))
# if num > 0:
#     print('the number is', num,'and the number is positive')
# elif num ==0:
#     print('the number is', num, 'and the number is zero')
# else:
#     print('the number is', num, 'and the number is negative')

# num = int(input("Enter a number: "))
# if(num % 2) ==0:
#     print("{0} is Even".format(num))
# else:
#     print("{0} is Odd".format(num))


# A = [1,2,3,4,3,4,'rekha!']

# print(A)
# print(A[0])
# print(A[1])
# print(A[2])
# print(A[3])
# print(A[4])
# print(A[5])
# print(A[6])
# A[2]='im changing the 2nd value in the list'

# print(A)
# print(A[2])

# print('rekha!' not in A)

# list = ['abcd', 786, 2.23, 'john', 70.2]
# tinylist = [123,'john']
# print(list)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(tinylist*2)
# print(list + tinylist)

# print('---------------------------------')
# empty_tuple = ()
# print(empty_tuple)

# tup = 'python','geeks'
# print(tup)

# list=(1,2,3,4)
# print(list)
# print(list[0])
# print(list[2])

# tuple1 = (0,1,2,3)
# tuple2 = ('python','geek')

# print(tuple1 + tuple2)

tuple1 = (0,1,2,3)
tuple2 = ('python','geek')
tuple3 = (tuple1, tuple2)
print(tuple3)

tup = ('python','php')
print(len(tup))

A = {'Age':25,'Name':'rekha'}
print(A)
print(A['Age'])
print(A['Name'])

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = {1:'Geeks', 2:'For',3:'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = dict({1: 'Geeks',2 :'For',3:'Geeks'})
print("Dictionary with the use of Integer Keys: ")
print(Dict)

Dict = dict([(1,'Geeks'),(2,'For')])
print(Dict)

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict)

Dict['Value_set']=2,3,4
print(Dict)

Dict[2] ='welcome'
Dict[5] = {'Nested' : {'1':'Life','2':'Geeks'}}
print(Dict)

Dict = {1:'Geeks', 'name':'For',3:'Geeks'}

print(Dict[1])
print(Dict.get(3))
print(Dict.get('name'))

a = {1,2,3,4,5,6,6,7,7,8}
print(a)

normal_set = set(["a","b","c"])
print("normal_set",normal_set)

normal_set.add("d")
print("normal_set",normal_set)