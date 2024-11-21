dict={}
for i in range(5):
    s=input("enter name: ")
    m=int(input("enter marks: "))
    dict[s]=m

h=[]
a=[]
l=[]
ans="";p=0

for i in dict:
    if dict[i]>=85:
        h.append(i)
        if dict[i]>p:
            ans=i
            p=dict[i]
    elif dict[i]<60:
        l.append(i)
    else:
        a.append(i)
print("high performers: ",len(h))
print(h)
print("avgerage performers: ",len(a))
print(a)
print("low performers: ",len(l))
print(l)
print("highest marks: ",ans)