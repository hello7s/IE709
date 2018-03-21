#Python supports two types of numbers: integers and floating point numbers.

myint = 100
print(myint)

#Either of the following notations work for floating point numbers
myfloat = 100.0
print(myfloat)

myfloat = float(100)
print(myfloat)

#Strings use either single or double quotes
mystring = 'Hola'

yourstring = "Adios"

print(mystring,yourstring)

one = 1
two = 2
three = one + two

print(one, two, three)

watch = "Watch the space"
space = " "
between = "between the words"
print(watch,space,between)
print(watch,between)
print(watch + between)
print (watch + " " + between)

#Variable assignments can be done with multiple variables
x, y = 100,200
print(x,y)
print (x+y)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)