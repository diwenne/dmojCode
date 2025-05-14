from collections import deque
directions = [(1,0), (-1, 0), (0, 1),(0, -1)]
r, c = map(int,input().split())
arr = []
empty = {}
for i in range(r):
    arr.append(input())
for i in range(1,r-1):
    for j in range(1,c-1):
        a = arr[i][j]
        if a == ".":
            empty[(i,j)] = -1
        if a == "S":
            start = (i,j)
def bfs(x,y):
    visited = set()
    boo = True
    queue = deque([(x,y,0)])
    while queue:
        x,y,length = queue.popleft()
        if boo == True:
            if (x,y) in cams:
                boo = False
                continue
        if (x,y) not in visited:
            visited.add((x,y))
            if arr[x][y] == "." and (x,y) not in cams:
                empty[(x,y)]=length
            node = arr[x][y]
            lis = {"R","L","U","D"}
            if node in lis:
                if node == "R":
                    direction = directions[2]
                elif node == "L":
                    direction = directions[3]
                elif node == "U":
                    direction = directions[1]
                elif node == "D":
                    direction = directions[0]
                newX = x+direction[0]
                newY = y+direction[1]
                if 0<= newX < r and 0<= newY < c:
                    if arr[newX][newY] != "W" and (newX,newY) not in cams:
                        queue.insert(0,(newX,newY,length))
            else:
                for i in directions:
                    newX = x+i[0]
                    newY = y+i[1]
                    if 0<= newX < r and 0<= newY < c:
                        if arr[newX][newY] != "W" and (newX,newY) not in cams:
                            if (newX, newY) not in visited and (x,y) not in cams:
                                queue.append((newX,newY,length+1))
                                boo = False
                        elif (newX,newY) in cams:
                            if arr[newX][newY] in lis:
                                queue.append((newX, newY, length + 1))
                                boo = False

cams = set()
for i in range(1,r-1):
    for j in range(1,c-1):
        n = arr[i][j]
        if n == "C":
            cams.add((i,j))
            for h in directions:
                queue2 = deque([(i, j)])
                while queue2:
                    x2,y2 = queue2.popleft()
                    cam0 = x2+h[0]
                    cam1 = y2+h[1]
                    if 0<=cam0<r and 0<= cam1<c:
                        if arr[cam0][cam1] != "W":
                            cams.add((cam0, cam1))
                            queue2.append((cam0,cam1))

print(cams)
bfs(start[0],start[1])
for i in empty:
    print(empty[i])