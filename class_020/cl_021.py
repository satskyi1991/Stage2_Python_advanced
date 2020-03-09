#Program for calculating roots of square equation
import math

a = input("Enter a:")
a = float(a)
b = input("Enter b:")
b = float(b)
c = input("Enter c:")
c = float(c)
x1=x2=D=None
if a==0:
    print("It is not a square equation");
else:
    D = b*b - 4*a*c
    if D == 0:
        x1 = x2 = -b/ 2*a
    elif D>0:
        x1 = (-b + math.sqrt(D))/ 2*a
        x2 = (-b - math.sqrt(D))/ 2*a
    else:
        print("Equation have no roots");
print(x1, x2, D)
