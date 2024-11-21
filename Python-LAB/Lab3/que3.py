n = int(input("Enter Number"))
a = 0
b = 1

while n!=0:
    print(a,end =" ")
    temp = a+b
    a=b
    b=temp
    n=n-1