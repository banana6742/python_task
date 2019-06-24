# Iterator vs Iterable
# Lists,tuples,dictionaries,and sets are all iterable objects.they are iterable containers which you can get an iterator form.
# all these objects have a iter() method which is used to get an iterator

mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# string are also iterable objects,containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('-'*40)

# create an Iterator
# to create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object/
# as you have learned in the python classes/objects chapter, all classes have a function called __init__(), which allows you do some initializing when the object is being created/
# the __iter__() method acts similar, you can do operations(initializing etc.), but must always return the iterator object itself.
# the __next__() method also allows you to do operaions, and must return the next item in the sequence.
# create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

print('-'*40)
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('-'*40)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

    


year = int(input("Enter the year, check wether leap year or not :"))

if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print('{0} this is leap year'.format(year))

        else:
            print('{0} this is not leap year'.format(year))

    else:
        print('{0} this is leap year'.format(year))

else:
    print('{0} this is not leap year'.format(year))


# python program to display calendar of given month of the year
# import module
import calendar

# yy = 2014
# mm = 11

# to ask month and year from the user
yy = int(input("enter year: "))
mm = int(input("enter month: "))

# display the calender
print(calendar.month(yy,mm))

#1.calender(year,w,l,c):- this function displays the year, width of characters, no. of lines per week and column separations.
#2.firstweekdays() :- this function returns the first week day number. by default 0 (Monday).

# python code to demonstrate the working of calender() and firstweekday()
import calendar

# using calender to print calender of year
# prints calender of 2012 20002
print("The calender of year 2019 is: ")
print(calendar.calendar(2019,2,1,6))

# using firstweekday() to print starting day number 
print("the starting day number in calender is :", end="")
print(calendar.firstweekday())

print('-'*40)

# python code to demonstrate the working of isleap() and leapdays()

# importing calendar module for calendar operation
import calendar

# using isleap() to check if year is leap or not
if(calendar.isleap(2000)):
    print("The year is leap")
else:print("The year is not leap")

#using leapdays() to print leap days between years
print("The leap days between 1950 and 2000 are : ",end="")
print(calendar.leapdays(1950,2000))


#please upload all code in github and send me the link make notes
# practice all examples thinks  