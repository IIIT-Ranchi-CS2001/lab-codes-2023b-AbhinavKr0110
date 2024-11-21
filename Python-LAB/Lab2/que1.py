s1 ="Maha Bharat"
print(s1.swapcase())
print(s1[5:])
print(s1[5:]*3)
print(s1.replace("Maha","Mera"))
print(s1+" Mahan")

s = "Ba Ba Black Sheep"
print(len(s))
print(s.find("e"))
print(s.count('a'))
print(s.replace("Ba Ba "," Ta Ta "))

s2 = str(input("Enter the number : "))
print(s2==s2[::-1])

name = input("enter the name : ")
rollNumber = input("enter the roll no. : ")
Marks = int(input("enter the marks : "))
GradePoint = -1
remark=""
print("Name: ",name)
print("Roll Number: ",rollNumber)
print("marks: ",Marks)

if Marks>=90 :
    GradePoint = 10
    remark = "Outstanding"

elif Marks<90 and Marks>=80 :
    GradePoint = 9
    remark = "VERY GOOD"

elif Marks<80 and Marks>=70 :
    GradePoint = 8
    remark = "GOOD"

elif Marks<70 and Marks>=60 :
    GradePoint = 7
    remark = "AVERAGE"

elif Marks<60 and Marks>=50 :
    GradePoint = 6
    remark = "PASS"

else  :
    GradePoint = 0
    remark = "FAIL"

print("Grade Point: ",GradePoint)
print("Remark: ",remark)