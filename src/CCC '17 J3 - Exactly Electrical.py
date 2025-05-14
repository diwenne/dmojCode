a,b=map(int,input().split())
c,d = map(int,input().split())
e = int(input())
if e-(abs(b-d)+abs(a-c))>=0 and (e-(abs(b-d)+abs(a-c)))%2 ==0:
    print('Y')
else:
    print('N')