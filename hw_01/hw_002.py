# import the math module
import math


a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")
a = int(a)
b = int(b)
c = int(c)
print(type(a))
print(type(b))
print(type(c))
p = 0.5*(a+b+c)
S = math.sqrt(p*(p - a)*(p - b)*(p - c))
print(type(p))
print(type(S))
print( p )
print( S )