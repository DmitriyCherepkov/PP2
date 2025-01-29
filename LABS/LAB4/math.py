import math

#1 Write a Python program to convert degree to radian.
# print("{:.6f}".format(math.radians(int(input()))))

#2 Write a Python program to calculate the area of a trapezoid.
#h, b1, b2 = float(input("Type height: ")), float(input("Type base 1: ")), float(input("Type base 2: "))
#print("\nThe area of the trapezoid is: " + str((b1+b2)/2*h))

#3 Write a Python program to calculate the area of regular polygon.
n, a = int(input("\nInput number of sides: ")), float(input("Input the length of a side: "))
tg = 1 if 90-180/n == 45 else math.tan(math.radians(90-180/n)) 
print("\nThe area of the polygon is: " + str(int(n*a*a/(tg*4))))

# 4 Write a Python program to calculate the area of a parallelogram.
#h, b = float(input("Type height: ")), float(input("Type base: "))
#print("\nThe area of the parallelogram is: " + str(b*h))