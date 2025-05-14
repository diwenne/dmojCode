from collections import deque
n,h = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
directions = [(0,1),(1,0),(0,-1),(-1,0)]

vis = set()

def bfs():
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        if (x,y) not in vis:
            vis.add((x,y))

            if (x,y) == (n-1,n-1):
                return "yes"

            else:
                for i in directions:
                    newX,newY = x+i[0], y+i[1]

                    if 0<=newX<n and 0<=newY<n:
                        if abs(graph[newX][newY]-graph[x][y])<=h:
                            queue.append((newX,newY))
    return "no"

print(bfs())



