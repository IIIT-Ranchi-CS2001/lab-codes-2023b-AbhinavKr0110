count = 0
word = ""
for i in (input("Enter String ") + " "):
    
    if i != " ":
        word+=i
        continue
    if word == "":
        continue
    for j in range(0, int((len(word)+1)/2)):
        if word[j] != word[-(j+1)]:
            break
    else:
        count+=1
    word = ""

print(F"Palindrome words = {count}")