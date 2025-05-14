angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
counter = 0

if angle1 == angle2:
    counter += 1
if angle1 == angle3:
    counter += 1
if angle2 == angle3:
    counter += 1
if not angle1 + angle2 + angle3 == 180:
    print("Error")
elif counter == 0:
    print("Scalene")
elif counter == 1:
    print("Isosceles")
elif counter == 3:
    print("Equilateral")
