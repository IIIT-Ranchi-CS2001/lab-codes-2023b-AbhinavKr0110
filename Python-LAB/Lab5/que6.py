dict={}
for i in range(5):
    s=input("enter the name:")
    n=int(input("enter the salary:"))
    dict[n]=s
l=list(dict.keys())
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            l[i],l[j]=l[j],l[i]
for i in range(0,len(l)):
    print(i+1,dict[l[i]],":",l[i])