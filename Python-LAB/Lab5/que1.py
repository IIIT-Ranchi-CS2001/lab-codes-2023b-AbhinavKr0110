import math
point1=tuple((int(x) for x in input("Enter the Points 1 ").split()))
point2=tuple((int(x) for x in input("Enter the Points 2 ").split()))
distance = math.sqrt((point2[0] - point1[0])**2 + 
                     (point2[1] - point1[1])**2 + 
                     (point2[2] - point1[2])**2)

print(f"Distance between the points {point1} & {point2} is {distance}")