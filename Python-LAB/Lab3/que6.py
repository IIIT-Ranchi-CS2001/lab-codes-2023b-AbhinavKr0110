word = input("Enter String ")
ch = input("Enter character ")
count = 0

for i in word:
    if ch == i:
        count += 1

print(F"Instances of {ch} = {count}")