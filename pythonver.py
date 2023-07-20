import math
import cmath


a, b, c = [float(s) for s in input('Enter what you would like x, y, and z to be: ').split()]
d = b*b-4*a*c
if a==0:
     print("Use another fucking number")
if d<0:
    x1 = (-b + cmath.sqrt(d))/2*a
    x2 = (-b - cmath.sqrt(d))/2*a
if d>=0:
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
if x1 == x2:
     print(x1)
if x1 != x2:
     print("1",x1)
     print("2",x2)


