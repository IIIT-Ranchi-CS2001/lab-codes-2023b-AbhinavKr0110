names=list(x for x in input("Enter the names: ").split())
roll=list(int(x) for x in input("Enter the roll no: ").split())
marks=list(int(x) for x in input("Enter the marks: ").split())

detail=list(zip(names,roll,marks))
print(detail)

print("sorted by marks: ",sorted(detail,key=lambda x: x[2]))