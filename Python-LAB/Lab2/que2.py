import math
a = int(input("enter the no. a: "))
b = int(input("enter the no. b: "))
c = int(input("enter the no. c: "))

d  = b*b - 4*a*c

if d==0:
    r1=r2=-b/(2*a)
    print("root r1,r2 is: ",r1)
elif d>0:
    r1=(-b + math.sqrt(d))/2*a
    r2=(-b - math.sqrt(d))/2*a
    print("root r1 is :",r1)
    print("root r2 is :",r2)

else :
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(-d)/(2*a)
    print("Real_part root is: ",real_part)
    print("imaginary part is : ",imaginary_part)