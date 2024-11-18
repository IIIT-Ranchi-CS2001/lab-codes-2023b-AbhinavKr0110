n = int(input("Enter Number"))
sum = 0
while n > 0:
    d = n % 10
    n = int(n / 10)
    sum += d

print("Sum of digits = ",sum)