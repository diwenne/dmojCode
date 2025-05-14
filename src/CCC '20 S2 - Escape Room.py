from collections import deque
r = int(input())
c = int(input())
# arr = []
# for i in range(r):
#     arr.append(list(map(int,input().split())))
# print(arr)
dick = {}

for i in range(1,r+1):
    row = list(map(int, input().split()))
    for j in range(1,len(row)+1):
        x = row[j-1]
        dick.setdefault(x,[]).append((i,j))

# print(dick)

def bfs(x,y):
    queue = deque([(r, c)])
    vis = set()
    while queue:
        # print(queue)
        x,y = queue.popleft()
        if (x,y) not in vis:
            vis.add((x,y))
            a = x*y
            if (x,y) == (1,1):
                return True
            else:
                if a in dick:
                    for i in dick[a]:
                        queue.append((i[0],i[1]))



if bfs(r-1,c-1):
    print("yes")
else:
    print("no")



