# this file contains all about numbers is python 
x=2
y=3
z=4
print(x+y)
print(x-y+z)
print(x+(y*z))
print((x+y)*z) # we use paranthesis for more readability of the code and we also use paranthesis if we want to do some specific operation do first.
print(x+2.23)
a=int(2.23) # if we need in integer only not in decimal
print(x+a)
name='amrit'+'rajput'
print (name)
print(x+1,y+2)
print(y%2)
print(x**2) # ('**') for power
print(2**1000) # python can easily handle large operation also
result=1/3.0
print(result)


#In Python, the str() and repr() functions are used to obtain string representations of objects. While they may seem similar at first glance, there are some differences in how they behave. Both of the functions can be helpful in debugging or printing useful information about the object.


#COMPARISON
print(1<2)
print(x is 2)
print(5.0 == 5)
print(4.0!=5)
print(x<y<z)
print(x>y>z)
print(x<y and y<z) #both true then only true
print(x<y or y>x) #if 1 true o/p is true
print(x<y and y>z)
print(1==2<3) # means 1==2 and 2<3

# LIBRARY ('MATH')

import math
print(math.floor(3.5)) # for getting floor of any no.
print(math.floor(-3.5))

print(math.ceil(3.5))
print(math.ceil(-3.5))

print(math.trunc(-3.5)) # towards 0
print(math.trunc(3.5)) # o/p = 3
 
# we can also calculate complex no.
num1=(2+9j)
num2=7
print(num1*num2)
print(num1*6)

# operation on octal , hexadecimal , binary
num3=0o20 #for octal we write '0o' before no.
print(num3)

num4=0x60 #for hexadecimal use '0x'
print(num4)

num5=0b0101 #for binary use '0b'
print(num5)

# CONVERSION OF ANY NO. T OCTAL , HEXADECIMAL , BINARY these are methods so we use () 
print(oct(64))
print(hex(64))
print(bin(64))

print(int('64',8)) # this is better practice for conversion use n0. in form of string then comma the conversion's base
print(int('100',2)) 


#ANOTHER LIBRARY 'RANDOM'


import random


print(random.random())
print(random.randint(1,9)) #if we need rndm no.b/w 2 no.
l1=['amrit','amrit raj','amrit rajput'] # we need rndm arr element
print(random.choice(l1)) #choice because we want from l1
print(random.shuffle(l1)) #for shuffling
print(l1)


# SETS

setone={1,2,3,4}
print(setone & {1,3}) # in set '&' is used for finding common part
print(setone | {1,3,7}) # '|' is used for finding all unique no.
print(setone-{1,2,3,4}) # if we set is empty then it return 'set()'
 # NOTE:-IF WE WANT TO DENOTE EMPTY SET THEN WE USE '()' BUT IF WE NEED TO DECLARE THEN WE USE'{}'


 # BOOLEAN


print(True==1)
print(False==0)

print(True is 1) # obj differnt but val almost same
print(True+4) # means 1+4=5