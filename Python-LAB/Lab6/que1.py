import math

def cosine(n,x):
    if n==1:
        return 1
    elif n%2==0:
        return -1*(x**(2*(n-1))/math.factorial(2*(n-1))) + cosine(n-1,x)
    else :
        return (x**(2*(n-1))/math.factorial(2*(n-1))) + cosine(n-1,x)

n = int(input("Enter the no . "))
x= int(input("Enter the value of x ."))
print(cosine(n,x))