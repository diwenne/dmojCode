n = int(input())
heights = list(map(int,input().split()))
bases = list(map(int,input().split()))
counter = 0
for i in range(n):
    h1 = heights[i]
    h2 = heights[i+1]
    b = bases[i]
    area = b*(h1+h2)
    counter += area
print(counter/2)
