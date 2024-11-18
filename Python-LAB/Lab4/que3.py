course = ["Python Programming", "COA", "Algorithms", "Maths", "Organizational Behaviour", "Theory of Computation"]
code = ["CS-2001", "CS-2003", "CS-2007", "M-2001", "HS-2001", "CS-2005"]
zp = zip(code, course)
lst = list(zp)
fin = []
for i in lst:
    fin.append(f"{i[0]} : {i[1]}")
print(fin)