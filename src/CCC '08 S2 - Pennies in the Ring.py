import math

def integer_points_circle_efficient(r):
    count = 0
    for x in range(r + 1):
        y_max = math.floor(math.sqrt(r ** 2 - x ** 2))
        count += (y_max + 1)  # Count all integer y-values
    return 4 * count - 4 * r - 3  # Adjust for overlapping axes points

while True:
    radius = int(input())
    if radius ==0:
        break

    print(integer_points_circle_efficient(radius))






