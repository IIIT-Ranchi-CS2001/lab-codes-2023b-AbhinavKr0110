names=list(x for x in input("Enter the names: ").split())
roll=list(int(x) for x in input("Enter the roll no: ").split())
marks=list(int(x) for x in input("Enter the marks: ").split())

details = []

for i in range(0,len(names)):
    p = (roll[i],names[i],marks[i])
    details.append(p)
print(details)
details.sort(key = lambda x: x[2])
print("sorterd by marks  :",details)