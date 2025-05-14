c,r = map(int,input().split())
x,y = 0,0
while True:
    tempx,tempy = map(int,input().split())
    x+=tempx
    if x<0:
        x=0
    if x>c:
        x = c
    y+=tempy
    if y<0:
        y=0
    if y>r:
        y=r