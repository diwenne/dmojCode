from collections import deque
c = int(input())
graph = []
directions = [(1,0),(0,1),(-1,0),(0,-1)]
counter = 0
vis = set()
for i in range(2):
    graph.append(list(map(int,input().split())))
print(graph)
def bfs(x,y):
    shared = 0
    triangles = 0
    sharedvis = set()
    vis.add((x,y))
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        # print(x,y)
        triangles+=1
        for i in directions:
            newX = x+i[0]
            newY = y+i[1]
            if 0<=newX<2 and 0<=newY<c:
                if graph[newX][newY] == 1 and (x,y,newX,newY) not in sharedvis:
                    print(newX, newY)
                    sharedvis.add((x,y,newX,newY))
                    sharedvis.add((newX,newY,x,y))
                    shared+=1
                    if (newX, newY) not in vis:
                        queue.append([newX,newY])
                        vis.add((newX,newY))
    sides = 2*triangles+1
    print(sides,triangles)
    print(shared)
    return triangles*2 - shared*2
for row in range(2):
    for col in range(c):
        if graph[row][col] ==1 and (row,col) not in vis:
            counter+= bfs(row,col)


