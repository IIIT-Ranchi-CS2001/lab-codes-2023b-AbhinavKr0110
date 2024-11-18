lst = [int(x) for x in input("Enter Number:\n").split()]
print(lst)
mean = sum(lst) / len(lst)
print(f"Mean = {mean}")
mode = 0
max = 0
for i in lst:
    if lst.count(i) > max:
        max = lst.count(i)
        mode = i
print(f"Mode = {mode}")
lst.sort()
if type(len(lst)/2) == float:
    median = (lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]) / 2
else:
    median = lst[int(len(lst)/2)]
print(f"Median = {median}")