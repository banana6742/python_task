boxs = ['lohit','rohit','mohit','ken']

for box in boxs:
    print('From this box', box)

boxes = ['lohit','rohit','mohit','lohit','endo','chihiro']

for box in boxes[1:4]:
    if box == 'lohit':
        print(f'{box}-say hello')

    else:
        print('just this', box)


fruits = ['cheery','orange','melon','watermelon','lemon']

for fruit in fruits:
    if fruit == 'melon' :
        print(f'happy you with {fruit} ')

    elif fruit == 'lemon' :
        print(f'happy you with {fruit} ')

    else:
        print('good',fruit)


for x in range(2,6):
    print('this is only the range', x)

for x in range(10,20,2):
    print('this is only the range', x)

for x in range(2,30,3):
    print('this will print',x)

for x in range(1,31,4):
    print('this is only the range each 4',x)

for x in range(7):
    print(x)
else:
    print("finally finished!")

for x in range(9,-1,-1):
    print(x)
else:
    print('test finished')

susumu = ["lohit","susumu","chihiro","kojun"]
php = ["python","programming","xyz","abc"]

for name in susumu:
    for brabra in php:
        print(name, brabra)

print('______________________________________')

adjs = ['dark', 'big','rotten']
nouns = ['fish', 'meat','vegetable','fruit']

for adj in adjs:
    for noun in nouns:
        print(adj, noun)

for i in range(3,16,3):
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")

print('______________________________________')

captains = ['Janeway','Picard','Sisko']

for i in range(len(captains)):
    print(captains[i])

for i in reversed(range(5)):
    print(i)

for i in reversed(range(len(captains))): 
    print(captains[i])


love= 21
hate= 0

while hate<love:
    if hate % 2 == 0:
        print(hate)
    hate+=1

count=0
while(count<3):
    count = count +1
    print("Hello Geek")

count =0
while(count<3):
    count = count + 1
    print("Hello Geek")
else:
    print("In those we can end the block else block") 

age= 20
num= 0

while num<age:
    if num==0:
        num+=1
        continue
        
    if num %2 ==0:
        print(num)

    if num>10:
        break
    
    num+=1

# program to add natural
# numbers upto
# sum = 1 + 2 + 3 +....+n
# to take input from the user.
# n= int(input("enter n:"))

    n = 10

# intinalize sum and counter
    sum =0
    i = 1

    while i <= n:
        sum = sum + i
        i = i +1    #update counter

    # print the sum
    print("The sum is", sum)

    xyz = 5
    while xyz>0:
        xyz-=1
        print(xyz)

    n = 5
    while n >0:
        n -=1
        if n == 2:
            continue
        print(n)
    print('loop ended.')

  
    n = 7 
    while n >0:
        n-=1
        print(n)
        if n % 4 ==0 :
            print('loop ended')
            break
        else:
            print('loop done.')


    n= 5
    while n > 0:
        n-=1
        print(n)
        if n == 2 :
            continue
        else:
            print('loop done.')
    

    n = 10

# intinalize sum and counter
    sum =0
    i = 1

    while i <= n:
        sum = sum + i
        i = i +1    #update counter

    # print the sum
    print("The sum is", sum)

    n = 10

    mul = 1
    i = 1

    while i <= n:
        mul = 2 *i
        i = i + 1

        print(mul)

    # n = 2
    # while 1:
    #     i = 1;
    #     while i <= 10:
    #         print("%d x %d = %d\n"%(n,i,n*i));
    #         i = i + 1;
    #     choice = int(input("Do you want to continue printing the table, press 0 for no?"))
    #     if choice == 0:
    #         break;
    #     n = n + 1

        # i = 0;
        # while i!=10:
        #     print("%d"%i);
        #     continue;
        #     i=i+1
            