from collections import deque
r,c = map(int,input().split())
graph = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(r):
    a = list(input())
    # print(a)
    if "S" in a:
        # print(a)
        b = a.index("S")
        start = (i,b)
    # if "D" in a:
    #     b = a.index("D")
    #     dest = (i,b)
    graph.append(a)

def bfs(x,y):
    queue = deque([(x,y,0)])
    # vis = set()
    while queue:
        x, y, length = queue.popleft()
        if (x,y) not in vis:
            vis.add((x,y))
            print(x,y)

            # print(x,y)
            if graph[x][y] == "." or graph[x][y] == "*":
                graph[x][y] = length
                # print(69)
            else:
                if graph[x][y]>length:
                    graph[x][y] = length
                    # print(70)

            for i in directions:
                # print(i[0],x)
                # print
                newX = x+i[0]
                newY = y+i[1]
                if 0<=newX<r and 0<=newY<c:
                    # print(newX,newY,10)
                    a = graph[newX][newY]
                    if a != "D" and a != "*" and a != "S" and a != "X":
                        # print(11)
                        queue.append((newX,newY,length+1))
vis = set()
for i in range(r):
    for j in range(c):

        if graph[i][j] == "*":
            bfs(i,j)
# for i in graph:
#     print(i)
# bfs(0,2)

def bfs2(s1,s2):
    queue = deque([(s1,s2,0)])
    vis = set()
    while queue:
        x,y,length = queue.popleft()
        if (x,y) not in vis:
            # print(x,y)
            # print(x,y)
            vis.add((x,y))
            if graph[x][y] == "D":
                # print(69)
                return length
            else:
                for i in directions:
                    newX = x+i[0]
                    newY = y+i[1]

                    if 0<=newX<r and 0<=newY<c:

                        a = graph[newX][newY]
                        if a != "X":
                            if type(a) == int:
                                # print(a)
                                if length+1 < a:

                                    queue.append((newX,newY,length+1))
                            elif a == ".":
                                queue.append((newX,newY,length+1))
                            elif a == "D":
                                queue.append((newX,newY,length+1))
    return "KAKTUS"
# for i in graph:
#     print(i)
print(bfs2(start[0],start[1]))

