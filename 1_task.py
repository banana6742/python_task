x1 = 5
x2 = 5
y1 = 'Hello'
y2 = 'Hello'
y3 = [1,2,3]
y4 = [1,2,3]

if (x1 == x2):
    print('x1 is equal to x2')
else:
    print(x1 ,'is not equal to',x2)

print(x1 is x2)
print(x1 is not x2)

print(y1 is y2)

if (y3 == y4):
    print(y3 ,'is equal to',y4)
else:
    print(y3 ,'is not equal to',y4)

x = True
y = False

print('x and y is', x and y)

print('x or y is',x or y)

print('not x is', not x)

for val in "string":
    if val == "i":
        break
    print(val)


for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


