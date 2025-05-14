x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
list1 = [x1,x2,x3]
list2 = [y1,y2,y3]
for i in list1:
    if list1.count(i) == 1:
        print(str(i)+" ",end="")
for i in list2:
    if list2.count(i) == 1:
        print(i)
