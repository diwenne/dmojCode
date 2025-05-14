from collections import deque
directions = [(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1)]
n,q = map(int,input().split())
guards = []
graph = [[0 for _ in range(5000)]for _ in range(5000)]
# print(graph)
for i in range(n):
    a,b = map(int,input().split())
    guards.append((a,b))
def bfs():
    queue = deque([])
    for x,y in guards:
        queue.append((x,y,0))
    vis = set()
    while queue:
        # print(queue)
        x,y,length = queue.popleft()
        if (x,y) not in vis:
            vis.add((x,y))
            print(x,y)
            graph[x][y] = length

            for i in directions:
                newX = x+i[0]
                newY = y+i[1]
                if 0<=newX<=5000 and 0<= newY <= 5000:
                    print(newX,newY)
                    queue.append((newX,newY,length+1))

bfs()
print(graph)
for i in range(q):
    a,b = map(int,input().split())
    print(graph[a][b])
