st1 = set([x for x in input("Enter Dancer:\n").split()])
st2 = set([x for x in input("Enter Singer:\n").split()])

print("All Artists: ", st1.union(st2))
print("AllRounders: ", st1.intersection(st2))
print("Dancer but not Singer: ", st1.difference(st2))
print("Singer but not Dancer: ", st2.difference(st1))
print("Singer but not Dancer cum Dancer but not Singer", st2.difference(st1).union(st1.difference(st2)))