import sys
import math
a, b = map(int, input().split())
nums = b-a+1
if nums ==1:
    print(a)
    sys.exit()
elif nums ==2:
    print(a)
    print(b)
    sys.exit()
elif nums >2 and nums <5:
    x = 2
    y = 2
elif nums > 4 and nums < 7:
    x = 2
    y = 3
elif nums > 6 and nums < 10:
    x = 3
    y = 3
elif nums > 9 and nums < 13:
    x = 3
    y = 4
elif nums > 12 and nums < 17:
    x = 4
    y = 4
elif nums > 16 and nums < 21:
    x = 4
    y = 5
elif nums > 20 and nums < 26:
    x = 5
    y = 5
elif nums > 25 and nums < 31:
    x = 5
    y = 6
elif nums > 30 and nums < 37:
    x = 6
    y = 6
elif nums > 36 and nums < 43:
    x = 6
    y = 7
elif nums > 42 and nums < 50:
    x = 7
    y = 7
elif nums > 49 and nums < 57:
    x = 7
    y = 8
elif nums > 56 and nums < 65:
    x = 8
    y = 8
elif nums > 64 and nums < 73:
    x = 8
    y = 9
elif nums > 72 and nums < 82:
    x = 9
    y = 9
elif nums > 81 and nums < 91:
    x = 9
    y = 10
elif nums > 90 and nums < 101:
    x = 10
    y = 10
row = x
col = y
arr = [[0 for i in range(row)] for j in range(col)]
if col%2==0:
    colstart = int(col/2-1)
else:
    colstart = int(col/2)
if row%2==0:
    rowstart = int(row/2-1)
else:
    rowstart = int(row/2)


print(colstart, rowstart)
arr[colstart][rowstart]= a

counter = 0
incre = 1
incr = []
for i in range(1, nums+1):
    if i%2 == 0:
        incre+=1
        counter+=incre
        incr.append(incre)
    # print(counter, incre)
    if counter>=nums:
        break
dict = {"t": [-1, 0],"d": [1, 0],"l": [0, -1],"r": [0, 1] }
start = str(a)[:]
start = int(start)
while start<=counter:
    start +=1
    arr[colstart+1][rowstart] = start
for i in arr:
    print(i)


