x = int(input('enter the number :'))
if x % 2 ==0 :
      print("the number", x, "is even")
else:
      print("the number", x, "is odd")
       

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

def Fib(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
# print([Fib(n) for n in range(1,20)])
print(Fib(20))

intrst = input('Type the interest :%')
time = input('how many years are you going to save? :')
sav1 = int(input('how much do you save in the account? :'))

sav2= (int(sav1)*(1+int(intrst)/100)**int(time))

print("your saving in", time,  "years will be", sav2)

