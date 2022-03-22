import math
number = int(input("enter a number:"))
x =int(number)
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return x
x1 = int(math.sqrt(x))
if (x1*x1)<x:
    x1=x1+1
c=0
while c==0:
    d=x1*x1
    d1=d-x
    d2=int(math.sqrt(d1))
    if (isPerfectSquare(d1)):
        c=c+1
        p1=x1-d2
        p2=x1+d2
        print("factors of",x,"are",p1,"and",p2)
    x1=x1+1
