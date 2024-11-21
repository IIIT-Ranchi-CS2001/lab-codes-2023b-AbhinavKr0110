s=input("enter the string:")
dict={}
for i in s:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
        
print(dict)